# pycsm
python Chinese sentence match

# usege

```py
>>>from csm import SentenceMatch

>>>sm = SentenceMatch()
>>>sent1 = u'中文句子相似度计算'
>>>sent2 = u'汉语句子相似度计算'
>>>print('match result:' + str(sm.match(sent1, sent2)))
match result:(True, 0.7777777777777778)
```

