# -*-coding: utf-8 -*-
# 分词
import jieba
import os
from word2vec.utils import files_processing

source_folder = './three_kingdoms/source'
segment_folder = './three_kingdoms/segment'

def segment_lines(file_list, segment_out_dir, stopwords=[]):
    for i, file in enumerate(file_list):
        segment_out_name = os.path.join(segment_out_dir, 'segment_{}.txt'.format(i))
        with open(file, 'rb') as f:
            document = f.read()
            document_cut = jieba.cut(document)
            sentence_segment = []
            for word in document_cut:
                if word not in stopwords:
                    sentence_segment.append(word)
            result = ' '.join(sentence_segment)
            result = result.encode('utf-8')
            with open(segment_out_name, 'wb') as f2:
                f2.write(result)

stopwords=[line.strip() for line in open('cn_stopwords.txt', encoding='utf-8').readlines()]
file_list = files_processing.get_files_list(source_folder,postfix='*.txt')
segment_lines(file_list, segment_folder)



