import ProfileForm from "/modules/ProfileForm.js"

const main = () => {
    document.getElementById('create-profile')?.replaceChildren(ProfileForm())
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', main)
} else {
    main()
}
