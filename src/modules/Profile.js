import { tag, attr } from '/modules/tag.js'

// Shortcut functions
const Li = (...x) => tag('li', ...x)
const Ul = (...x) => tag('ul', ...x)
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
    const AnchorTags = links?.map(({ name, href }) => tag('a',
        name || href,
        attr('href', href),
        attr('title', href),
    ))

    // Construct the image, if a path is given
    const Img = !imgPath ? null : tag('img',
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
        Img,
        Ul(
            className('inline profile-meta'),
            major ? Li(major) : null,
            joined ? Li('Joined ', joined) : null,
            role ? Li(role) : null,
        ),
        tag('p', bio, className('profile-bio')),
        !AnchorTags ? null : Ul(
            className('profile-linktree'),
            // Wrap anchor tags in list item tags
            ...AnchorTags.map((Anchor) => Li(Anchor)),
        ),
    )
}
