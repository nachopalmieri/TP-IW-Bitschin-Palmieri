
import { UIElement, addClasses, removeClasses } from '../ui.js';

class Track {
    constructor({title, coverSrc, audioSrc} = {}) {
        this.title = title;
        this.coverSrc = coverSrc;
        this.audioSrc = audioSrc;
    }
}

class AudioPlayer extends UIElement {
    #audio;
    #onNextTrack = "next-track";
    #onPrevTrack = "prev-track";

    controls = {
        'main': true,
        'next': true,
        'prev': true
    }

    icons = {
        'play': ['fa', 'fa-play'],
        'next': ['fa', 'fa-next'],
        'prev': ['fa', 'fa-prev'],
        'pause': ['fa', 'fa-pause']
    }

    template = () => 
        document.querySelector('#audio-player-template');

    constructor(tracks = [], controls = {}, icons = {}) {
        super();
        this.#audio = null;
        this.isPlaying = false;
        this.currentTrack = null;
        this.controls = Object.assign(this.controls, controls);
        this.icons = Object.assign(this.icons, icons);

        this.setTracks(tracks);
    }

    initialize(component) {
        this.btnMain = component.querySelector('.btn-main');
        this.btnNext = component.querySelector('.btn-next');
        this.btnPrev = component.querySelector('.btn-prev');

        const _this = this;

        if (this.btnMain) {
            this.btnMain.addEventListener('click', (e) => _this.onBtnMainClick());
        }

        if (this.btnNext) {
            
            const icon = this.btnNext.querySelector('i') || this.btnNext.querySelector('svg');
            
            if (icon) {
                removeClasses(icon, this.icons.next);
                addClasses(icon, this.icons.next);
            }

            this.btnNext.addEventListener('click', (e) => _this.onBtnNextClick());

        }

        if (this.btnPrev) {
            
            const icon = this.btnPrev.querySelector('i') || this.btnPrev.querySelector('svg');
            
            if (icon) {
                removeClasses(icon, this.icons.next);
                addClasses(icon, this.icons.next);
            }

            this.btnPrev.addEventListener('click', (e) => _this.onBtnPrevClick());
        }

        this.imgCover = component.querySelector('.img-cover');
        this.labelCover = component.querySelector('.label-cover');

    }

    onBtnMainClick() {
        if (this.isPlaying) {
            this.pause();
        } else {
            this.play();
        }
    }

    onBtnNextClick(evnt) {
        this.moveToNextTrack();
        this.play();

        this.component.dispatchEvent(
            new Event(this.#onNextTrack, {
                sender: this, 
                track: this.currentTrack,
                trackIdx: this.tracks.indexOf(this.currentTrack)
            })
        );
    }

    onBtnPrevClick(evnt) {
        this.moveToPrevTrack();
        this.play();

        this.component.dispatchEvent(
            new Event(this.#onPrevTrack, {
                sender: this,
                track: this.currentTrack, 
                trackIdx: this.tracks.indexOf(this.currentTrack)
            })
        );
    }

    play() {
        if (this.#audio && !this.isPlaying) {
            this.isPlaying = true;
            this.#audio.play();
            this.render();
        }
    }

    pause() {
        if (this.#audio && this.isPlaying) {
            this.isPlaying = false;
            this.#audio.pause();
            this.render();
        }
    }

    getTrack({ current = 0, relative = false } = {}) {

        let actual = this.tracks.indexOf(this.currentTrack);

        if (actual < 0) {
            actual = 0;
        }
        
        if (!relative) {
            actual = current;
            current = 0;
        }

        return this.tracks[actual + current];

    }

    moveToTrack(current) {
        const newTrack = this.getTrack({ current, relative: true }) || this.currentTrack;
        this.setTrack(newTrack);
    }

    moveToNextTrack() {
        this.moveToTrack({current: +1});
    }

    moveToPrevTrack() {
        this.moveToTrack({current: -1});
    }

    setTrack(track) {
        if (track && track !== this.currentTrack) {
            this.currentTrack = track;
            this.#setAudio(this.currentTrack.audioSrc);
        } else if (!track) {
            this.currentTrack = null;
            this.#setAudio(null);
        }

        this.render();
    }

    setTracks(tracks) {
        this.tracks = tracks || [];
        this.setTrack(tracks[0]);
    }

    #setAudio(src) {

        if (this.#audio && this.#audio.src !== src) {

            if (this.isPlaying) {
                this.pause();
            }

        }

        if (src) {
            this.#audio = new Audio(src);
        } else {
            this.#audio = null;
        }

    }

    render() {

        if (this.currentTrack && this.imgCover) {
            if (this.imgCover.src !== this.currentTrack.coverSrc) {
                this.imgCover.src = this.currentTrack.coverSrc;
            }
        }

        if (this.btnMain) {
            if (this.controls.main) {

                const icon = this.btnMain.querySelector('i') || this.btnMain.querySelector('svg');

                if (icon) {
                    if (this.isPlaying) {
                        removeClasses(icon, this.icons.play);
                        addClasses(icon, this.icons.pause);
                    } else {
                        removeClasses(icon, this.icons.pause);
                        addClasses(icon, this.icons.play);
                    }
                }

                this.btnMain.style.display = 'block';
            } else {
                this.btnMain.style.display = 'none';
            }
        }

        if (this.btnNext) {
            
            const hasNext = this.getTrack({ current: +1, relative: true }) != null;

            if(hasNext && this.controls.next) {
                this.btnNext.style.display = 'block';
            } else {
                this.btnNext.style.display = 'none';
            }

        }

        if (this.btnPrev) {

            const hasPrev = this.getTrack({ current: -1, relative: true }) != null;

            if(hasPrev && this.controls.prev) {
                this.btnPrev.style.display = 'block';
            } else {
                this.btnPrev.style.display = 'none';
            }
        }

        if (this.currentTrack && this.labelCover) {
            this.labelCover.innerText = this.currentTrack.title;
        }

    }

    onremove() {
        this.btnMain = null;
        this.btnNext = null;
        this.btnPrev = null;
        this.imgCover = null;

        super.onremove();
    }

}

export { AudioPlayer, Track };