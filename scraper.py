import json
import datetime
import pandas as pd
from twitter import Twitter
from tweet_preprocessor import TWPreprocessor
from indexer import Indexer

reply_collection_knob = False


def read_config():
    with open("config.json") as json_file:
        data = json.load(json_file)

    return data


def write_config(data):
    with open("config.json", 'w') as json_file:
        json.dump(data, json_file)


def save_file(data, filename):
    df = pd.DataFrame(data)
    df.to_pickle("data/" + filename)


def read_file(type, id):
    return pd.read_pickle(f"data/{type}_{id}.pkl")


def main():
    config = read_config()
    indexer = Indexer()
    twitter = Twitter()

    pois = config["pois"]
    keywords = config["keywords"]

    for i in range(len(pois)):
        if pois[i]["finished"] == 0:
            print(f"---------- collecting tweets for poi: {pois[i]['screen_name']}")

            raw_tweets = twitter.get_tweets_by_poi_screen_name(pois[i]["screen_name"],pois[i]["count"])  # pass args as needed

            processed_tweets = []
            for tw in raw_tweets:
                processed_tweets.append(TWPreprocessor.preprocess(tw))

            indexer.create_documents(processed_tweets)

            pois[i]["finished"] = 1
            pois[i]["collected"] = len(processed_tweets)

            write_config({
                "pois": pois, "keywords": keywords
            })

            save_file(processed_tweets, f"poi_{pois[i]['id']}.pkl")
            print("------------ process complete -----------------------------------")

    for i in range(len(keywords)):
        if keywords[i]["finished"] == 0:
            print(f"---------- collecting tweets for keyword: {keywords[i]['name']}")

            raw_tweets = twitter.get_tweets_by_lang_and_keyword(keywords[i]["count"],keyword[i]["name"],keyword[i]["lang"])  # pass args as needed

            processed_tweets = []
            for tw in raw_tweets:
                processed_tweets.append(TWPreprocessor.preprocess(tw))

            indexer.create_documents(processed_tweets)

            keywords[i]["finished"] = 1
            keywords[i]["collected"] = len(processed_tweets)

            write_config({
                "pois": pois, "keywords": keywords
            })

            save_file(processed_tweets, f"keywords_{keywords[i]['id']}.pkl")

            print("------------ process complete -----------------------------------")

    if reply_collection_knob:
        # Write a driver logic for reply collection, use the tweets from the data files for which the replies are to collected.
        for poi in pois:
            print(f" collecting replies for POI : {poi['Screen_name']} ")
            poi_tweets = read_file('poi',poi['id'])

            tweet_5days[]
            for tweet in poi_tweets.to_dict(orient="records"):
                td =datetime.datetime.now() - datetime.datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
                if td.days<5:
                    print(' tweet id is {}. is accepted for replies!'.format(tweet['id_str']))
                    tweets_5days.append(tweet)
                else:
                    pass
            if len(tweets_5days)>0:
                for key, tw in enumerate(tweets_5days):
                    if key ==0 :
                        raw_tweets = twitter.get_replies_by_tweet_id(tw["id_str"], None, poi['screen_name'],1000)
                    else :
                        raw_tweets = twitter.get_replies_by_tweet_id(tw["id_str"], tweets_5days[key-1["id_str"], poi["screen_name"], 1000)

                    processed_tweets= []
                    for tw in raw_tweets:
                        processed_tweets.append(TWPreprocessor.preprocess(tw,country=tw["country"], is_keyword=True))
        raise NotImplementedError



if __name__ == "__main__":
    main()