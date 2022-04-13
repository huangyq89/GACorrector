import os
import time

def splign(sequence_file):
    print(((time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))) + \
    ' Start aligning sequences of new genes to the reference genome using Splign.')
    os.system('mkdir execute_splign')
    sentence = 'cp ' + sequence_file + ' mask_result_1.txt execute_splign'
    os.system(sentence)
    os.system('../splign -mklds execute_splign')
    os.system('../makeblastdb -dbtype nucl -parse_seqids -in execute_splign/' + sequence_file + ' > makedblog_1.txt')
    os.system('../makeblastdb -dbtype nucl -parse_seqids -in execute_splign/mask_result_1.txt > makedblog_2.txt')
    os.system('../compart -qdb execute_splign/' + sequence_file + ' -sdb execute_splign/mask_result_1.txt > output.compartments')
    os.system('../splign -ldsdir execute_splign -comps output.compartments > output.splign')
    print(((time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))) + \
    ' Done!')
