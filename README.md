## Random Melody Creator
Creates a MIDI semi-randomly with specified features. Useful for people that want to write lyrics but can't write music. Helps you brainstorm what could possibly sound good as far as melodies go. Sample melody is included at the root of this repo (`midi.mid`)

## Usage:
1. Install `midicsv` (also installs a utility called `csvmidi`). You can `sudo apt install` it on Debian based installs, and it's available on Windows as well if you're torturing yourself with that OS.
2. Run `python3 random-melody.py`. You will be dropped into an interactive program and asked some questions. The program will then write your melody, in csv form, to `midi.csv`.
3. Run `midicsv midi.csv > midi.mid`
4. Upload midi.mid to https://onlinesequencer.net/ (via the large button at the top that says "Import MIDI" and play your melody! You can change speed by changing the BPM, or switch instruments. Sky is the limit
