def aa_percentage(proteinseq, aminoacid):
    seq = proteinseq.upper()
    aa = aminoacid.upper()
    length = len(seq)
    aa_count = seq.count(aa)
    percentage = aa_count / length *100
    return(percentage)
assert round(aa_percentage("MSRSLLLRFLLFLLLLPPLP", "M")) == round(5)
assert round(aa_percentage("MSRSLLLRFLLFLLLLPPLP", "r")) == round(10)
assert round(aa_percentage("MSRSLLLRFLLFLLLLPPLP", "L")) == round(50)
assert round(aa_percentage("MSRSLLLRFLLFLLLLPPLP", "Y")) == round(0)

def base_counter(DNA_sequence, threshold):
    seq = DNA_sequence.upper()
    counter = 0
    for base in seq:
        if base in ["A", "T", "C", "G"]:
            continue
        else:
            counter = counter + 1
    proportion = counter / len(seq)
    return proportion >= threshold
assert base_counter("ATCGATCGATCGATCGXXXX",0.15) == True
assert base_counter("ATCGATCGATCGATCGXXXX",0.21) == False

def Kmer_counting1(DNA_sequence, kmersize = 4, minfrequency = 0):
    i=0
    seq = DNA_sequence.upper()
    frequency = {}
    for i in range(len(seq)- kmersize):
        a = seq[i:i+kmersize]
        frequency[a] = frequency.get(a,0) + 1
    for key in frequency:
        if frequency[key] > minfrequency:
            print(key)

def Kmer_counting2(DNA_sequence, kmersize = 4, minfrequency = 0):
    i=0
    seq = DNA_sequence.upper()
    frequency = {}
    ls = []
    for i in range(len(seq)- kmersize):
        a = seq[i:i+kmersize]
        frequency[a] = frequency.get(a,0) + 1
    for key in frequency:
        if frequency[key] > minfrequency:
            ls.append(key)
    print(ls)
