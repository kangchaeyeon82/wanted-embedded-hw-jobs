import json
from collections import Counter
S=json.load(open('out/skills.json',encoding='utf-8'))
for tr in ['임베디드','하드웨어']:
    r=sorted([s for s in S if s['track']==tr],key=lambda s:-s['must'])[:18]
    print(tr,[(s['skill'],s['must'],s['nice_only'],s['must_share']) for s in r])
J=json.load(open('out/jobs.json',encoding='utf-8'))
for tr in ['임베디드','하드웨어']:
    E=[j for j in J if j['track']==tr and j['years_min']<=2]
    c=Counter(k.strip() for j in E for k in j['must'].split(',') if k.strip())
    print(tr,'junior(<=2y)',len(E),c.most_common(15))
E=[j for j in J if j['years_min']==0]
print('newbie',len(E),[ (j['company'],j['position']) for j in E][:31])
