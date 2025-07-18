/**
 * Creates new HTMLElements using document.createElement().
 * @param {string} name The name of the tag.
 * @param  {...HTMLElement | Text | Attr | string | EventContainer} children
 * The children of the tag.  Attaches attributes and HTML nodes as expected.
 * @returns {HTMLElement} The new element.
 */
export const tag = (name, ...children) => {
    const tagNode = document.createElement(name)

    for (const child of children) {
        switch (true) {
            case child instanceof HTMLElement:
            case child instanceof Text:
                tagNode.appendChild(child)
                break

            case child instanceof Attr:
                tagNode.setAttributeNode(child.cloneNode())
                break

            case child instanceof EventContainer:
                for (const event of child.events) {
                    tagNode.addEventListener(event, child.callback)
                }
                break

            case typeof child === 'string':
                tagNode.appendChild(document.createTextNode(child))
                break

            case child === null || child === undefined:
                break

            default:
                console.warn('unknown type for tag function: ', child)
        }
    }

    return tagNode
}

/**
 * Creates Attrs using document.createAttribute().
 * @param {string} key The name of the attribute.
 * @param {string} value The value of the attribute.
 * @returns {Attr} The new attribute node.
 */
export const attr = (key, value) => {
    const attrNode = document.createAttribute(key)
    attrNode.value = value || ''
    return attrNode
}

/**
 * Container class that holds a potential event listener.
 */
class EventContainer {
    /**
     * Constructs an event container.
     * @param {[string]} events List of events that trigger the callback.
     * @param {EventCallback} callback The callback function.
     */
    constructor(events, callback) {
        this.events = events
        this.callback = callback
    }
}

/**
 * Creates a potential event listener that can be attached via the tag
 * function.
 * @param {string} events The list of events separated by spaces.
 * @param {EventCallback} callback The callback function.
 * @returns {EventContainer} An event container.
 */
export const on = (events, callback) => {
    return new EventContainer(events.split(' '), callback)
}
