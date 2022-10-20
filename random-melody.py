import random
#import sys

#https://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies -> https://www.convertcsv.com/html-table-to-csv.htm -> some data wrangling in a repl
midi_map = {'G9': 127, 'F#9': 126, 'Gb9': 126, 'F9': 125, 'E9': 124, 'D#9': 123, 'Eb9': 123, 'D9': 122, 'C#9': 121, 'Db9': 121, 'C9': 120, 'B8': 119, 'A#8': 118, 'Bb8': 118, 'A8': 117, 'G#8': 116, 'Ab8': 116, 'G8': 115, 'F#8': 114, 'Gb8': 114, 'F8': 113, 'E8': 112, 'D#8': 111, 'Eb8': 111, 'D8': 110, 'C#8': 109, 'Db8': 109, 'C8': 108, 'B7': 107, 'A#7': 106, 'Bb7': 106, 'A7': 105, 'G#7': 104, 'Ab7': 104, 'G7': 103, 'F#7': 102, 'Gb7': 102, 'F7': 101, 'E7': 100, 'D#7': 99, 'Eb7': 99, 'D7': 98, 'C#7': 97, 'Db7': 97, 'C7': 96, 'B6': 95, 'A#6': 94, 'Bb6': 94, 'A6': 93, 'G#6': 92, 'Ab6': 92, 'G6': 91, 'F#6': 90, 'Gb6': 90, 'F6': 89, 'E6': 88, 'D#6': 87, 'Eb6': 87, 'D6': 86, 'C#6': 85, 'Db6': 85, 'C6': 84, 'B5': 83, 'A#5': 82, 'Bb5': 82, 'A5': 81, 'G#5': 80, 'Ab5': 80, 'G5': 79, 'F#5': 78, 'Gb5': 78, 'F5': 77, 'E5': 76, 'D#5': 75, 'Eb5': 75, 'D5': 74, 'C#5': 73, 'Db5': 73, 'C5': 72, 'B4': 71, 'A#4': 70, 'Bb4': 70, 'A4': 69, 'G#4': 68, 'Ab4': 68, 'G4': 67, 'F#4': 66, 'Gb4': 66, 'F4': 65, 'E4': 64, 'D#4': 63, 'Eb4': 63, 'D4': 62, 'C#4': 61, 'Db4': 61, 'C4': 60, 'B3': 59, 'A#3': 58, 'Bb3': 58, 'A3': 57, 'G#3': 56, 'Ab3': 56, 'G3': 55, 'F#3': 54, 'Gb3': 54, 'F3': 53, 'E3': 52, 'D#3': 51, 'Eb3': 51, 'D3': 50, 'C#3': 49, 'Db3': 49, 'C3': 48, 'B2': 47, 'A#2': 46, 'Bb2': 46, 'A2': 45, 'G#2': 44, 'Ab2': 44, 'G2': 43, 'F#2': 42, 'Gb2': 42, 'F2': 41, 'E2': 40, 'D#2': 39, 'Eb2': 39, 'D2': 38, 'C#2': 37, 'Db2': 37, 'C2': 36, 'B1': 35, 'A#1': 34, 'Bb1': 34, 'A1': 33, 'G#1': 32, 'Ab1': 32, 'G1': 31, 'F#1': 30, 'Gb1': 30, 'F1': 29, 'E1': 28, 'D#1': 27, 'Eb1': 27, 'D1': 26, 'C#1': 25, 'Db1': 25, 'C1': 24, 'B0': 23, 'A#0': 22, 'Bb0': 22, 'A0': 21}

final_midi = ""
note_len_total = 0

#if str(sys.argv)[1] == "-i":

verse_counter = 1

final_midi = """0, 0, Header, 1, 2, 384
1, 0, Start_track
1, 0, Time_signature, 4, 2, 24, 8
1, 0, Tempo, 1000000
1, 0, End_track
2, 0, Start_track
2, 0, Program_c, 0, 0\n"""

while(True):
    print(f"Starting verse {verse_counter}")
    
    rng = input("What range would you like to use? (ie 'A3-A#6'): ")
    if "-" in rng:
        rng = rng.split("-")
        note_lower = midi_map[rng[0]]
        note_higher = midi_map[rng[-1]]
    else:
        note_lower = midi_map[rng]
        note_higher = midi_map[rng]

    note_len = input("Note length range in ms (eg 50-100): ")
    if "-" in note_len:
        note_len = note_len.split("-")
    else:
        note_len = [note_len]
    note_len_min = int(note_len[0])
    note_len_max = int(note_len[-1])
    print(note_len_min, note_len_max)

    verse_len = int(input("How many notes should this verse have: "))
    print(verse_len)

    ##########################################################

    notes = [random.randint(note_lower,note_higher) for x in range(verse_len)]
    
    #if "y" in input("Add a longer note somewhere? (y/n): "):
    #    longer = random.randint(0,len(notes)-1)
    #else:
    #    longer = -1
    
    for y in notes:
        note_len = random.randint(note_len_min, note_len_max)
        #if x == longer:
        #    note_len += 200
        final_midi += f"2, {note_len_total}, Note_on_c, 0, {y}, 50\n"
        note_len_total += note_len
        final_midi += f"2, {note_len_total}, Note_off_c, 0, {y}, 0\n"
    
    if "n" in input("Another verse? (y/n): "):
        break

    pause_between = int(input("How many ms should the pause between verses be? "))
    note_len_total += pause_between

    verse_counter += 1


final_midi += f"2, {note_len_total}, End_track\n0, 0, End_of_file"

f = open("midi.csv", "w+")
f.write(final_midi)
f.close()

print("\n" + final_midi)
