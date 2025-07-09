# OS2G.github.io

Club website for the Operating Systems & Open-Source Group at the University of
Nebraska-Lincoln.  The site is written in vanilla HTML, CSS, and javascript,
and is accompanied by a simple SSG written in Python.

## File Structure

- The layout is found in `./layout.html`, and contains the `<head/>` tag along
  with any headers, footers, or navigation bars.  The page content will be
  inserted into the template in the place of the string `##CONTENTS##`.
- The un-transformed site can be found in the `./src` directory.  When the SSG
  runs, this directory is copied wholesale into the destination directory with
  every HTML file inserted into the layout.
  - Reusable javascript (modules) are in the `./src/modules` directory.
  - All styles are in `./src/styles.css`.
  - The directories `./src/images` and `./src/fonts` contain, well, images and
    fonts.
  - The `./src/data` directory contains additional resources, such as JSON
    files.
  - `./src/index.html` contains the home page.
  - `./src/404.html` contains the error page.
  - Subpages can be found in their own directories with there own `index.html`
    files — this is for prettier URLs.
- The destination directory is `./www/`.  This is the directory published to
  Github Pages.
- The SSG program can be found in `./ssg.py`.  It can be ran with
  `python3 ./ssg.py`.

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
