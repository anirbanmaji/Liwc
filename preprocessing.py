import nltk
from nltk.tokenize import sent_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import *
from nltk.stem.porter import *
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

#file read
with open("E:\pythonWorkplace\LIWC\Output.txt") as fin:
    text=fin.read()

#tokenizing
#text="text that you want to tokenize."
token=' '.join([word for word in text.split() if word not in stopwords.words("english")])
tokenizer = RegexpTokenizer(r'\w+')
tokenized=tokenizer.tokenize(token)
#print(tokenized)

#root word
stemmer = PorterStemmer()
final=[]
for word in tokenized: # iterate over word_list
    final.append(stemmer.stem(word))
print(final)

text_file = open("Dataset.txt", "w+")
text_file.writelines(["%s\n" % item  for item in final])
text_file.close()

