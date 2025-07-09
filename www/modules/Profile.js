import { tag, attr } from '/modules/tag.js'

// Shortcut functions
const li = (...x) => tag('li', ...x)
const ul = (...x) => tag('ul', ...x)
const className = (x) => attr('class', x)
const id = (x) => attr('id', x)

export default function({
    name,
    major,
    bio,
    role,
    joined,
    links,
    imgPath,
    isAlumni,
}) {
    // Convert all the links into anchor tags, if any exist
    const anchorTags = links?.map(({ name, href }) => tag('a',
        name || href,
        attr('href', href),
        attr('title', href),
    ))

    // Construct the image, if a path is given
    const img = !imgPath ? null : tag('img',
        className('profile-pic'),
        attr('src', imgPath),
        attr('alt', 'Profile image for ' + (name || 'unnamed member')),
        attr('title', 'Profile image for ' + (name || 'unnamed member')),
        attr('width', 150),
        attr('height', 150),
    )

    return tag('section',
        id(name?.toLowerCase().replaceAll(' ', '-')),
        className('profile' + (isAlumni ? ' alumni' : '')),
        tag('h3', name, className('profile-name')),
        img,
        ul(
            className('inline profile-meta'),
            major ? li(major) : null,
            joined ? li('Joined ', joined) : null,
            role ? li(role) : null,
        ),
        tag('p', bio, className('profile-bio')),
        !anchorTags ? null : tag('ul',
            className('profile-linktree'),
            // Wrap anchor tags in list item tags
            ...anchorTags.map((a) => li(a)),
        ),
    )
}
