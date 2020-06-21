# -*-coding: utf-8 -*-
# Word2Vec，计算相似度
from gensim.models import word2vec
import multiprocessing

# 若存在多个文件,使用PathLineSentence
segment_folder = './three_kingdoms/segment'
sentences = word2vec.PathLineSentences(segment_folder)

# 设置模型参数,进行训练
model = word2vec.Word2Vec(sentences, size=128, window=5, min_count=5,workers=multiprocessing.cpu_count())
# 保存模型
model.save('./models/word2vec_TK.model')
for wv in model.wv.similar_by_word('曹操', topn=20):
    if len(wv[0]) == 2 or len(wv[0]) == 3:
        print(wv[0], wv[1])
print(model.wv.similarity('曹操', '曹孟德'))
print(model.wv.most_similar(positive=['曹操', '刘备'], negative=['张飞']))
print(model.wv.most_similar(positive=['曹操', '袁绍'], negative=['袁本初']))