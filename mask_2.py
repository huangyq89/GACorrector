import re
import time


def mask_2(genome):
    print(((time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))) + \
          ' Start masking sequences in the reference genome that aligned with sequences of new genes.')
    old_seq = readfasta(genome)
    readfasta('mask_result_1.txt')
    f = open('output.splign', 'r')
    a = f.readlines()
    f.close()
    f = open('old_sequence_2.txt', 'w')
    for line in a:
        if 'exon' in line:
            f.writelines(line)
            if re.findall(r'\|(\d+) *', line) != []:
                chromo = re.findall(r'\|(\d+) *', line)[0]
            elif re.findall(r'\|.*?\|(.*?)\|', line) != []:
                chromo = re.findall(r'\|.*?\|(.*?)\|', line)[0]
            else:
                continue
            start = re.findall(r'\s+(\d+)', line)[-2]
            end = re.findall(r'\s+(\d+)', line)[-1]
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
                    f.writelines(old_seq[num][start - 1:end] + '\n')
                    global seq
                    for s in seq[num]:
                        new.append(s)
                    new[start - 1:end] = 'K' * length
                    seq[num] = ''.join(new)
    sortline(seq)
    f.close()
    f = open('mask_result_2.txt', 'w')
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
    return(seq)

def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

def sortline(seq):
    for k in seq:
        new_k = ''
        for chunk in chunkstring(seq[seq.index(k)], 60):
            new_k += chunk + '\n'
        seq[seq.index(k)] = new_k
