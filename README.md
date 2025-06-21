# OS2G.github.io

Club website for the Operating Systems & Open-Source Group at the University of
Nebraska-Lincoln.  The site is a pseudo-single page site written in vanilla
HTML, CSS, and javascript.

## File Structure

- The main layout and the `head` tag are located in `./index.html`, while all
  page content is found in the `./pages` directory.
- All styles should be kept to `./styles.css` (unless they are being applied
  inside a `template` tag).
- The directories `./images` and `./fonts` contain, well, images and fonts.

## Conventions

- Inline CSS should generally be avoided in favor of using more complicated CSS
  selectors.
- Inline javascript function calls and `onevent="function()"` HTML attributes
  are encouraged.
- CSS classes that apply keyframe animations to an element should be named in
  the format `kf-ANIMATION_NAME`, and classes that apply animations to elements
  *within* themselves should be in the format `kf-ANIMATION_NAME-container`.
