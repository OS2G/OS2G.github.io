---
title: filetypes
sub_title: operating systems & open source group
date: feb 12 2026
author: carston wiebe
theme:
  name: tokyonight-storm
  override:
    footer:
      style: template
      center: '<span style="color:grey">FILETYPES : MD : FEB 11 2026</span>'
      right: '{current_slide} / {total_slides}'
---

what are some filetypes?
===

<!--column_layout: [1, 1, 1, 1]-->

<!--column: 0-->

<!--pause-->

# audio

- mp3
- flac
- wav
- m4a
- ogg
- opus

# image

- png
- jpeg
- avif
- heic
- svg
- webp
- gif

<!--column: 1-->

# video

- mp4
- mov

# document

- pdf
- html
- docx
- pptx
- xlsx
- gdoc
- gslides
- gsheet
- epub
- mobi

<!--column: 2-->

# container

- mkv
- zip
- tar
- riff

# program

- jar
- exe
- apk
- apkm
- apks

<!--column: 3-->

# text

- txt
- md
- adoc

# code

- c
- java
- ...

# data

- json

<!--pause-->

# ???

- xml

common types
===

<!--column_layout: [1,1]-->

<!--column: 0-->

<!--pause-->

# riff

- resource interchange file format
- full of "chunks" of data (in bits)
- each chunk header contains the chunk's type and size

<!--column: 1-->

<!--pause-->

![image:width:100%](./images/riffinnards.png)

<!--column: 0-->

<!--pause-->

# xml

- full of "tags" which contain data (strings)
- tags open and close themselves and have attributes
<!--pause-->
- `<html><head></head><body></body></html>`

<!--pause-->

# zip

- compresses data using one of many algorithms
- primarily `deflate` (also used in pngs!)

how does your computer know a file's type?
===

<!--column_layout: [1, 4, 1]-->

<!--column: 1-->

<!--pause-->

# file extension

<!--pause-->

- easily fooled

<!--pause-->

# guess

<!--pause-->

- based on the file contents
- not always accurate or possible

<!--pause-->

# type signatures

- also called magic numbers
- opening x bits of the file

inside a pdf
===

![image:width:100%](./images/pdfinnards.png)

inside a png
===

<!--column_layout: [1, 1]-->

<!--column: 0-->

![image:width:100%](./images/pnginnards.png)

<!--pause-->

- eight byte signature
- `0x89504e470d0a1a0a`

<!--column: 1-->

<!--pause-->

`0x89`
: `0b10001001`, can't be 7-bit

<!--pause-->

`0x504e47`
: ascii for png

<!--pause-->

`0x0d0a`
: dos-style line ending

<!--pause-->

`0x1a`
: dos-style end-of-file

<!--pause-->

`0x0a`
: unix-style line ending

files that lie to you
===

<!--column_layout: [1, 1]-->

<!--column: 0-->

<!--pause-->

# how

- file extensions that don't match the file signature
- file extensions that do match, but take advantage of how a parser works

<!--pause-->

# why

- malicious intent
<!--pause-->
- completely normal reasons

<!--column: 1-->

# examples

<!--pause-->

- arbitrarily rename text files
<!--pause-->
- html vs xml
- svg vs xml
<!--pause-->
- wav vs riff
<!--pause-->
- jar vs zip
<!--pause-->
- gdoc vs json
<!--pause-->
- docx vs xml
- docx vs zip
<!--pause-->
- pptx vs xml
- pptx vs zip
<!--pause-->
- opf vs xml
- opf vs zip
<!--pause-->
- epub vs xml
- epub vs zip
<!--pause-->
- mobi vs xml
- mobi vs zip
<!--pause-->
- azw vs xml
- azw vs zip
<!--pause-->
- kf8 vs xml
- kf8 vs zip

everything is a zip file of xml
===

<!--column_layout: [1, 4, 1]-->

<!--column: 1-->

<!--pause-->

- turns out making your file format is hard
<!--pause-->
- using an existing one is easy
<!--pause-->
- but, you don't want your files getting read by the wrong software
<!--pause-->
- the practice goes back to at least 1991 w/ wav
<!--pause-->
- most filetypes are like this

real filetypes
===

# mkv

<!--column_layout: [1,1]-->

<!--column: 0-->

<!--pause-->
- from matroska (pronounced matryoshka, the word for russian nesting doll)
- released 2002
<!--pause-->
- container for unlimited audio, video, images, and subtitles
- commonly used as output from video/audio creation software, and you then
  strip out what you need
<!--pause-->
<!--column: 1-->
![](./images/obs.png)
<!--column: 0-->
<!--pause-->
- honorary zip file of xml, but for extensible binary meta language
<!--pause-->
- ebml is xml but binary, with opening/closing tags, created for mkvs
<!--pause-->
- arbitrary-length "tags" in binary with clever trick

real filetypes
===

<!--column_layout: [1,2,1]-->

<!--column: 1-->

# mp3

<!--pause-->
- lossy compression format that commonly achieves 75%--95% reduction in size
<!--pause-->
- revolutionized music distribution
<!--pause-->
- designed by the moving picture experts group, developed largely in germany
  by the fraunhofer society
