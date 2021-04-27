import tweepy as Tp

class TwitterBot:
    def __init__(self, Consumer_key, Consumer_secret, Access_token, Access_secret):
        self.Consumer_key = Consumer_key
        self.Consumer_secret = Consumer_secret
        self.Access_token = Access_token
        self.Access_secret = Access_secret
        self.Login()
    def Login(self):
        self.auth = Tp.OAuthHandler(self.Consumer_key, self.Consumer_secret)
        self.auth.set_access_token(self.Access_token, self.Access_secret)
        self.API = Tp.API(self.auth)
        print("Twitter Logged In...")
    def Tweet(self, text):
        self.API.update_status(text)
    def Tweet_Media(self, File):
        self.API.update_with_media(File)
