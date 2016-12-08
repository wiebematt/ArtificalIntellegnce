from classifier import train, read_data, cleanup, cleanup_tweet, TESTING_FILE, CLASS_HRC, CLASS_DJT
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import CountVectorizer
import sys
import os

if __name__ == '__main__':
    # if len(sys.argv) != 2:
    #     print 'Usage: python scikit-learn-classifier.py tweet.csv'
    #     sys.exit(1)
    #
    # tweet_csv = sys.argv[1]
    tweet_csv = "tweets.csv"
    assert os.path.isfile(tweet_csv)
    # for_predict: dict(class, prob) | dict(word,prob) | dict(class, dict(word, prob)
    # This variable is for the predict function
    # for_scikit: sparse feature matrix | list[handles]
    # This variable is for the scikit naive bayes
    discard, for_scikit = train(cleanup(read_data(tweet_csv)))
    print "Training Complete"
    training_data, target = for_scikit
    mnb = MultinomialNB()
    print "Fitting Data"
    y_pred = mnb.fit(training_data, target)
    print "Beginning Testing"
    y_true = []
    testing_list = []
    for handle, tweet in read_data(TESTING_FILE):
        y_true.append(handle)
        testing_list.append(' '.join(cleanup_tweet(tweet)))
    vectorizer = CountVectorizer()
    testing_matrix = vectorizer.fit_transform(testing_list)
    y_pred = mnb.predict(testing_matrix)
    classification_report(y_true, y_pred, target_names=[CLASS_HRC, CLASS_DJT])
