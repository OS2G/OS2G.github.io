---
title: INSTALL-A-THON
sub_title: (OS)2G
date: FEB 05 2026
author: Carston Wiebe
theme:
  name: tokyonight-storm
  override:
    footer:
      style: template
      center: '<span style="color:grey">(OS)2G</span>'
      right: '{current_slide} / {total_slides}'
---

Intro to Linux
===

<!--column_layout: [1,1,1]-->

<!--column: 0-->

<!--pause-->

# Distribution

- How the computer works "underneath"
- Package managers

<!--pause-->

## Common

- Debian
- Ubuntu
- Mint

<!--pause-->

## Specialized

- Arch
- NixOS
- Nobara

<!--column: 1-->

<!--pause-->

# Desktop Environment

- Graphical User Interface
- File manager
- Icons
- Themes
- Window Manager

<!--pause-->

## Common

- GNOME
- KDE
- XFCE

<!--column: 2-->

<!--pause-->

# Window Manager

- Often bundled w/ DE
- Placement and appearance of windows

<!--pause-->

## Specialized

- i3
- bspwn
- qtile
- xmonad
- Awesome
<!--pause-->
- herbstluftwm

Raspberry Pi Zero W
===

<!--column_layout: [2,1]-->

<!--column: 0-->

Today we will be installing **Raspberry Pi OS Lite (32-bit)** on the RPi Zero
W.

<!--pause-->

> [!NOTE]
> You could also try installing other lite distros, like Kali or Alpine.

<!--incremental_lists: true-->

1.  Plug your SD card into your computer
2.  Download and run the RPi Imager from the link

<!--column: 1-->

![](./images/rpisite.png)

**https://www.raspberrypi.com/software/**

<!--column: 0-->

3.  Select **Raspberry Pi Zero** as Device
4.  Select **Raspberry Pi OS (other) > Raspberry Pi OS Lite (32-bit)** as OS
5.  Follow prompts as directed
6.  Enable SSH
7.  ~~if it shows up~~ Enable USB Gadget mode
    - Else try Raspberry Pi Connect
8.  Write the image to the SD card
9.  Put the card into your Pi and plug your Pi into power / laptop

Connect to your Pi
===

<!--column_layout: [1,2,1]-->

<!--column: 1-->

Open a terminal or PuTTY and connect to your Pi.

```
ssh username@host
```

Common Commands
===

<!--column_layout: [1,1,1]-->

<!--column: 0-->

<!--pause-->

# Moving Files

- <span style="color:red">mkdir</span> makes directories

- <span style="color:red">cd</span> changes directories

- <span style="color:red">mv</span> moves files

- <span style="color:red">cp</span> copies files

- <span style="color:red">ls</span> lists files

<!--pause-->

# Editing Files

- <span style="color:red">nano</span> is an easy text editor
- <span style="color:red">vi</span>, <span style="color:red">vim</span>, or
  <span style="color:red">neovim</span> are what cool people use
- <span style="color:red">emacs</span>

<!--column: 1-->

<!--pause-->

# Getting Stuff

- <span style="color:red">nmtui</span> is the network manager

- <span style="color:red">sudo</span> is "super user does" AKA admin permissions

- <span style="color:red">apt</span> is a package manager
  - <span style="color:red">apt search</span>
  - <span style="color:red">sudo apt install</span>
  - <span style="color:red">sudo apt update</span>

- <span style="color:red">wget</span> downloads files from the internet

<!--column: 2-->

<!--pause-->

# Server-ish Stuff

- <span style="color:red">systemctl</span> controls background processes
  - <span style="color:red">sudo systemctl start</span> turns something on
  - <span style="color:red">sudo systemctl stop</span> turns something off
  - <span style="color:red">sudo systemctl enable</span> automatically turns
    something on
  - <span style="color:red">sudo systemctl disable</span> undoes enable

<!--pause-->

- <span style="color:red">cloudflared</span> is used to put websites on the internet

<!--pause-->

- <span style="color:red">tailscale</span> is used to connect devices in an internal network

<!--pause-->

- <span style="color:red">apache</span> is a classic web server

<!--end_slide-->

<!--jump_to_middle-->

Projects
===
