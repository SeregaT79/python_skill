from pprint import pprint
from collections import Counter
import pandas as pd

file = '/home/zerg/Документы/PythonSkillbox/hw/lesson_009/events.txt'

with open(file, 'r', encoding='utf-8') as f:
    big_list = []
    for line in f.readlines():
        big_list.append(line.strip().replace('[', '').split(']'))


df = pd.DataFrame(big_list)

for line in df[0]:
    df[0].replace(line, line[:-10], inplace=True)

print(pd.pivot_table(df, values=1, index=0, aggfunc='sum'))



