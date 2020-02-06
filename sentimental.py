#import all the neccessory libraries
import nltk
from textblob import TextBlob
from newspaper import Article

#Get the url of the website
url=input("Enter or paste the url of the website")
#getting the article from the url by using the newspaper funcltion
article=Article(url)

#By using nltk library
article.download() #downloading the article from the url
article.parse()
nltk.download('punkt') #Punkt is a sentence tokenizer.It converts the texts into the list of sentences using the unsupervised algorithm.
article.nlp()


#For getting the summary of the Article
text=article.summary

#using textblob machine learning function we can process the texts

obj=TextBlob(text)

#Now will get the sentiment of the text

sentiment=obj.sentiment.polarity

#using if or else statements
if sentiment==0:
    print("The text is neutral")
elif sentiment>0:
    print("The text is positive")
else:
    print("The text is negative")
