
import { UIElement, addClasses, removeClasses } from 'ui.js';


export class AudioPlayer extends UIElement {

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
        this.tracks = tracks;
        this.currentTrack = null;
        this.controls = Object.assign(this.controls, controls);
        this.icons = Object.assign(this.icons, icons);

        this.setTrack(tracks[0]);
    }

    create(container = null) {
        const component = super.create(container);

        this.btnMain = component.querySelector('.btn-main');
        this.btnNext = component.querySelector('.btn-next');
        this.btnPrev = component.querySelector('.btn-prev');

        this.btnMain.addEventListener('click', this.onBtnMainClick);
        this.btnNext.addEventListener('click', this.onBtnNextClick);
        this.btnPrev.addEventListener('click', this.onBtnPrevClick);

        this.imgCover = component.querySelector('.img-cover');
        this.labelCover = component.querySelector('.label-cover');

        return component;
    }

    onBtnMainClick(evnt) {
        if (this.isPlaying) {
            this.pause();
        } else {
            this.play();
        }
    }

    onBtnNextClick(evnt) {
        this.moveToNextTrack();
        this.play();
    }

    onBtnPrevClick(evnt) {
        this.moveToPrevTrack();
        this.play();
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

    getTrack(current = 0, relative = false) {

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
        const newTrack = this.getTrack(current, relative=true) || this.currentTrack;
        this.setTrack(newTrack);
    }

    moveToNextTrack() {
        this.moveToTrack(current = +1);
    }

    moveToPrevTrack() {
        this.moveToTrack(current = -1);
    }

    setTrack(track) {
        if (track && track !== this.currentTrack) {
            this.currentTrack = track;
            this.#setAudio(this.currentTrack.audioSrc);
        } else if (!track) {
            this.currentTrack = null;
            this.#setAudio(null);
        }
    }

    #setAudio(src) {

        if (this.#audio && this.#audio.src !== src) {

            if (this.isPlaying) {
                this.pause();
            }

            if (src) {
                this.#audio = new Audio(src);
            } else {
                this.#audio = null;
            }

        }

    }

    render() {
        if (this.currentTrack) {
            if (this.imgCover.src !== this.currentTrack.coverSrc) {
                this.imgCover.src = this.currentTrack.coverSrc;
            }
        }

        if (this.btnMain) {
            if (this.controls.main) {
                if (this.isPlaying) {
                    removeClasses(this.btnMain, this.icons.pause);
                    addClasses(this.btnMain, this.icons.play);
                } else {
                    removeClasses(this.btnMain, this.icons.play);
                    addClasses(this.btnMain, this.icons.pause);
                }
                this.btnMain.show();
            } else {
                this.btnMain.hide();
            }
        }

        if (this.btnNext) {
            
            const hasNext = this.getTrack(current = +1, relative = true) != null;

            if(hasNext && this.controls.next) {
                this.btnNext.show();
            } else {
                this.btnNext.hide();
            }

        }

        if (this.btnPrev) {

            const hasPrev = this.getTrack(current = -1, relative = true) != null;

            if(hasPrev && this.controls.prev) {
                this.btnNext.show();
            } else {
                this.btnNext.hide();
            }
        }

        if (this.labelCover) {
            this.labelCover.innerText = "label";
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