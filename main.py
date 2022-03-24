import csv
from nltk.tokenize import TreebankWordTokenizer
from nltk.probability import FreqDist
from collections import Counter
tokenizer = TreebankWordTokenizer()

txtfile = open('expat.txt','r', encoding='utf-8')

empty =[]

for line in txtfile:

    empty.extend(tokenizer.tokenize((line)))
    #empty.append(tokenizer.tokenize((line)))

txtfile.close()

#fdist= FreqDist(word.most_common(30) for word in empty )

counter = Counter(empty)
most = counter.most_common(1500)

k= open('expattoken.csv', 'w', encoding= 'utf-8', newline= '')
csvWrite = csv.writer(k)
csvWrite.writerow(most)
print(most)