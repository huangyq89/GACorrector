import os
import time

def add_genome(sequence_file, output_genome):
    print(((time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))) + \
    ' Start adding sequences of new genes to the reference genome.')
    f = open(sequence_file, 'r')
    a = f.readlines()
    f.close()
    f = open('mask_result_2.txt', 'a')
    f.writelines('\n')
    f.writelines(a)
    f.close()
    os.system('mv mask_result_2.txt ' + output_genome)
    print(((time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))) + \
    ' Done!')
