#用于纠正译名时的检索，定位错误的译名，提取到daixiuzheng.json文件中，修改后进行合并。
import json

print('输入1:查找')
print('输入2:合并')
a=input()

if a=='1':
    f=open('AngelWish预翻译文件_processed.json','r',encoding='utf8')
    f=json.load(f)

    out=open('daixiuzheng.json','w',encoding='utf8')
    daixiuzheng={}

    for text in f:
        if 'メルヴェイユ家' in text:#带修正的词
            if 'メルヴェイユ家' not in f[text]['userTrans']:#提取出译文中不包含指定翻译的
                daixiuzheng[text]=f[text]['userTrans']
    json.dump(daixiuzheng,out,ensure_ascii=False, indent=4)

if a=='2':
    with open('AngelWish预翻译文件_processed.json','r',encoding='utf8') as yuanwen: 
        yuanwen=json.load(yuanwen)
        with open('.\\backup\\backup.json','w',encoding='utf8') as back:#备份
            json.dump(yuanwen,back,ensure_ascii=False, indent=4)

    with open('daixiuzheng.json','r',encoding='utf8') as changed:
        changed=json.load(changed)
        for text in changed:
            yuanwen[text]['userTrans']=changed[text]
    
    with open('AngelWish预翻译文件_processed.json','w',encoding='utf8') as out: 
        json.dump(yuanwen,out,ensure_ascii=False, indent=4)
                
