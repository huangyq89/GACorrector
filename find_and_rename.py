import re
import os
import time

def find_and_rename(annotation_file, sequence_file):
    f = open(sequence_file, 'r')
    a = f.readlines()
    f.close()
    num = 0
    for line in a:
        if re.match("^>", line) is not None:
            num += 1
    print('Received ' + str(num) + ' sequences as input.')
    print(((time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))) + \
    ' Start looking for and renaming duplicated genes in the old annotation file.')
    f = open(annotation_file, 'r')
    b = f.readlines()
    f.close()
    f = open('places_to_mask.txt', 'w')
    for line in a:
        if re.match("^>", line) is not None:
            chromo = re.findall(r'>(.*?)\s', line)[0]
            for line in b:
                if '"' + chromo + '"' or '-' + chromo + ';' in line:
                    f.writelines(line)
                    b[b.index(line)] = line.replace(chromo, chromo + "_old")
                    break
    f.close()
    f = open('rename.gtf', 'w')
    f.writelines(b)
    f.close()
    print(((time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))) + \
    ' Done!')
