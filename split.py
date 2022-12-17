from clean import *
import nltk
from nltk.corpus import stopwords
import polarity

nltk.download('stopwords')
input=open("tweets.txt","r", encoding='UTF-8')
output=open("processed.txt","a", encoding='UTF-8')
polarr=open("polarity.txt","a", encoding='UTF-8')

all_stopwords = stopwords.words('english')

count = {}
count["neg"] = 0
count["neut"] = 0
count["pos"] = 0
a=[]

gate=True
for line in input:
    line=(line.lower()).split()
    for word in line:
        if word=="rt":
            if gate:
                gate=False
                continue
            #disini
            f = str(polarity.polar(a,count)) + "\n"
            polarr.write(f)
            output.write(str(a)+"\n")
            a=[]
            continue
        if cleanWord(word):
            if cleanWord(word) in all_stopwords:
                continue
            a.append(cleanWord(word))

sum = count["neg"] + count["neut"] + count["pos"]
print("persen neg")
print(count["neg"]/sum*100)
print("persen pos")
print(count["pos"]/sum*100)
print("persen neut")
print(count["neut"]/sum*100)
print("Total tweets")
print(count)