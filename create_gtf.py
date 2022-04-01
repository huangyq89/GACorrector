import os
import re
import sys
def create_gtf(sequence_file, gtf_file):
    sentence = 'awk \'/^>/{if (l!=\"\") print l; print; l=0; next}{l+=length($0)}END{print l}\' ' + sequence_file + ' > sequence_read.txt'
    os.system(sentence)
    f = open('sequence_read.txt', 'r')
    a = f.readlines()
    f.close()
    f = open(gtf_file, 'w')
    for line in a:
        if re.match("^>", line) is not None:
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

create_gtf(sys.argv[1], sys.argv[2])
