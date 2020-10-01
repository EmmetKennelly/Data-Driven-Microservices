# -*- coding: utf-8 -*-
"""
Created on Mar  2 12:29:50 2020

@author: Emmet
"""
import re


from textblob import TextBlob
import random 
import time
import grpc


def run():
    while True:
        with grpc.insecure_channel('greeter_server:5001') as channel:
            stub = (channel)
            messageLength = 0
            for response in stub.getTweets:
                messageLength += len(response.message)       
                time.sleep(random.randint(1,3))
                return clean_tweet(response.message) 

def clean_tweet(tweets):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])| (\w+:\/\/\S+)", " ", tweets).split())

 
def countWords(data):
   
    count = (data).str.len()
   
    return count

 
def get_tweet_sentiment(self, tweet):   
        tweet_dict = (tweet)
        sentiments = TextBlob(self.clean_tweet(tweet))
        score = round(sentiments.sentiment.subjectivity, 2)
        
        if score > 0:
            return tweet_dict["score"].append('positive')
        elif sentiments.sentiment.polarity == 0:
            return tweet_dict["score"].append('neutral')
        else:
            return tweet_dict["score"].append('neagtive')
 

def countOccurences(data,minWordLength, minWordOccurence):
 clean_tweet(data)
 data = data[clean_tweet == True]
 wordOccurences = {}
 wordList = []

 allWords = (clean_tweet).str.split()
 
 for tweets in allWords:
  for word in tweets:
   if (len(word)>=minWordLength):
    wordOccurences[word] = wordOccurences[word] + 1
               
   else:
    wordOccurences[word]=1    
 
   for word in wordOccurences:
      if wordOccurences[word]>=minWordOccurence:
       print( "The word : "+ word + "  appeared : " + str(wordOccurences[word])+" times" )
       wordList.append(word)
         
         
   
  
   return wordList



#def main():
    
    #run()
    #countWords(run())
    #get_tweet_sentiment( run() )
    #countOccurences(run(), 4, 100)
    
    

 #if __name__ == '__main__':
 #main()
 
