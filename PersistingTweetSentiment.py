import tweepy
from tweepy import OAuthHandler
import timeimport pandas as pd
from textblob import TextBlob
import datetime
import mysql.connector
def insertInTable(p_date,p_author, p_text, p_translate, p_sentiment,p_sensation):
    try:
        connection = mysql.connector.connect(host='localhost',
                             database='database_name',
                             user='user',
                             password='password')
        cursor = connection.cursor(prepared=True)
        sql_insert_query = '''INSERT INTO `tweets`.`tweets_table`(`Date`,`Author`, `Text`, `Translate`, `Sentiment`, `Sensation`)VALUES(%s,%s,%s,%s,%s,%s)'''

        insert_tuple = (p_date,p_author, p_text, p_translate, p_sentiment,p_sensation)
        result = cursor.execute(sql_insert_query, insert_tuple)
        connection.commit()
        print ("Record inserted successfully into tweets_table table")
    except mysql.connector.Error as error :
        connection.rollback()
        print("Failed to insert into MySQL table {}".format(error))
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

for tweet in tweepy.Cursor(api.search,
                           q="word",
                           rpp=100,
                           tweet_mode='extended',
                           result_type="recent",
                           include_entities=True,
                           lang="pt-br").items(1000):
    if not tweet.retweeted and ('RT @' not in tweet.full_text):
        data = tweet.created_at
        autor = tweet.author.screen_name
        text = tweet.full_text
        phrase = TextBlob(texto)
        translate = TextBlob(str(phrase.translate(to='en')))
        sentiment = traducao.sentiment
        if sentiment.polarity < 0.0:
            sentiment2 = 'Negative'
        elif sentiment.polarity == 0.0:
            sentiment2 = 'Neutral'
        else:
            sentiment2 = 'Positive'
        time.sleep(10)
        print(author + "-" + text + "-" + str(sentiment) + "-" + str(sentiment2))
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        insertInTable(now, author, text, str(translate), str(sentiment), sentiment2)
