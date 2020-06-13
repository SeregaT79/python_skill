from pprint import pprint
from collections import Counter
import pandas as pd

file = '/home/zerg/Документы/PythonSkillbox/hw/lesson_009/events.txt'

with open(file, 'r', encoding='utf-8') as f:
    big_list = []
    for line in f.readlines():
        big_list.append(line.strip().replace('[', '').split(']'))

def splitMy(s):
    for i in s:
        i.replace(i, i[:-10])
    return s

df = pd.DataFrame(big_list)
# df[0] = splitMy(df[0])

# print(df.head(3))
for i in df[0]:
    df[0].i = df[0].i[:-10]
print(df[0])