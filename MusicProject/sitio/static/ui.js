
class UIElement {

    template = null;
    component = null;

    constructor() {
        this.childs = { 'root': [] };
    }

    child(instance, container = 'root') {
        if (!this.childs.hasOwnProperty(container)) {
            this.childs[container] = [];
        }

        if (!this.childs[container].includes(instance)) {
            this.childs[container].append(instance);
        }

        return instance;
    }
    
    create(container = null) {

        if(!container) {
            container = document.querySelector('body');
        }

        let fragment = this.template;

        if (typeof fragment === 'function') {
            fragment = fragment();
        }

        if (fragment) {

            const node = fragment.content.cloneNode(true);

            container.addEventListener('DOMNodeRemoved', this.onremove);

            container.appendChild(node);

            this.component = container.lastElementChild;

            for(const childContainerKey in Object.keys(this.childs)) {

                const childContainer = this.childs[childContainerKey];

                for (const child in childContainer) {
                    if (childContainerKey === 'root') {
                        child.create(container=this.component);
                    } else {
                        child.create(container=childContainer);
                    }
                }
            }
            
            this.initialize(this.component);

            this.render();

        }

        return this.component;

    }

    initialize(component) {}

    render() {}

    onremove(evnt) {
        if (this.component && (evnt.target == this.component || evnt.target == this.component.parentElement)) {
            this.component.parentElement.removeEventListener('DOMNodeRemoved', this.onremove);
            this.component = null;

            for(const childContainer in Object.keys(this.childs)) {
                for (const child in childContainer) {
                    child.onremove(evnt);
                }
            }
        }
    }

}

class Throttler {

    constructor(callback, time) {
        this.throttleTimer = false;
    }

    throttle(callback, time) {
        if (this.throttleTimer) return;

        this.throttleTimer = true;

        setTimeout(() => {
            callback();
            this.throttleTimer = false;
        }, time);
    }

}

const addClasses = (element, classList) => {
    classList.forEach(cls => {
        element.classList.add(cls);
    })
}

const removeClasses = (element, classList) => {
    classList.forEach(cls => {
        element.classList.remove(cls);
    })
}

export { UIElement, Throttler, addClasses, removeClasses };