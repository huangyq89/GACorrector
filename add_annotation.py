import os
def add_annotation(new_annotation_file, output_annotation):
    f = open(new_annotation_file, 'r')
    a = f.readlines()
    f.close()
    f = open('rename.gtf', 'a')
    f.writelines('\n')
    f.writelines(a)
    f.close()
    os.system('mv rename.gtf ' + output_annotation)
