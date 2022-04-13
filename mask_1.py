import re
import time

def mask_1(genome):
    print(((time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))) + \
    ' Start masking sequences of duplicated genes in the reference genome.')
    readfasta(genome)
    f = open('places_to_mask.txt', 'r')
    a = f.readlines()
    f.close()
    f = open('old_sequence_1.txt', 'w')
    for line in a:
        f.writelines(line)
        match = re.findall(r'(\d+) *', line)
        chromo = match[0]
        start = match[1]
        end = match[2]
        start = int(start)
        end = int(end)
        if start > end:
            start, end = end, start
        global index
        for name in index:
            if re.match(chromo + '\s+', name) is not None:
                num = index.index(name)
                num = int(num)
                new = []
                length = end - start + 1
                global seq
                f.writelines(seq[num][start - 1:end] + '\n')
                for s in seq[num]:
                    new.append(s)
                new[start - 1:end] = 'K' * length
                seq[num] = ''.join(new)
    sortline(seq)
    f.close()
    f = open('mask_result_1.txt', 'w')
    i = 0
    while i < len(index):
        f.writelines('>' + index[i] + '\n')
        f.writelines(seq[i] + '\n')
        i += 1
    f.close()
    print(((time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))) + \
    ' Done!')

def readfasta(file):
    f = open(file)
    lines = f.readlines()
    f.close()
    lines.append('>')
    global index
    index = []
    global seq
    seq = []
    seqplast = ''
    for line in lines:
        if '>' in line:
            index.append(line.replace('\n', '').replace('>', ''))
            seq.append(seqplast.replace('\n', ''))
            seqplast = ''
        else:
            seqplast += line.replace('\n', '')
    index = index[:-1]
    seq = seq[1:]

def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

def sortline(seq):
    for k in seq:
        new_k = ''
        for chunk in chunkstring(seq[seq.index(k)], 60):
            new_k += chunk + '\n'
        seq[seq.index(k)] = new_k
