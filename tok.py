import json,os,re
from collections import Counter
c=Counter();c2=Counter()
for f in os.listdir('data/d'):
    j=json.load(open('data/d/'+f,encoding='utf-8'))['job']
    t=j['detail']['requirements']+'\n'+j['detail']['preferred_points']
    c.update(set(w.lower() for w in re.findall(r'[A-Za-z][A-Za-z0-9+#/\-\.]{1,}',t)))
    c2.update(set(re.findall(r'[가-힣]{2,}',t)))
print(c.most_common(260));print(c2.most_common(200))
