# pycsm
python Chinese sentence match

#usege

```py
from csm import SentenceMatch

sm = SentenceMatch()
sent1 = '中文句子相似度计算'
sent2 = '计算中文句子相似度'

sm.match(sent1, sent2)
```

