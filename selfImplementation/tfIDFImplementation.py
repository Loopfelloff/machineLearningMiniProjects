import pandas as pd
import numpy as np
import tfIDFClass

def main():
    corpus = [
    "Thor eating pizza, Loki is eating pizza, Ironman ate pizza already",
    "Apple is announcing new iphone tomorrow",
    "Tesla is announcing new model-3 tomorrow",
    "Google is announcing new pixel-6 tomorrow",
    "Microsoft is announcing new surface tomorrow",
    "Amazon is announcing new eco-dot tomorrow",
    "I am eating biryani and you are eating grapes"
            ]
    v = tfIDFClass.TfidfVectorizer()
    v.fit(corpus)
    print(v.get_feature_names_out())
    print(v.idf_)


if __name__ == '__main__':
    main()

