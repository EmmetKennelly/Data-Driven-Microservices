# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 12:36:40 2020

@author: Emmet
"""
from flask import Flask, render_template
import redis

import datetime
from redis_collections import Dict


app = Flask(__name__, template_folder='templat')
collections = Dict()
redis_host = "localhost"
redis_port = 5001
redis_password = ""

# Main page
@app.route('/')
def hello_world():
   
     return refresh_page()

def refresh_page():
    
    result = list(collections.find({'date':{'$gt':datetime.datetime.utcnow() - datetime.timedelta(minutes=1)}}))
    sumOfSentiment = 0
    count = 0
    for res in result:
        sumOfSentiment = sumOfSentiment + res['sentiment']
        count = count + 1
        
    average = sumOfSentiment/count
    return render_template('home.html', result=average)

def find_average(score):
    return score

def get_reddit(time):
        reddit = []
        client = MongoClient('mongo')
        db = client.testdb
        reddit = list(db.posts.find({"date": {"$gt": datetime.datetime.utcnow() - datetime.timedelta(minutes=time)}}))
        reddit = [for token in reddit if token['over18'] == 'True']
        return reddit 
def main():
    print("Displaying:...")
    try:

        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
        data = r.tweets_db
        tweets = data.tweets_coll
        tweetInfo = tweets.find()

        for each in twtweetInfo:
            if refresh_page(each["time"]):
                noOfTweets.append(each["score"])
        total = 0
    
        for each in noOfTweets:
            total += each
        global score
        score = total / len(noOfTweets)
        score = round(score, 2)
        
         if(len(Flask.get_reddit(1)) > 0):
        reddit = Flask.get_reddit(1)
     
if __name__ == "__main__":
    main()
    app.run(host="0.0.0.0", port=5001, debug=True)
    conn = redis.StrictRedis(host='redis', port=5001)
