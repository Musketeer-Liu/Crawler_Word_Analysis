from collections import Counter
from tools.storage import *


class Analytics():


    def __init__(self, data):
        self.data = data
        self.stopwords = file_to_set('keywords.txt')

        self.content = self.get_content()
        self.keyword_count = self.get_keyword_count()


    def get_content(self):
        results = ''
        for item in self.data['tags']:
            if item['content']:
                results += item['content'] + ' '
        return results


    def get_keyword_count(self):
        all_words = self.content.split()
        good_words = []
        for word in all_words:
            word = word.clean_word(word)
            
            if word.strip() in self.stopwords:
                continue
            if len(word) <= 1:
                continue

            good_words.append(word)
        
        word_count = Counter(good_words)
        return self.sort_counter(word_count)

    
    @staticmethod
    def sort_counter(counter):
        results = []
        for item in sorted(counter, key=counter.__getitem__, reverse=True):
            results.append([item, counter[item]])
        return results

    
    @staticmethod
    def clean_word(word):
        word = word.lower()
        for x in list('`~!@#$%^&*()-_=+{}[]<>:;"|,./?'):
            word = word.replace(x, '')