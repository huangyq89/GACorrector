import re
import os

def find_and_rename(annotation_file, sequence_file):
    sentence = 'awk \'/^>/{if (l!=\"\") print l; print; l=0; next}{l+=length($0)}END{print l}\' ' + sequence_file + ' > sequence_read.txt'
    os.system(sentence)
    f = open('sequence_read.txt', 'r')
    a = f.readlines()
    f.close()
    f = open(annotation_file, 'r')
    b = f.readlines()
    f.close()
    f = open('places_to_mask.txt', 'w')
    for line in a:
        if re.match("^>", line) is not None:
            chromo = re.findall(r'>(.*?)\s', line)[0]
            for line in b:
                if chromo.lower() in line:
                    f.writelines(line)
                    b[b.index(line)] = line.replace(chromo.lower(), chromo.lower() + "_old")
                    break
    f.close()
    f = open('rename.gtf', 'w')
    f.writelines(b)
    f.close()

