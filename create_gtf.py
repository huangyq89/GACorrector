import os
import re
import sys

def create_gtf(sequence_file, gtf_file, output_sequence_file):
    index = readfasta(sequence_file)[0]
    seq = readfasta(sequence_file)[1]
    sentence = 'awk \'/^>/{if (l!=\"\") print l; print; l=0; next}{l+=length($0)}END{print l}\' ' + sequence_file + ' > sequence_read.txt'
    os.system(sentence)
    f = open('sequence_read.txt', 'r')
    a = f.readlines()
    f.close()
    f = open('unfinished.gtf', 'w')
    gene_name = ''
    end = ''
    i = 2
    for line in a:
        if re.match("^>", line) is not None:
            if " gene:" in line:
                new_gene_name = re.findall(r' gene:(.*)', line)[0]
                chromo = new_gene_name
                transcript_name = re.findall(r'>(.*?)\s', line)[0]
                if new_gene_name != gene_name:
                    i = 2
                    gene_name = new_gene_name
                    index[index.index(line[1:-1])] = new_gene_name
                    start = '1'
                    end = a[a.index(line) + 1][:-1]
                    line_parse = chromo + '\thyq\tgene\t' + start + '\t' + end + '\t.\t+\t.\tgene_id "' + gene_name + \
                                 '"; gene_version "2"; gene_name "' + gene_name + \
                                 '"; gene_source "hyq"; gene_biotype "protein_coding";' + '\n' + \
                                 chromo + '\thyq\ttranscript\t' + start + '\t' + end + '\t.\t+\t.\tgene_id "' + gene_name + \
                                 '"; gene_version "2"; transcript_id "' + transcript_name + '"; transcript_version "2"; gene_name "' + \
                                 gene_name + '"; gene_source "hyq"; gene_biotype "protein_coding"; transcript_name "' + \
                                 transcript_name + '"; transcript_source "hyq"; transcript_biotype "protein_coding";' + '\n' + \
                                 chromo + '\thyq\texon\t' + start + '\t' + end + '\t.\t+\t.\tgene_id "' + gene_name + \
                                 '"; gene_version "2"; transcript_id "' + transcript_name + \
                                 '"; transcript_version "2"; exon_number "1"; gene_name "' + gene_name + \
                                 '"; transcript_version "2"; gene_name "' + gene_name + \
                                 '"; gene_source "hyq"; gene_biotype "protein_coding"; transcript_name "' + transcript_name + \
                                 '"; transcript_source "hyq"; transcript_biotype "protein_coding"; exon_id "' + transcript_name + \
                                 '"; exon_version "2";' + '\n' + \
                                 chromo + '\thyq\tCDS\t' + start + '\t' + end + '\t.\t+\t0\tgene_id "' + gene_name + \
                                 '"; gene_version "2"; transcript_id "' + transcript_name + \
                                 '"; transcript_version "2"; exon_number "1"; gene_name "' + gene_name + \
                                 '"; transcript_version "2"; gene_name "' + gene_name + \
                                 '"; gene_source "hyq"; gene_biotype "protein_coding"; transcript_name "' + transcript_name + \
                                 '"; transcript_source "hyq"; transcript_biotype "protein_coding"; protein_id "' + transcript_name + \
                                 '"; protein_version "2";' + '\n'
                    f.writelines(line_parse)
                else:
                    seq[index.index(new_gene_name)] += "N" * 1000 + seq[index.index(line[1:-1])]
                    seq.pop(index.index(line[1:-1]))
                    index.pop(index.index(line[1:-1]))
                    start = str(int(end) + 1000)
                    length = a[a.index(line) + 1][:-1]
                    end = str(int(start) + int(length))
                    line_parse = chromo + '\thyq\ttranscript\t' + start + '\t' + end + '\t.\t+\t.\tgene_id "' + gene_name + \
                                 '"; gene_version "2"; transcript_id "' + transcript_name + '"; transcript_version "2"; gene_name "' + \
                                 gene_name + '"; gene_source "hyq"; gene_biotype "protein_coding"; transcript_name "' + \
                                 transcript_name + '"; transcript_source "hyq"; transcript_biotype "protein_coding";' + '\n' + \
                                 chromo + '\thyq\texon\t' + start + '\t' + end + '\t.\t+\t.\tgene_id "' + gene_name + \
                                 '"; gene_version "2"; transcript_id "' + transcript_name + \
                                 '"; transcript_version "2"; exon_number "' + str(i) + '"; gene_name "' + gene_name + \
                                 '"; transcript_version "2"; gene_name "' + gene_name + \
                                 '"; gene_source "hyq"; gene_biotype "protein_coding"; transcript_name "' + transcript_name + \
                                 '"; transcript_source "hyq"; transcript_biotype "protein_coding"; exon_id "' + transcript_name + \
                                 '"; exon_version "2";' + '\n' + \
                                 chromo + '\thyq\tCDS\t' + start + '\t' + end + '\t.\t+\t0\tgene_id "' + gene_name + \
                                 '"; gene_version "2"; transcript_id "' + transcript_name + \
                                 '"; transcript_version "2"; exon_number "' + str(i) + '"; gene_name "' + gene_name + \
                                 '"; transcript_version "2"; gene_name "' + gene_name + \
                                 '"; gene_source "hyq"; gene_biotype "protein_coding"; transcript_name "' + transcript_name + \
                                 '"; transcript_source "hyq"; transcript_biotype "protein_coding"; protein_id "' + transcript_name + \
                                 '"; protein_version "2";' + '\n'
                    i += 1
                    f.writelines(line_parse)
            else:
                i = 2
                chromo = re.findall(r'>(.*?)\s', line)[0]
                gene_name = chromo
                start = '1'
                end = a[a.index(line) + 1][:-1]
                line_parse = chromo + '\thyq\tgene\t' + start + '\t' + end + '\t.\t+\t.\tgene_id "' + gene_name + \
                             '"; gene_version "2"; gene_name "' + gene_name + \
                             '"; gene_source "hyq"; gene_biotype "protein_coding";' + '\n' + \
                             chromo + '\thyq\ttranscript\t' + start + '\t' + end + '\t.\t+\t.\tgene_id "' + gene_name + \
                             '"; gene_version "2"; transcript_id "' + gene_name + '"; transcript_version "2"; gene_name "' + \
                             gene_name + '"; gene_source "hyq"; gene_biotype "protein_coding"; transcript_name "' + \
                             gene_name + '"; transcript_source "hyq"; transcript_biotype "protein_coding";' + '\n' + \
                             chromo + '\thyq\texon\t' + start + '\t' + end + '\t.\t+\t.\tgene_id "' + gene_name + \
                             '"; gene_version "2"; transcript_id "' + gene_name + \
                             '"; transcript_version "2"; exon_number "1"; gene_name "' + gene_name + \
                             '"; transcript_version "2"; gene_name "' + gene_name + \
                             '"; gene_source "hyq"; gene_biotype "protein_coding"; transcript_name "' + gene_name + \
                             '"; transcript_source "hyq"; transcript_biotype "protein_coding"; exon_id "' + gene_name + \
                             '"; exon_version "2";' + '\n' + \
                             chromo + '\thyq\tCDS\t' + start + '\t' + end + '\t.\t+\t0\tgene_id "' + gene_name + \
                             '"; gene_version "2"; transcript_id "' + gene_name + \
                             '"; transcript_version "2"; exon_number "1"; gene_name "' + gene_name + \
                             '"; transcript_version "2"; gene_name "' + gene_name + \
                             '"; gene_source "hyq"; gene_biotype "protein_coding"; transcript_name "' + gene_name + \
                             '"; transcript_source "hyq"; transcript_biotype "protein_coding"; protein_id "' + gene_name + \
                             '"; protein_version "2";' + '\n'
                f.writelines(line_parse)
    f.close()
    sortline(seq)
    f.close()
    f = open(output_sequence_file, 'w')
    i = 0
    while i < len(index):
        f.writelines('>' + index[i] + '\n')
        f.writelines(seq[i] + '\n')
        i += 1
    f.close()
    sentence = 'awk \'/^>/{if (l!=\"\") print l; print; l=0; next}{l+=length($0)}END{print l}\' ' + output_sequence_file + ' > sequence_read_2.txt'
    os.system(sentence)
    f = open('sequence_read_2.txt', 'r')
    b = f.readlines()
    f.close()
    f = open('unfinished.gtf', 'r')
    c = f.readlines()
    f.close()
    for line in b:
        if re.match("^>", line) is not None:
            chromo = line[1:-1]
            end = b[b.index(line) + 1][:-1]
            for line in c:
                if chromo in line:
                    c[c.index(line)] = line.replace(re.findall(r'gene\t1\t(\d+)', line)[0], end)
                    break
    f = open(gtf_file, 'w')
    f.writelines(c)
    f.close()

def readfasta(file):
    f = open(file)
    lines = f.readlines()
    f.close()
    lines.append('>')
    index = []
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
    return(index, seq)

def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

def sortline(seq):
    for k in seq:
        new_k = ''
        for chunk in chunkstring(seq[seq.index(k)], 60):
            new_k += chunk + '\n'
        seq[seq.index(k)] = new_k

create_gtf(sys.argv[1], sys.argv[2], sys.argv[3])
