# OS2G.github.io

Club website for the Operating Systems & Open-Source Group at the University of
Nebraska-Lincoln.  The site is a pseudo-single page site written in vanilla
HTML, CSS, and javascript.

## Dependencies

- [htmz](https://leanrada.com/htmz/)...?  It is a single-line of HTML that
  implementes a fraction of [htmx](https://htmx.org), but it has a few tricks
  up it's sleeve.

## File Structure

- The main layout and the `head` tag are located in `./index.html`, while all
  page content is found in the `./pages` directory.  Pages are loaded via htmz.
- Page-specific javascript (e.g. `main` functions) should be in `./pages` and
  should be named after their owners, e.g. `./pages/members.html` and
  `./pages/members.html.js`.
- Reusable javascript (modules) are in the `./modules` directory.
- All styles are in `./styles.css`.
- The directories `./images` and `./fonts` contain, well, images and fonts.
- The `./data` directory contains additional resources, such as JSON files.

## Conventions

- CSS classes that apply keyframe animations to an element should be named in
  the format `kf-ANIMATION_NAME`, and classes that apply animations to elements
  *within* themselves should be in the format `kf-ANIMATION_NAME-container`.

## Profiles

Member profiles are defined in `./data/members.json`, and have the following
fields (all optional):

`name`
:   Your name.

`major`
:   Your major(s).

`bio`
:   A short-ish biography.

`role`
:   Your role at OS2G (e.g. president, treasurer, et cetera) if any.

`joined`
:   The year you first joined OS2G.

`isAlumni`
:   Whether or not you have graduated.

`imgPath`
:   An absolute path to an image you want displayed.  Should be a square,
    and will be automatically sized to 150px by 150px.

`links`
:   A collection of links that each have a `name` and an `href`.
