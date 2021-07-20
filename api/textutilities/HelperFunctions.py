from nltk.tokenize import WordPunctTokenizer
from nltk.stem.wordnet import WordNetLemmatizer

import textutilities.CleaningFunctions as c
import textutilities.FilterFunctions as f


def make_wordbank(list_of_texts):
    wordbank = []
    for text in list_of_texts:
        clean = cleaner(text)
        print("text cleaned")
        no_extra_words = f.unified_word_filter(clean)
        print("removed useless words")
        lemmatized = lemmatizer(no_extra_words)
        print("lemmatized")
        wordbank.extend(lemmatized)
    return wordbank


def cleaner(raw_text):
    # noBrackets = c.remove_directions_brackets(rawText)
    # noDirections = c.remove_directions_space(noBrackets)
    noTags = c.remove_html_tags(raw_text)
    #noNames = c.remove_abrv_names(noDirections)
    tokenized = WordPunctTokenizer().tokenize(noTags)
    #noCaps = c.remove_all_caps(tokenized)
    #cleanList = c.remove_punctandnums(noCaps)
    return tokenized


def lemmatizer(List):
    lemList = []
    for word in List:
        lemList.append(WordNetLemmatizer().lemmatize(word))
    return lemList
