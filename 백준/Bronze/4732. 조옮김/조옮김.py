import sys

# 기준 12음 (출력은 이 형식만 허용)
notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

# 음 → 인덱스 매핑
note_to_index = {note: i for i, note in enumerate(notes)}

# 동음이명 처리
enharmonic = {
    "Bb": "A#",
    "Db": "C#",
    "Eb": "D#",
    "Gb": "F#",
    "Ab": "G#",
    "B#": "C",
    "Fb": "E",
    "E#": "F",
    "Cb": "B"
}

while True:
    line = sys.stdin.readline().strip()
    if line == "***":
        break

    song = line.split()
    shift = int(sys.stdin.readline().strip())

    result = []

    for note in song:
        # 동음이명 처리
        if note in enharmonic:
            note = enharmonic[note]

        idx = note_to_index[note]
        new_idx = (idx + shift) % 12
        result.append(notes[new_idx])

    print(" ".join(result))