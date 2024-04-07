import json
import re

def teshuzifutihuan(text):
    return text.replace("♪", "").replace("・", "").replace("〜", "").replace("～", "").replace("?", "").replace(" ", "").replace('\u3000','').replace('\t','').replace('「','').replace('」','').replace('\n','')

yuanwen=open('.\日文脚本\\all.orig.json','r',encoding='utf8')
yuanwen=json.load(yuanwen)

transpath='AngelWish预翻译文件_processed.json'
with open(transpath,'r',encoding='utf-8') as f:
    replacement_dict=json.load(f)
replacement_dict = {teshuzifutihuan(key): value for key, value in replacement_dict.items()}

out=[]
for i in yuanwen:
    content=i['message']
    if teshuzifutihuan(content) in replacement_dict:
        if len(content)>0:
            if not re.match(r'[A-Za-z]', content[0]):
                content=replacement_dict[teshuzifutihuan(content)]["userTrans"]
    out.append({'message':content})

with open('.\日文脚本\\all.trans.json','w',encoding='utf8') as f:
    json.dump(out,f,ensure_ascii=False, indent=4)