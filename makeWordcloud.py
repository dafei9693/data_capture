from utils import getDatafromSql
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba


data = getDatafromSql()
title = []
for d in data:
    title.append(d[0].replace(" ",''))
with open('prepare.txt','a') as f:
    for d in title:
        f.write(d)
    f.close()

text_from_file_with_apath = open('prepare.txt').read()
wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)

my_wordcloud = WordCloud(font_path="C:\Windows\Fonts\simfang.ttf").generate(wl_space_split)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()