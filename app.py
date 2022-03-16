from data_sources.twitter_bot import Twitter
from data_sources.cryptopanic_bot import Cryptopanic
from tools.sentiment_analysis import SentimentAnalyzer

def main():
    twitter = Twitter('Bitcoin')
    cryptopanic = Cryptopanic()
    # cryptopanic.getDataCryptopanic()
    sentimentAnalyzer = SentimentAnalyzer()
    sentimentAnalyzer.analysis(twitter.getTweets())
    sentimentAnalyzer.analysis(cryptopanic.getDataCryptopanic())
    
if __name__ == '__main__':
    main()
    