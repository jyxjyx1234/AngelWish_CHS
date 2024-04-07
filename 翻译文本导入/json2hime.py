import codecs
import re
import json
import os
from hanzidict import hanzidict

def teshuzifutihuan(text):#匹配时去除特殊字符
    return text.replace("♪", "").replace("・", "").replace("〜", "").replace("～", "").replace("?", "").replace(" ", "").replace('\u3000','').replace('\t','')

def hanzitihuan(text):#按照字典替换不支持的汉字
    replaced_string=''
    for char in text:
        replaced_string += hanzidict.get(char, char)
    return replaced_string

transpath='AngelWish预翻译文件_processed.json'
with open(transpath,'r',encoding='utf-8') as f:
    replacement_dict=json.load(f)

replacement_dict = {teshuzifutihuan(key): value for key, value in replacement_dict.items()}

with codecs.open('.\原文件\hime.txt', 'r', encoding='shiftjis') as input_file:
    with codecs.open(".\\fvp-utf8\\hime_transed.txt", 'w', encoding='utf8') as hime:
        with codecs.open(".\\fvp-utf8\\hime_strings_transed.txt", 'w', encoding='utf8') as himestrings:
            for line in input_file:
                if line.startswith("\tpushstring "):
                    content = line.strip()[11:]
                    content1 = teshuzifutihuan(content)
                    sline=content
                    if content1 in replacement_dict:
                        if len(content1)>0:
                            if not re.match(r'[A-Za-z]', content1[0]):
                                line = line.replace(content, replacement_dict[content1]["userTrans"])
                                sline= replacement_dict[content1]["userTrans"]
                    himestrings.write(hanzitihuan(sline)+'\n')
                hime.write(hanzitihuan(line))


