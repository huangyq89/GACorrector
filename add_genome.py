import os
def add_genome(sequence_file, output_genome):
    f = open(sequence_file, 'r')
    a = f.readlines()
    f.close()
    f = open('mask_result_2.txt', 'a')
    f.writelines('\n')
    f.writelines(a)
    f.close()
    os.system('mv mask_result_2.txt ' + output_genome)
