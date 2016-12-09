# Functions to develop:
import sys
from collections import Counter
from random import randint
from stopwords import STOPWORDS
import os
import csv
import re

TESTING_FILE = "test_file.txt"
TRAINING_FILE = "training_file.txt"
K_FOLD_FACTOR = 3
SMOOTHING_FACTOR = 1
SEPARATOR = ","
CLASS_HRC = "HillaryClinton"
CLASS_DJT = "realDonaldTrump"
HRC_INDEX = 0
DJT_INDEX = 1


def read_data(file_name):
    """ Reads in tweets from csv file """
    # This function will be responsible for reading an input file in csv format.
    corpus = []
    print "Reading file " + file_name
    with open(file_name, 'rb') as csvfile:
        fieldnames = csvfile.readline().strip().split(SEPARATOR)
        for line in csv.DictReader(csvfile, fieldnames):
            corpus.append((line['handle'], line['text']))
    print "Read " + str(len(corpus)) + " tweets"
    return corpus


def cleanup_tweet(tweet):
    """ Cleans up tweet """
    line = re.sub(r'http\S+', '', tweet.strip().lower()).strip()
    words = re.sub("[^a-zA-Z#@]", " ", line).split()
    return filter(lambda x: x not in STOPWORDS and len(x) > 3, words)


def cleanup(corpus):
    """ Cleans up list of handle/tweets """
    # This function will be responsible for cleaning up the input data. This cleanup includes removal of special
    # characters, stop words and performing normalization on the input text data. It will also be responsible for
    # converting the textual data into features. For this exercise we will use Bag Of Words based features.
    testing_set = open(TESTING_FILE, 'w')
    testing_set.write("handle,text\n")
    testing_set_count = 0
    training_list = []
    print "Separating Tweets for Testing, Cleaning Tweets"
    for handle, tweet in corpus:
        valid_words_only = cleanup_tweet(tweet)
        if randint(1, 10) <= K_FOLD_FACTOR:
            testing_set_count += 1
            testing_set.write(handle + SEPARATOR + reduce(lambda x, y: x + " " + y, valid_words_only, "") + "\n")
        else:
            training_list.append((handle, valid_words_only))
    testing_set.close()
    # have priors, word count for each candidate
    print "Sectioned {0} ({1}%) examples for testing".format(str(testing_set_count),
                                                             str(int(100.0 * testing_set_count / len(corpus))))
    return training_list


def train(training_list):
    """ Trains NB classifer. Returns 2 tuples, one for use in evaluation and one for scikit """
    # This function will compute the following probabilities:
    # p(class1), p(class2) ... p(classn): This represents the distribution of each class in your dataset, and the
    # probability of seeing the data from each class.
    # p(feature1|class1): Given class1, what is the probability of seeing feature1 in this class? It is important to
    # identify what you consider as a feature. Is your feature a single word, bigrams (2 words), or trigrams (3words)?
    # For this project it is acceptable to consider unigram features (each feature is one word)
    # p(feature1), p(feature2)...p(featuren): The individual probability of each feature.

    # Note: Please make sure that you use numpy arrays to store your feature probability values. Also make sure that
    # your representations are consistent with the input values required by Scikit-learn's Naive Bayes Implementation
    print "Computing Class priors, Feature Priors, and Feature/Class Likelihood"
    per_class_priors = Counter()
    per_feature_priors = Counter()
    likelihood = {CLASS_HRC: Counter(), CLASS_DJT: Counter()}
    for handle, tweet in training_list:
        per_class_priors.update([handle])
        tweet_counter = Counter(tweet)
        per_feature_priors.update(tweet_counter)
        likelihood[handle].update(tweet_counter)
    target, feature_matrix = zip(*training_list)
    # Return (Class Probabilities dict(class, prob) | Feature Probabilities dict(feature, prob) |
    # Likelihood dict(class, dict (word, prob))
    # (list of list of tweets | List of Classes)
    return (prob_dict(per_class_priors), prob_dict(per_feature_priors),
            {k: prob_dict(likelihood[k]) for k in likelihood}), (
           map(lambda x: ' '.join(x), list(feature_matrix)), target)


def prob_dict(input_counter):
    """ Returns dictionary of element probabilities """
    total = sum(input_counter.values(), 0.0)
    return {k: v / total for k, v in input_counter.iteritems()}


def compute_likelihoods(words, feature_likelihood):
    """ Compute P(Class | Features) for list of Features """
    result = 1
    for word in words:
        if word in feature_likelihood:
            result *= feature_likelihood[word]
        else:
            result *= 1.0 / len(feature_likelihood)
    return result


def compute_recall_precision(y_true, y_pred, classifier):
    """ Compute recall or precision. Inputing y_true y_pred yields recall
     Swapping the two yields precision"""
    count = 0.0
    right = 0.0
    for index, i in enumerate(y_true):
        if i == classifier:
            count += 1
            if y_pred[index] == classifier:
                right += 1
    return right / count


def compute_f1_score(recall, precision):
    """ Computes F1 score """
    return 2 * precision * recall / (precision + recall)


def evaluation(y_true, y_pred):
    """ Prints out classification report for given true and predicted classifications """
    print "Starting Evaluation"
    for classifier in (CLASS_HRC, CLASS_DJT):
        recall = compute_recall_precision(y_true, y_pred, classifier)
        precision = compute_recall_precision(y_pred, y_true, classifier)
        f1_score = compute_f1_score(recall, precision)
        print classifier + ":  Recall: {0}  Precision {1}  F1 Score {2}".format(recall, precision, f1_score)


def predict(tweet_str, classifier_priors, all_feature_priors, feature_probabilities):
    """ Returns list of likely classes in descending order"""
    # This function will compute the overall accuracy and the per class accuracy of your classifier. We require the
    # following metrics for accuracy computation:
    # print "Beginning Evaluation"
    words = cleanup_tweet(tweet_str)
    classification = []
    for classifier in classifier_priors:
        prob = classifier_priors[classifier] * compute_likelihoods(words, feature_probabilities[
            classifier]) / compute_likelihoods(words, all_feature_priors)
        classification.append((prob, classifier))
    return sorted(classification, reverse=True)


def test_naive_bayes(probability_components):
    """ Runs testing of NB Classifier on test data"""
    print "Beginning Testing"
    y_true = []
    y_pred = []
    class_priors, feature_priors, feature_likelihoods = probability_components
    for handle, tweet in read_data(TESTING_FILE):
        y_true.append(handle)
        predictions = predict(tweet, class_priors, feature_priors, feature_likelihoods)
        y_pred.append(predictions[0][1])
    return y_true, y_pred


if __name__ == '__main__':

    # comment out the following and uncomment out the last line if the tweet csv is
    # in this directory or for easy of execution
    if len(sys.argv) != 2:
        print 'Usage: python classifier.py tweet.csv'
        sys.exit(1)
    tweet_csv = sys.argv[1]
    # tweet_csv = "tweets.csv"

    assert os.path.isfile(tweet_csv)
    # for_predict: dict(class, prob) | dict(word,prob) | dict(class, dict(word, prob)
    # This variable is for the predict function
    # for_scikit: [[tweet words seperated by spaces]] | list[handles]
    # This variable is for the scikit naive bayes
    for_predict, for_scikit = train(cleanup(read_data(tweet_csv)))
    print "Training Complete"
    accuracy, testing_handles = test_naive_bayes(for_predict)
    evaluation(accuracy, testing_handles)
