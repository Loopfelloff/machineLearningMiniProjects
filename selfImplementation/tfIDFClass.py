# assume the scikit learn formula to calculate the inverse document frequency
import numpy as np
import pandas as pd
import math

class TfidfVectorizer():

    vocabulary_ = {}
    idf_ = None # will be initialized later on to a numpy array # basically for each word in list of get_feature_names_out you would store the correspondign value of IDF i suppose
    corpus = []
    bags_of_words = []
    def __init__(self):
        pass
    def fit(self, corpus): # this calculates the IDF i suppose
        self.corpus = corpus
        bags_of_words = []
        for sentence in self.corpus:
            for word in sentence.split():
                if word not in bags_of_words:
                    bags_of_words.append(word)
        self.bags_of_words = bags_of_words
        self.bags_of_words.sort(key=str.lower)

        self.idf_ = np.zeros((len(bags_of_words)))

        for index,word in enumerate(bags_of_words):
            for sentence in self.corpus:
                if word in sentence.split():
                    self.idf_[index] += 1
            self.idf_[index] = math.log((1+len(corpus))/ (1 + self.idf_[index])) + 1
                    
            
    def transform(self, corpus): # just return an array of some sort the entire TF IDF shit
        pass
    def get_feature_names_out(self):
        # this function contains all the list of all the keywords in ascending order usign in the corpus
        return self.bags_of_words 


