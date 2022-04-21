# GACorrector

GACorrector是一个基于Python的程序，用于参考基因组和注释的更新。GACorrector的输入文件是待更新的参考基因组、待更新的参考基因组注释文件、用于更新的新基因序列和新基因的注释文件；输出文件是更新后的参考基因组和更新后的参考基因组注释文件。

## 使用方法

在Linux命令行执行：

    git clone git://github.com/huangyq89/Genome_Corrector.git

进入`../Genome_Corrector/`目录，执行以下命令解压`tools.tar`包：

    tar -xzvf tools.tar

打开测试文件所在目录`../Genome_Corrector/test/`，在命令行执行以下命令：
    
    python ../Genome_Corrector.py test_genome.fa test_annotation.gtf test_sequence.fasta output_genome.fa output_annotation.gtf
    
接收的参数依次为`待更新的参考基因组`、`待更新的注释文件`、`用于更新的测序结果`、`更新后的参考基因组`和`更新后的注释文件`。

## 原理

`Genome Corrector`首先调用自带的`splign`（下载自NCBI），确定用于更新的测序结果在参考基因组中的位置，并生成`output.splign`文件；接下来`mask.py`根据`output.splign`中的结果屏蔽（以K替代）参考基因组中原有的序列；最后`add_genome.py`在参考基因组末尾添加新序列，`add_annotation.py`在注释文件末尾添加新序列的注释。
