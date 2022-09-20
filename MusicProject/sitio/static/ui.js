
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

            this.component = fragment.content.cloneNode(true);

            container.addEventListener('DOMNodeRemoved', this.onremove);

            for(const childContainer in Object.keys(this.childs)) {
                for (const child in childContainer) {
                    if (childContainer === 'root') {
                        child.create(container=this.component);
                    } else {
                        child.create(container=childContainer);
                    }
                }
            }

            this.render();

            container.appendChild(this.component);

        }

        return this.component;

    }

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

const addClasses = (element, classList) => {
    for (const cls in classList) {
        element.classList.add(cls);
    }
}

const removeClasses = (element, classList) => {
    for (const cls in classList) {
        element.classList.remove(cls);
    }
}

export { UIElement, addClasses, removeClasses };