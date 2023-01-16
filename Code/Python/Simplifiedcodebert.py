# -*- coding: utf-8 -*-
"""semantic_clone_bench_dataset_evaluation_codebert.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XqGJS9Qh7IsjI0flsycEWv9SRVtTcZCr
"""

# from google.colab import drive
#
# drive.mount('/content/gdrive/', force_remount=True)

# Commented out IPython magic to ensure Python compatibility.
# %cd gdrive/MyDrive

# !pip install transformers==4.0.1
# !pip install torch===1.7.0
# !pip install numpy===1.19.2
# !pip install -U scikit-learn
# !pip install seaborn===0.11.0
# !pip install pandas===1.1.3
# !pip install tqdm===4.50.2
# tensorflow.keras.models
# import sys
# sys.path.append('G:\\checkpoint-best-f1') #folder which contains model, snn etc.,
# import shap
from model import Model
from transformers import (RobertaConfig, RobertaModel, RobertaTokenizer)
import torch
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import seaborn as sns
import json
import numpy
from numpy import argmax, save, load, sum, sqrt
from numpy.linalg import norm
import os
from collections import Counter
import pandas as pd
from tqdm.notebook import tqdm
import re
import numpy as np
import json
import os
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

device = torch.device("cpu")
BLOCK_SIZE = 400

config = RobertaConfig.from_pretrained('roberta-base')
model = RobertaModel.from_pretrained('microsoft/codebert-base')
tokenizer = RobertaTokenizer.from_pretrained('roberta-base')

model = Model(model,config,tokenizer)

model_path = 'mymodel.bin'
model.load_state_dict(torch.load(model_path, map_location=lambda storage, loc: storage), strict=False)
model.to(device)

def myfunc():

    device = torch.device("cpu")
    # path = 'D:/SMU/OneDrive - Singapore Management University/Gen. Work Artifacts/Xplain_CodeBERT_SemClone/test/MutatedSemanticClonePairs'
    path = 'pythontestfolder'
    clone_files = os.listdir(path)

    def read_file_python(filename):
        ori_file = open(path + "/" + filename, "r")
        list_lines = []
        line = ori_file.readline()
        while line:
            list_lines.append(line)
            line = ori_file.readline()
        for i in range(len(list_lines)):
            if list_lines[i] == "\n" and list_lines[i + 1] == "\n":
                m1 = list_lines[:i]
                m2 = list_lines[i + 2:]
                break
        if m1 and m2:
            m1_str = ""
            m2_str = ""
            for line in m1:
                m1_str += line
            for line in m2:
                m2_str += line
            return m1_str, m2_str
        else:
            print("Error occurs while detecting method 1 and method 2.")
            return None, None

    clone_files

    # generate dissimilar pairs
    pairs = []
    for file_name in clone_files:
        code_1, code_2 = read_file_python(file_name)
        pairs.append((code_1, code_2))

    i= 0
    for pair in pairs:
        if not pair[0] or not pair[1]:
            print(i)
        i+=1

    len(clone_files)




    def convert_examples_to_features(code_1, code_2):

        code1_tokens=tokenizer.tokenize(code_1)
        code1_tokens=code1_tokens[:BLOCK_SIZE-2]
        code1_tokens =[tokenizer.cls_token]+code1_tokens+[tokenizer.sep_token]
        code1_ids=tokenizer.convert_tokens_to_ids(code1_tokens)
        padding_length = BLOCK_SIZE - len(code1_ids)
        code1_ids+=[tokenizer.pad_token_id]*padding_length

        code2_tokens=tokenizer.tokenize(code_2)
        code2_tokens=code2_tokens[:BLOCK_SIZE-2]
        code2_tokens =[tokenizer.cls_token]+code2_tokens+[tokenizer.sep_token]
        code2_ids=tokenizer.convert_tokens_to_ids(code2_tokens)
        padding_length = BLOCK_SIZE - len(code2_ids)
        code2_ids+=[tokenizer.pad_token_id]*padding_length

        source_tokens=code1_tokens+code2_tokens
        source_ids=code1_ids+code2_ids
        return torch.tensor(source_ids).to(device)

    remove_comments = False
    predictions = []
    code_1, code_2 = pairs[0]

    iput_ids = convert_examples_to_features(code_1, code_2)
    prediction = model(iput_ids)
    print(prediction)
    prediction_float = prediction[0].tolist()
    prediction = int(torch.argmax(prediction[0]))
    predictions.append(prediction)

    print("prediction = "+ str(prediction))

    return prediction, prediction_float

# print("calling :")
# myfunc()