---
title: Music Technology & Modular Synthesis
short: Music Tech & Synths
author: Carston Wiebe
date: Apr 09 2026
---

[TOC]

# Modular Synthesis

- Synthesize audio waves from first principles
- Analog (physical synth) and digital (DAW plugins)
- Imitate almost any instrument
- Create unique sounds

![Steve Porcaro (from Toto) with the Polyfusion Daimius
synth.](./img/polyfusion_daimius.jpg)

![A modern Moog synth (the Subsequent 25).](./img/modern_moog.jpg)

![The `synth1` VST plugin.](./img/synth1.png)

## Moog Synthesizer

- Created by Robert Moog
- Work started in 1963 after meeting Herb Deutsch
- Innovated in its use of transistors instead of vacuum tubes
- $16,000 grant

![The first commercial Moog synth.](./img/moog.jpg)

> According to Moog, when Deutsch saw this, he became excited and immediately
> began making music with the prototype, attracting the interest of passersby:
> "They would stand there, they'd listen and they'd shake their heads ... What
> is this weird shit coming out of the basement?"

- Presented at the annual Audio Engineering Society convention in 1964
- People bought his synth then and there, even though he didn't plan to sell it
- Built to order, no instruction books or guides

## Problems

- **Very** expensive
- Analog synths are specialized hardware
- Digital synths are subscriptions and proprietary software
- Choice overload

# Digital Audio Workstations

- One stop shop
- Common ones are:
    - Reaper
    - FL Studio
    - Ableton

![Reaper's interface.](./img/reaper.png)

### Virtual Studio Technology

- FOSS plugin system for DAWs
- Hundreds of thousands free and paid VSTs are available

# Synth Modules

- Many, many different types
- Control, modification, generation

### Eurorack

![A Eurorack... rack, I guess?](./img/eurorack.jpg)

- Based on the Eurocard standard
    - IEEE
    - Standard PCB sizes that can all fit into the same cases
- Uses U for height units and HP for width units
- +/-12V power

![Eurorack widths.  The standard height is 3U.](./img/hp_dims.jpg)

## Voltage Controlled Oscillators

- Create the base waveform that your human ears can hear
- Inputs control the pitch of the sounds, not the volume
- Most oscillator modules will have multiple VCOs

![Different waves VCOs can produce.](./img/waves.png)

## Voltage Controlled Filters

- The most basic way to modify sounds
- Typically, VCOs connect directly to VCFs

![Different types of filters.](./img/filters.jpg)

- `<INSERT FOURIER TRANSFORM TANGENT HERE>`

![A square wave that is poorly reconstructed.](./img/recon.png)

![A filtered square wave.](./img/rounded.gif)

- Filtering a sine wave is useless (or, technically it is volume control!)

## Voltage Controlled Amplifiers

- *Actual* volume control
- The only way to turn a VCO "off"

## Low Frequency Oscillators

- VCOs that produce sounds below the human range of hearing
- Used as control signals for other modules
- Vibratto, tremelo

### Frequency Modulation

![A simple FM setup.](./img/freqmod.png)

## Envelope Generators

- Unlike everything else mentioned here, these only "fire off" when a key is
  pressed
- Four properties
    - **Attack**
    - **Delay**
    - **Sustain**
    - **Release**

![The standard ADSR waveform.](./img/adsr.jpg)

## Ring Modulators

- Like FM but for the amplitude instead of the frequency

![Input and output waveforms in a ring modulator.  From top to bottom:
Carrier, modulator, output.](./img/ring_modulation.png)

## And More!

- Noise circuits create random noise (white, brown, blue, pink)
- Mixers combine multiple waves into one
- Splitters duplicate one wave into multiple
- Sequencers create repeating patterns

# My Synth

### Core Module

- A Raspberry Pi Pico with extra outputs duct-taped on.
- Control Signals and Power Supply
- Creates the CV using an I2C-controlled Digital-to-Analog Converter

![Kicad Schematic for the Core.](./img/core.png)

### Oscillator Module

- One VCO, one LFO

![Kicad Schematic for the Oscillator.](./img/osc.png)

### Filter Module

- Straight ripoff of the Polivoks filter

![Kicad Schematic for the Filter.](./img/vcf.png)

### Amp Module

- VCA and ADSR ENV

![Kicad Schematic for the VCA.](./img/vca.png)

## Assembled!

![The assembled Core and Oscillator boards.](./img/real.jpg)

# Software

### DAWs

- Reaper <https://reaper.fm>
- FL Studio <https://image-line.com/fl-studio>

### Plugins

- Synth1 <https://daichilab.sakura.ne.jp/softsynth>

### Misc.

- SunVox <https://warmplace.ru/soft/sunvox/>
