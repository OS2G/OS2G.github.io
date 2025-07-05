/**
 * Creates new HTMLElements using document.createElement().
 * @param {string} name The name of the tag.
 * @param  {...HTMLElement | Text | Attr | string} children The children of the
 * tag.  Attaches attributes and HTML nodes as expected.
 * @returns {HTMLElement} The new element.
 */
export const tag = (name, ...children) => {
    const newTag = document.createElement(name)

    for (const child of children) {
        switch (true) {
            case child instanceof HTMLElement:
            case child instanceof Text:
                newTag.appendChild(child)
                break

            case child instanceof Attr:
                newTag.setAttributeNode(child.cloneNode())
                break

            case typeof child === 'string':
                newTag.appendChild(document.createTextNode(child))
                break

            case child === null || child === undefined:
                break

            default:
                console.warn('unknown type for tag function: ', child)
        }
    }

    return newTag
}

/**
 * Creates Attrs using document.createAttribute().
 * @param {string} key The name of the attribute.
 * @param {string} value The value of the attribute.
 * @returns {Attr} The new attribute node.
 */
export const attr = (key, value) => {
    const newAttr = document.createAttribute(key)
    newAttr.value = value || ''
    return newAttr
}
