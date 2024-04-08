import re
from collections import OrderedDict
import nltk
# nltk.download('words')

class Workers:

    def remove_sign_en(self, txt_list:list):
        no_sign = [re.sub(r'[^a-zA-Z\d\s:]','',i) for i in txt_list]
        return no_sign
    
    def remove_num_en(self, txt_list:list):
        no_num = [re.sub(r'[^a-zA-Z\s]','',j) for j in txt_list]
        return no_num
    
    def remove_multi_spaces(self, txt_list:list):
        singlespace = [re.sub(' +', ' ', t) for t in txt_list ]
        return singlespace
    
    def remove_duplicated_words_preserve_order(self, txt_list:list):
        no_dupl_list = []
        for eachstr in txt_list:
            unique_words = list(OrderedDict.fromkeys(eachstr.split())) #ATTENTION!: you can use set instead of  
                            #OrderedDict but it won't preserve the order of words.
            no_dupl_list.append(' '.join(unique_words))

        return no_dupl_list
    
    def remove_meanningless(self, txt_list):
        words = set(nltk.corpus.words.words())
        meaningfull_lst = []
        for mystr in txt_list:
            all_meaningfull_sentence = " ".join(w for w in nltk.wordpunct_tokenize(mystr)
                    if w.lower() in words or not w.isalpha())   # removing non alphabetic charcters also

            meaningfull_lst.append(all_meaningfull_sentence)

        return meaningfull_lst
    
    def remove_char_single(self, txt_lst):
        no_char = []

        for string_ in txt_lst:
            word_lst = string_.split()
            multichar_lst = [eachword for eachword in word_lst if len(eachword)!= 1]
            no_char.append(' '.join(multichar_lst))

        return no_char
