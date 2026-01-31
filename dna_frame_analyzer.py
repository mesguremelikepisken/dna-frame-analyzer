def delet_gap(dna):
    clear = ""
    for base in dna.upper():
        if base in ["A", "T", "C", "G"]:
            clear += base
    return clear

def frame_creat(dna):
    frame0 = dna
    frame1 = dna[1:]
    frame2 = dna[2:]
    return [frame0, frame1, frame2]

def control_stop_codon(frame):
    stoplar = ["TAA", "TAG", "TGA"]
    for i in range(0, len(frame) - 2, 3):
        kodon = frame[i:i+3]
        if kodon in stoplar:
            return True
    return False


def control_begin_codon(frame):
    for i in range(0, len(frame) - 2, 3):
        codon = frame[i:i+3]
        if codon == "ATG":
            return True
    return False

def foun_best_frame(dna):
    frames = frame_creat(dna)
    for index, frame in enumerate(frames):
        there_is_stop = control_stop_codon(frame)
        there_is_begin = control_begin_codon(frame)

        if not there_is_stop and there_is_begin:
            return f"Best frame is Frame {index} with sequence: {frame}"
        
    return "No suitable frame found."

def begin_analize():
    dna = input("Please enter DNA sequence: ")
    clear_dna = delet_gap(dna)
    result = foun_best_frame(clear_dna)
    print(result)


begin_analize()
