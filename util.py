import operator

import pandas as pd
import string


def get_panda(list_data):
    df = pd.DataFrame(list_data)
    df.columns = ['word', 'freq']
    return df


def remove_redundancies(word_list):
    del_list = []
    for w in word_list:
        w_lower = w.strip(string.punctuation).lower()
        if (w_lower in word_list and w in word_list) and w_lower != w and w[0].isupper():
            word_list[w_lower] = word_list[w] + word_list[w_lower]
            del_list.append(w)

    for w in del_list:
        del word_list[w]

    return word_list


def remove_common_words(word_list):
    common_words = {'the', 'is', 'in', 'and', 'of', 'to', 'a', 'that', 'for', 'as', 'was', 'by', 'with', 'on', 'or',
                    'which', 'are', 'their', 'an', 'be', 'but', 'this', 'also', 'it', 'its', 'if', 'from', 'at', 'were',
                    'had', 'has', 'than'}
    for c in common_words:
        if c in word_list:
            del word_list[c]

    return word_list


def get_sorted_dict(paragraphs):
    word_dict = {}

    # The dictionary here will contain duplicates of words that are both uppercase and lowercase.
    # They are removed in the next function call
    for p in paragraphs:
        words = p.get_text().split()
        for w in words:
            w = w.strip(string.punctuation)
            if w in word_dict:
                word_dict[w] = word_dict[w] + 1
            else:
                word_dict[w] = 1

    word_dict = remove_redundancies(word_dict)
    word_dict = remove_common_words(word_dict)

    sorted_dict = sorted(word_dict.items(), key=operator.itemgetter(0))
    sorted_dict.sort(key=operator.itemgetter(1), reverse=True)

    return sorted_dict
