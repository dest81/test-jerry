import re


def text_to_word(text):
    # returns array of words
    # [ word1, word2, .., word2]
    abbr = ["Dr\." , "Prof\." , "Mr\." , "Mrs\." , "Ms\." , "i\.e\." , "etc\."]
    words = re.compile("(%s|[\w]+'?\w?)" % '|'.join(abbr)).findall(text)
    return [word.lower() for word in words]


def text_to_sentences(text):
    # returns array of words groupped by sentences
    # [[ word1, word2, .., word2], [ word1, word2, .., word2], ...]
    sentences = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', text)
    return [text_to_word(sentence) for sentence in sentences]


class Word(object):

    def __init__(self, text=None):
        words = text_to_word(text)
        self.words = words
        self.sentences = text_to_sentences(text)

    def unique_words(self, words):
        words = list(set(words))
        words.sort()
        return words

    def occurrence_in_text(self, word, sentences):
        return len([word for item in self.words if item == word])

    def occurrence_in_sentence(self, word, sentence):
        return len([word for item in sentence if item == word])

    def occurrence(self, word, sentences):
        total = self.occurrence_in_text(word, sentences)
        if not total:
            return
        detail = []
        i = 1
        for sentence in sentences:
            occurrence = self.occurrence_in_sentence(word, sentence)
            if occurrence > 0:
                detail.extend([str(i)] * occurrence)
            i += 1
        return '{%s:%s}' % (total, ','.join(detail))

    def calculate(self, words, sentences):
        result = []
        for word in self.unique_words(words):
            stat = self.occurrence(word, sentences)
            if stat:
                result.append({
                    'word': word,
                    'stat': stat
                })
        return result

    def result(self):
        return self.calculate(self.words, self.sentences)
