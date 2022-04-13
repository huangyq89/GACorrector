import os
import time

def add_annotation(new_annotation_file, output_annotation):
    print(((time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))) + \
    ' Start adding new annotations to the old annotation file.')
    f = open(new_annotation_file, 'r')
    a = f.readlines()
    f.close()
    f = open('rename.gtf', 'a')
    f.writelines('\n')
    f.writelines(a)
    f.close()
    os.system('mv rename.gtf ' + output_annotation)
    print(((time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))) + \
    ' Done!')

