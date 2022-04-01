import os
import re
def create_gff(sequence_file, gff_file):
    sentence = 'awk \'/^>/{if (l!=\"\") print l; print; l=0; next}{l+=length($0)}END{print l}\' ' + sequence_file + ' > sequence_read.txt'
    os.system(sentence)
    f = open('sequence_read.txt', 'r')
    a = f.readlines()
    f.close()
    f = open(gff_file, 'w')
    for line in a:
        if re.match("^>", line) is not None:
            chromo = line[1:-1]
            gene_name = chromo
            start = '1'
            end = a[a.index(line) + 1][:-1]
            line_parse = chromo + '\thyq\tregion\t' + start + '\t' + end + '\t.\t+\t.\tID=' + gene_name + ';Dbxref=' + \
                         gene_name + ';Name=' + gene_name + ';chromosome=' + gene_name + \
                         ';gbkey=Src;genome=chromosome;mol_type=genomicDNA;strain=Tuebingen' + '\n' + \
                         chromo + '\thyq\tgene\t' + start + '\t' + end + '\t.\t+\t.\tID=gene-' + gene_name + \
                         ';Dbxref=' + gene_name + ';Name=' + gene_name + ';description=' + gene_name + \
                         ';gbkey=Gene;gene=' + gene_name + ';gene_biotype=protein_coding;gene_synonym=' + gene_name + '\n' + \
                         chromo + '\thyq\ttranscript\t' + start + '\t' + end + '\t.\t+\t.\tID=rna-' + gene_name + \
                         'Parent=gene-' + gene_name + ';Dbxref=' + gene_name + ';Name=' + gene_name + \
                         'gbkey=mRNA;gene=' + gene_name + ';gene=' + gene_name + ';product=' + gene_name + \
                         ';transcript_id=' + gene_name + '\n' + \
                         chromo + '\thyq\texon\t' + start + '\t' + end + '\t.\t+\t.\tID=exon-' + gene_name + \
                         'Parent=rna-' + gene_name + ';Dbxref=' + gene_name + 'gbkey=mRNA;gene=' + gene_name + ';gene=' + \
                         gene_name + ';product=' + gene_name + ';transcript_id=' + gene_name + '\n' + \
                         chromo + '\thyq\tCDS\t' + start + '\t' + end + '\t.\t+\t0\tID=cds-' + gene_name + \
                         'Parent=rna-' + gene_name + ';Dbxref=' + gene_name + ';Name=' + gene_name + \
                         'gbkey=CDS;gene=' + gene_name + ';gene=' + gene_name + ';product=' + gene_name + \
                         ';protein_id=' + gene_name + '\n'
            f.writelines(line_parse)
    f.close()

create_gff(sys.argv[1], sys.argv[2])
