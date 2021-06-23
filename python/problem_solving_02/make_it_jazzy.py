def make_it_jazzy(chords):
    return [chord + "7" if chord[-1] != "7" else chord for chord in chords]
