# Functions to develop:
import sys
import numpy as np
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


# class LearningClass:
#     def __init__(self, tweet_class, prior, word_count, dictionary):
#         self.tweet_class = tweet_class
#         self.prior = prior
#         self.word_count = word_count
#         self.dict = dictionary


def read_data(file_name):
    # This function will be responsible for reading an input file in csv format.
    corpus = []
    print "Reading file " + file_name
    with open(file_name, 'rb') as csvfile:
        fieldnames = csvfile.readline().strip().split(SEPARATOR)
        for line in csv.DictReader(csvfile, fieldnames):
            corpus.append((line['handle'], line['text']))
    print "Read " + str(len(corpus)) + " tweets"
    return cleanup(corpus)


def compute_tf(examples):
    tf_data = []
    word_doc_count = {}
    for tweet in examples:
        features = tweet.split(",")
        term_freq_per_tweet = {}
        # Counts the words in a tweet
        for term in features:
            if term in term_freq_per_tweet:
                term_freq_per_tweet[term] += 1
            else:
                term_freq_per_tweet[term] = 1
        # Counts the # of documents a word is in. Also normalizes the word counts
        for x in term_freq_per_tweet:
            if x in word_doc_count:
                word_doc_count[x] += 1
            else:
                word_doc_count[x] = 1
            term_freq_per_tweet[x] = 1 + np.math.log(term_freq_per_tweet[x])
        tf_data.append(term_freq_per_tweet)
    tf_data = reduce(merge_word_counts, tf_data, {})
    return tf_data, word_doc_count


def merge_word_counts(t1, t2):
    for x in t1:
        if x in t2:
            t1[x] = t1[x] + t2[x]
    for y in t2:
        if y not in t1:
            t1[y] = t2[y]
    return t1


def idf(target_dict, corpus_size, merged_counts):
    for x in target_dict:
        target_dict[x] *= np.math.log(1 + corpus_size / merged_counts[x])
    return target_dict


def normalize_training_data(hrc_examples, djt_examples):
    print "Normalizing data"
    corpus_size = len(hrc_examples) + len(djt_examples)
    print "Computing TF"
    hrc_dict, word_doc_count = compute_tf(hrc_examples)
    djt_dict, word_doc_count2 = compute_tf(djt_examples)
    merged_counts = merge_word_counts(word_doc_count, word_doc_count2)
    print "Computing IDF"
    return (CLASS_HRC, idf(hrc_dict, corpus_size, merged_counts)), \
           (CLASS_DJT, idf(djt_dict, corpus_size, merged_counts))


def cleanup(corpus):
    # This function will be responsible for cleaning up the input data. This cleanup includes removal of special
    # characters, stop words and performing normalization on the input text data. It will also be responsible for
    # converting the textual data into features. For this exercise we will use Bag Of Words based features.
    # training_set = open(TRAINING_FILE, 'w')
    hrc_examples = []
    djt_examples = []
    testing_set = open(TESTING_FILE, 'w')
    count = 0
    print "Separating Tweets by Class"
    for handle, tweet in corpus:
        words = [j for i in map(lambda x: re.sub("[^a-zA-Z]", " ", x).strip().split(), tweet.strip().lower().split())
                 for j in i]
        valid_words_only = filter(lambda x: len(x) > 3, filter(lambda x: x not in STOPWORDS, words))
        if randint(1, 10) <= K_FOLD_FACTOR:
            count += 1
            testing_set.write(handle + SEPARATOR + reduce(lambda x, y: x + SEPARATOR + y, valid_words_only) + "\n")
        else:
            # training_set.write(handle + SEPARATOR + reduce(lambda x, y: x + SEPARATOR + y, valid_words_only))
            if handle == CLASS_HRC:
                hrc_examples.append(reduce(lambda x, y: x + SEPARATOR + y, valid_words_only))
            elif handle == CLASS_DJT:
                djt_examples.append(reduce(lambda x, y: x + SEPARATOR + y, valid_words_only))
    testing_set.close()
    print "Sectioned {0} ({1}%) examples for testing".format(str(count), str(int(100.0 * count / len(corpus))))
    for handle, training_class in normalize_training_data(hrc_examples, djt_examples):
        training_writer = open("train_" + handle + ".txt", 'w')
        for item in training_class:
            training_writer.write(item + " " + str(training_class[item]) + "\n")
        training_writer.close()
        print "Wrote " + str(len(training_class)) + " words to " + "train_" + handle + ".txt"


def train():
    # This function will compute the following probabilities:
    # p(class1), p(class2) ... p(classn): This represents the distribution of each class in your dataset, and the
    # probability of seeing the data from each class.
    # p(feature1|class1): Given class1, what is the probability of seeing feature1 in this class? It is important to
    # identify what you consider as a feature. Is your feature a single word, bigrams (2 words), or trigrams (3words)?
    # For this project it is acceptable to consider unigram features (each feature is one word)
    # p(feature1), p(feature2)...p(featuren): The individual probability of each feature.
    # p(feature1|feature2): What is the probability that you would see feature1 given feature2? Do you really need to
    # compute this? Do not compute it if you do not need this value.
    # Note: Please make sure that you use numpy arrays to store your feature probability values. Also make sure that
    # your representations are consistent with the input values required by Scikit-learn's Naive Bayes Implementation
    trainer = np.array()
    pass


def evaluation():
    # This function will compute the overall accuracy and the per class accuracy of your classifier. We require the
    # following metrics for accuracy computation:
    pass


def predict():
    # Given an input string, this function will return the list of classes it might belong to with decreasing
    # probability
    pass


if __name__ == '__main__':
    # if len(sys.argv) != 2:
    #     print 'Usage: python classifier.py tweet.csv'
    #     sys.exit(1)
    #
    # tweet_csv = sys.argv[1]
    tweet_csv = "tweets.csv"
    assert os.path.isfile(tweet_csv)
    try:
        read_data(tweet_csv)

    finally:
        # ready for user input
        pass
