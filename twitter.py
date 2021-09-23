import tweepy


class Twitter:
    def __init__(self):
        self.auth = tweepy.OAuthHandler("zGi89YGHUAk5vcXlHYBuT3hSi", "Ad9oJGB27J5kvmbeMj6eb6R9FSwZsRzW2GzRUfgvciNpn3zpcU")
        self.auth.set_access_token("1432805975669493762-VUWiVFfE28BfiWWFokOVYN2TmZqVEm", "U74I8pDiQjJ5zTQ8AUJgWzgXtGSmVKAvb7GNip4bp7I9C")
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


    def get_tweets_by_poi_screen_name(self,keyword,lang,count):
        '''
        Use user_timeline api to fetch POI related tweets, some postprocessing may be required.
        :return: List
        '''
          _list=[]
        for tweet in tweepy.cursor(self.api.user_timeline,screen_name=poiName).items(count):
            _list.append(tweet)
        return _list
        
        raise NotImplementedError

    def get_tweets_by_lang_and_keyword(self):
        '''
        Use search api to fetch keywords and language related tweets, use tweepy Cursor.
        :return: List
        '''
          _list=[]
        for tweet in tweepy.cursor(self.api.search,keyword,lang).items(count):
            _list.append(tweet)
        return _list
        raise NotImplementedError

    def get_replies(self):
        '''
        Get replies for a particular tweet_id, use max_id and since_id.
        For more info: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/guides/working-with-timelines
        :return: List
        '''
          _list=[]
        for tweet in tweepy.cursor(self.api.search,q='to:'+user,since_id=sinceID timeout=999999).items(maxID):
            if hasattr(tweet,'in_reply_to_status_is_str'):
                if (tweet.in_reply_to_status_is_str==tweet_id):
                    replies.append(tweet)
        return replies
        raise NotImplementedError