<!--pause-->
- released 1991
<!--pause-->
- objectively very cool

real filetypes
===

<!--column_layout: [1, 1]-->

<!--column: 0-->

# mp3 file structure

![diagram showing the internal structure of an mp3 file taken from
[wikipedia](https://en.wikipedia.org/wiki/MP3#File_structure)](./images/mp3blocks.png)

<!--column: 1-->

<!--pause-->
# mp3 encoding

<!--pause-->
1.  divide the audio into small, overlapping pieces
<!--pause-->
1.  convert each piece into a sum of cos functions
<!--pause-->
1.  perform the fourier transform on each piece
<!--pause-->
1.  remove sounds humans can't hear
<!--pause-->
1.  encode each piece according to the bitrate
<!--pause-->
1.  format each piece into an mp3 header/data block

math stuff
===

<!--column_layout: [1,1]-->

<!--column: 0-->

<!--pause-->

# laplace

```typst +render
$
cal(L){1} &= 1/s \
cal(L){t} &= 1/s^2 \
cal(L){e^(a t)} &= 1/(s-a) \
cal(L){(d f(t)) / (d t)} &= s F(s)
$
```

<!--pause-->

# fourier

```typst +render
$
cal(F){cos(a t)} &= pi delta_a + pi delta_(-a)
$
```

<!--column: 1-->

<!--pause-->
## dct

- discrete cosine transform
<!--pause-->
  - type i   : dct
<!--pause-->
  - type ii  : idct
<!--pause-->
  - type iii : dst
<!--pause-->
  - **type iv  : mdct**

<!--pause-->
## fft

- fast fourier transform
- equivalent to discrete fourier transform
<!--pause-->
- mathematically the same, faster, *and* more accurate

real filetypes
===

<!--column_layout: [1,2,1]-->

<!--column: 1-->

# png

<!--pause-->
- lossless compression format
<!--pause-->
- pronounced "ping" apparently
<!--column: 0-->
![image:width:100%](./images/ping-pong.jpg)
<!--column: 1-->
<!--pause-->
- created to be an improved version of gif (pronounced "jif" apparently)
<!--column: 2-->
![image:width:100%](./images/jif.jpeg)
<!--column: 1-->
<!--pause-->
- designed by the portable network graphics development group
<!--pause-->
- released 1996

real filetypes
===

<!--column_layout: [1, 1]-->

<!--column: 0-->

# png file structure

<!--pause-->
- type signature: `0x89504e470d0a1a0a`
<!--pause-->
- made up of "chunks", like mp3s and riffs
<!--pause-->
- but png's headers are more fun
<!--pause-->
  - 4 bytes for size
  - 4 bytes for type
  - x bytes for data
  - 4 bytes for checksum

<!--column: 1-->

<!--pause-->
# png headers

<!--pause-->
- chunk types are given as ascii words
<!--pause-->
  - `IHDR`
  - `PLTE`
  - `IDAT`
  - `IEND`
  - `bKGD`
  - `gAMA`
  - `eXIf`
<!--pause-->
- the case of each letter gives additional info
<!--pause-->
  - 1st = critical
<!--pause-->
  - 2nd = public
<!--pause-->
  - 3rd = reserved
<!--pause-->
  - 4th = dependent

real filetypes
===

# png compression

<!--pause-->
- uses `deflate`
<!--pause-->
  - `deflate` *really* likes zeros
<!--pause-->
- first uses one of a number of prediction methods
<!--pause-->
  - that number is 1
<!--pause-->
- called method 0
<!--pause-->
  1.  do nothing
<!--pause-->
  1.  `next = prev`
<!--pause-->
  1.  `next = upper`
<!--pause-->
  1.  `next = prev upper`
<!--pause-->
  1.  `next = closest to prev + upper - prev upper`
<!--pause-->
- intended to get everything close to 0 for `deflate`s benefit
<!--pause-->
- basically, take the derivative of the image

closing
===

<!--column_layout: [1,4,1]-->

<!--column: 1-->

<!--pause-->
- most filetypes are fake
<!--pause-->
- basically just different ways of telling the computer to stop reading
<!--pause-->
- the real ones are normally for media
<!--pause-->
  - and use scary math like derivatives and transforms
<!--pause-->

in many ways they are very simple --- computers have to read them really fast,
and complication costs a lot

<!--end_slide-->
<!--jump_to_middle-->

fin.
===

<!--alignment: center-->
any questions?

activity
===

<!--alignment: center-->

# write a little parser

don't worry it's not that hard.  trust

<!--alignment: left-->

<!--new_line-->

<!--pause-->

<!--column_layout: [1,1]-->

<!--column: 0-->

# riff

```
id   : 4 bytes
size : 4 bytes
data : size bytes
pad  : 1 or 0 bytes (total must be even)
```

if id is `RIFF` or `LIST` then the first 4 bytes of data will be a name,
and the rest of data is more chunks

<!--column: 1-->

![image:width:100%](./images/riffinnards.png)
