import { tag, attr, on } from '/modules/tag.js'
import Profile from '/modules/Profile.js'

const TextInput = (name, hint) => tag('input',
    attr('type', 'text'),
    attr('name', name),
    attr('placeholder', hint),
    attr('title', hint),
)

const TextAreaInput = (name, hint) => tag('textarea',
    attr('name', name),
    attr('placeholder', hint),
    attr('title', hint),
    attr('spellcheck', 'false'),
)

const CheckboxInput = (name, hint) => tag('input',
    attr('type', 'checkbox'),
    attr('name', name),
    attr('title', hint),
)

const Button = (name, hint, callback) => tag('button',
    attr('type', 'button'),
    attr('class', name),
    on('click', callback),
    hint,
)

/**
 * Creates a link input that allows entry of a URL and a display name, and has
 * a button to delete the entry.
 * @returns {HTMLElement} A list item containing form fields.
 */
const LinkRow = () => {
    const This = tag('li',
        TextInput('link-href', 'Link URL'),
        TextInput('link-text', 'Display name'),
        Button('remove-link', 'Remove link', () => This.remove())
    )

    return This
}

export default function() {
    const NameInput = TextInput('name', 'Your name')
    const MajorInput = TextInput('major', 'Your major(s)')
    const BioInput = TextAreaInput('bio', 'A little about you')
    const RoleInput = TextInput('role', 'Your role at OS2G')
    const JoinedInput = TextInput('joined', 'The year you joined')
    const ImgPathInput = TextInput('img-path', 'Filename of your profile pic')
    const IsAlumniInput = CheckboxInput('is-alumni', 'Have you graduated?')
    const Links = tag('ul',
        attr('class', 'profile-form-links'),
        Button('add-link', 'Add link', () => Links.prepend(LinkRow()))
    )

    const profileJson = () => ({
        name: NameInput.value,
        major: MajorInput.value,
        bio: BioInput.value,
        role: RoleInput.value,
        joined: JoinedInput.value,
        links: Array.from(Links.getElementsByTagName('li'))
                    .map((Li) => ({
                        name: Li.querySelector('[name="link-text"]')?.value,
                        href: Li.querySelector('[name="link-href"]')?.value,
                    })),
        imgPath: ImgPathInput.value ? '/images/' + ImgPathInput.value : null,
        isAlumni: IsAlumniInput.checked,
    })

    const DownloadButton = Button(
        'profile-form-download',
        'Download JSON',
        () => {
            const data = btoa(JSON.stringify(profileJson()))
            const url = "data:application/json;base64," + data
            const dummyLink = tag('a',
                attr('href', url),
                attr('download', 'profile.json'),
            )
            dummyLink.dispatchEvent(new MouseEvent('click'))
        },
    )

    const CopyButton = Button(
        'profile-form-copy',
        'Copy JSON',
        () => {
            navigator.clipboard.writeText(JSON.stringify(profileJson()))
        },
    )

    const ProfileOutput = tag('output', attr('name', 'profile'))

    const updateForm = () => {
        ProfileOutput.replaceChildren(Profile(profileJson()))
    }

    return tag('form',
        attr('class', 'profile-form'),
        on('change input click', updateForm),
        NameInput,
        MajorInput,
        BioInput,
        Links,
        RoleInput,
        JoinedInput,
        ImgPathInput,
        tag('label',
            attr('class', 'for-alumni'),
            IsAlumniInput,
            IsAlumniInput.title
        ),
        CopyButton,
        DownloadButton,
        ProfileOutput,
    )
}
