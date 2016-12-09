from classifier import train, read_data, cleanup, cleanup_tweet, TESTING_FILE, CLASS_HRC, CLASS_DJT
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
import sys
import os

if __name__ == '__main__':

    # comment out the following and uncomment out the last line if the tweet csv is
    # in this directory or for easy of execution
    if len(sys.argv) != 2:
        print 'Usage: python classifier.py tweet.csv'
        sys.exit(1)
    tweet_csv = sys.argv[1]
    # tweet_csv = "tweets.csv"

    assert os.path.isfile(tweet_csv)
    # for_scikit: [[tweet words seperated by spaces]] | list[handles]
    # This variable is for the scikit naive bayes
    discard, for_scikit = train(cleanup(read_data(tweet_csv)))
    print "Training Complete"
    training_data, target = for_scikit
    text_clf = Pipeline([('vect', CountVectorizer()), ('clf', MultinomialNB())])
    text_clf = text_clf.fit(training_data, target)
    print "Beginning Testing"
    y_true = []
    testing_list = []
    for handle, tweet in read_data(TESTING_FILE):
        y_true.append(handle)
        testing_list.append(' '.join(cleanup_tweet(tweet)))
    y_pred = text_clf.predict(testing_list)
    print classification_report(y_true, y_pred, target_names=[CLASS_HRC, CLASS_DJT])
