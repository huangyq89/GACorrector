# GACorrector

GACorrector是一个基于Python的程序，用于参考基因组和注释的更新。GACorrector的输入文件是待更新的参考基因组、待更新的参考基因组注释文件、用于更新的新基因序列和新基因的注释文件；输出文件是更新后的参考基因组和更新后的参考基因组注释文件。

GACorrector is a Python-based program used to update reference genomes and annotations. GACorrector takes a reference genome, genome annotation, sequences of new gene models and the annotations of new gene models as input; the output is an updated reference genome and and updated genome annotation file.

## 使用方法
## Tutorial

在Linux命令行执行：
In Linux command line, run the following command:

    git clone https://github.com/huangyq89/GACorrector.git

进入`../GACorrector/`目录，执行以下命令解压`tools.tar`包：
enter`../GACorrector/`directory，run the following command to decompress`tools.tar`package:

    tar -xzvf tools.tar

打开测试文件所在目录`../GACorrector/test/`，在命令行执行以下命令：
open the directory with test files`../GACorrector/test/`, run the following command:

    python ../create_gtf.py test_sequence.fasta test_sequence_annotation.gtf processed_sequence.fasta

打开测试文件所在目录`../GACorrector/test/`，在命令行执行以下命令：
open the directory with test files`../GACorrector/test/`, run the following command:

    python ../GACorrector.py test_genome.fa test_annotation.gtf test_sequence.fasta  test_sequence_annotation.gtf output_genome.fa output_annotation.gtf processed_sequence.fasta

接收的参数依次为`待更新的参考基因组`、`待更新的注释文件`、`create_gtf.py处理过的新基因序列`、`新基因的注释文件`、`更新后的参考基因组`、`更新后的注释文件`和`新基因原始序列`。
Parameters accepted are in order as follows:`reference genome to be updated`、`genome annotation to be updated`、`new gene models sequences processed by create_gtf.py`、`annotation of new gene models`、`updated reference genome`、`updated genome annotation`and`raw sequences of new gene models`。
