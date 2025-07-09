import Profile from "/modules/Profile.js"

/**
 * Loads member data.
 * @param {string} href The URL of the JSON file containing member information.
 * @returns {Promise<[HTMLElement]>} The HTML profiles.
 */
const loadMembers = async (href) => {
    let json = await fetch(href, { 'Content-Type': 'text/json' })
        .then((resp) => resp.json())
        .catch((reason) => console.error(reason))

    // In case fetch failed
    json ||= []
    // Sort the profiles so that current members are first
    json.sort((a, b) => a.isAlumni && !b.isAlumni ? 1 :
                        !a.isAlumni && b.isAlumni ? -1 :
                        0)

    return json.map(Profile)
}

const main = async () => {
    document.getElementById('members')
        ?.replaceChildren(...await loadMembers('/data/members.json'))
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', main)
} else {
    main()
}
