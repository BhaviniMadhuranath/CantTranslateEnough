import nltk
nltk.download('udhr') # udhr = Universal Declaration of Human Rights
from nltk.corpus import udhr

text = "This is a test text"
n = 3 # 1 = Unigram, 2 = bigram, 3 = trigram
text_len = len(text)
num_ngrams = text_len - n + 1 # How many ngrams of length n will fit in this text
#print(f"The text is {text_len} characters long and will fit {num_ngrams} n-grams of length {n}.")

#for p in range(num_ngrams) :
#            print(f"{p}: {text[p:p+n]}")

import typing

def extract_xgrams(text: str, n_vals: typing.List[int]) -> typing.List[str]:
    """
    Extract a list of n-grams of different sizes from a text.
    Params:
        text: the test from which to extract ngrams
        n_vals: the sizes of n-grams to extract
        (e.g. [1, 2, 3] will produce uni-, bi- and tri-grams)
    """
    xgrams = []
    
    for n in n_vals:
        # if n > len(text) then no ngrams will fit, and we would return an empty list
        if n < len(text):
            for i in range(len(text) - n + 1) :
                ng = text[i:i+n]
                xgrams.append(ng)
        
    return xgrams

text = "I was taught that the way of progress was neither swift nor easy.".lower()
# Quote from Marie Curie, the first woman to win a Nobel Prize, the only woman to win it twice, and the only human to win it in two different sciences.

# Extract all ngrams of size 1 to 3.
xgrams = extract_xgrams(text, n_vals=range(1,4))

print(xgrams)


import re
def removePunc(text):
    punc = '''!()[]{};:"\,<>./?@#$%^&*_~'''
    i=0
    length=len(text)
    while(i<length):
        if text[i] in punc:
            text=text.replace(text[i],"")
            length=len(text)
            
        elif text[i] == "-":
            text=text.replace(text[i]," - ")
            length=len(text)
            i=i+2
        elif text[i]=="'":
            if(text[i-1]==" "):
                text=text.replace(text[i],"' ")
                length=len(text)
                i=i+1
            elif(text[i+1]==" "):
                text=text.replace(text[i]," '")
                length=len(text)
                i=i+1
            else:
                text=text.replace(text[i]," ' ")
                length=len(text)
                i=i+2
        i=i+1
    #print("removed punc")
    return text
text1 = removePunc("ever-lasting 'till it dies.")



def formatSentence(text):
    # text=[removePunc(x) for x in text]
    text=removePunc(text)
    text1=[x for x in text]
    #newList = ["<s>"]
    text1.insert(0,"<s>")
    # for i in text:
    #     newList.append(i)
    text1.append("</s>")
    return text


import typing

def extract_wordgrams(text: str, n_vals: typing.List[int]) -> typing.List[str]:
    """
    Extract a list of n-grams of different sizes from a text.
    Params:
        text: the test from which to extract ngrams
        n_vals: the sizes of n-grams to extract
        (e.g. [1, 2, 3] will produce uni-, bi- and tri-grams)
    """
    text = formatSentence(text)
    list1=text.split(' ')
    #print(list1)
    xgrams = []
    for n in n_vals:
        # if n > len(text) then no ngrams will fit, and we would return an empty list
        if n < len(list1):
            for i in range(len(list1) - n + 1) :
                ng = list1[i:i+n]
                str1= ""
                for l in range(0,n): 
                    if(str1==""):
                        str1=str1+ng[l]
                    else:
                        str1 = str1 + " " + ng[l]
                xgrams.append(str1)
            
                

    #print("extracted word grams")
    return xgrams

text = "ever-lasting 'till it dies.".lower()
# Quote from Marie Curie, the first woman to win a Nobel Prize, the only woman to win it twice, and the only human to win it in two different sciences.

# Extract all ngrams of size 1 to 3.
xgrams = extract_wordgrams(text, n_vals=range(1,4))

#print(xgrams)



import collections


def build_model(text: str, n_vals: typing.List[int]) -> typing.Dict[str, int]:
    """
    Build a simple model of probabilities of xgrams of various lengths in a text
    Parms:
        text: the text from which to extract the n_grams
        n_vals: a list of n_gram sizes to extract
    Returns:
        A dictionary of ngrams and their probabilities given the input text
    """
    model = collections.Counter(extract_xgrams(text, n_vals))  
    num_ngrams = sum(model.values())

    for ng in model:
        model[ng] = model[ng] / num_ngrams

    return model

test_model = build_model(text, n_vals=range(1,4))
#print({k: v for k, v in sorted(test_model.items(), key=lambda item: item[1], reverse=True)})



import collections


def build_modelwords(text: str, n_vals: typing.List[int]) -> typing.Dict[str, int]:
    """
    Build a simple model of probabilities of xgrams of various lengths in a text
    Parms:
        text: the text from which to extract the n_grams
        n_vals: a list of n_gram sizes to extract
    Returns:
        A dictionary of ngrams and their probabilities given the input text
    """
    model = collections.Counter(extract_wordgrams(text, n_vals))  
    num_ngrams = sum(model.values())

    for ng in model:
        model[ng] = model[ng] / num_ngrams
    print("done")

    return model

test_model_words = build_modelwords(text, n_vals=range(1,4))
#print({k: v for k, v in sorted(test_model_words.items(), key=lambda item: item[1], reverse=True)})




languages = ['english', 'german', 'french', 'italian', 'spanish']
language_ids = ['English-Latin1', 'German_Deutsch-Latin1', 'French_Francais-Latin1', 'Italian_Italiano-Latin1', 'Spanish_Espanol-Latin1']# I chose the above sample of languages as they all use similar characters. 

### Optional: If you want to add more languages:

# First use this function to find the language file id
def retrieve_fileid_by_first_letter(fileids, letter):
    return [id for id in fileids if id.lower().startswith(letter.lower())]

# Example usage
#print(f"Fileids beginning with 'R': {retrieve_fileid_by_first_letter(udhr.fileids(), letter='R')}")

# Then copy-paste the language name and language id into the relevant list:
languages += []
language_ids += []




raw_texts = {language: udhr.raw(language_id) for language, language_id in zip(languages, language_ids)}
#print(raw_texts['english'][:1000]) # Just print the first 1000 characters

# Build a model of each language
models = {language: build_model(text=raw_texts[language], n_vals=range(1,4)) for language in languages}
#print(models['german'])
#print("done")
modelswords = {language: build_modelwords(text=raw_texts[language], n_vals=range(1,4)) for language in languages}
#print(models['german'])




import math

def calculate_cosine(a: typing.Dict[str, float], b: typing.Dict[str, float]) -> float:
    """
    Calculate the cosine between two numeric vectors
    Params:
        a, b: two dictionaries containing items and their corresponding numeric values
        (e.g. ngrams and their corresponding probabilities)
    """
    numerator = sum([a[k]*b[k] for k in a if k in b])
    denominator = (math.sqrt(sum([a[k]**2 for k in a])) * math.sqrt(sum([b[k]**2 for k in b])))
    return numerator / denominator



def identify_language(
    text: str,
    language_models: typing.Dict[str, typing.Dict[str, float]],
    n_vals: typing.List[int]
    ) -> str:
    """
    Given a text and a dictionary of language models, return the language model 
    whose ngram probabilities best match those of the test text
    Params:
        text: the text whose language we want to identify
        language_models: a Dict of Dicts, where each key is a language name and 
        each value is a dictionary of ngram: probability pairs
        n_vals: a list of n_gram sizes to extract to build a model of the test 
        text; ideally reflect the n_gram sizes used in 'language_models'
    """
    text_model = build_model(text, n_vals)
    language = ""
    max_c = 0
    for m in language_models:
        if(check_not_in_language(text)):
            language = "not from any language"
        else:
            c = calculate_cosine(language_models[m], text_model)
            # The following line is just for demonstration, and can be deleted
            # print(f'Language: {m}; similarity with test text: {c}')
            if c > max_c:
                max_c = c
                language = m
    return language

# print(f"Test text: {text}")
# print(f"Identified language: {identify_language(text, models, n_vals=range(1,6))}")

# Prints
# Test text: i was taught that the way of progress was neither swift nor easy.
# Language: english; similarity with test text: 0.7812347488239613
# Language: german; similarity with test text: 0.6638235631734796
# Language: dutch; similarity with test text: 0.6495872103674768
# Language: french; similarity with test text: 0.7073331083503462
# Language: italian; similarity with test text: 0.6635204671187273
# Language: spanish; similarity with test text: 0.6811923819801172
# Identified language: english




def identify_languagewords(
    text: str,
    language_models: typing.Dict[str, typing.Dict[str, float]],
    n_vals: typing.List[int]
    ) -> str:
    """
    Given a text and a dictionary of language models, return the language model 
    whose ngram probabilities best match those of the test text
    Params:
        text: the text whose language we want to identify
        language_models: a Dict of Dicts, where each key is a language name and 
        each value is a dictionary of ngram: probability pairs
        n_vals: a list of n_gram sizes to extract to build a model of the test 
        text; ideally reflect the n_gram sizes used in 'language_models'
    """
    text_model = build_modelwords(text, n_vals)
    language = ""
    max_c = 0
    for m in language_models:
        c = calculate_cosine(language_models[m], text_model)
        # The following line is just for demonstration, and can be deleted
        #print(f'Language: {m}; similarity with test text: {c}')
        if c > max_c:
            max_c = c
            language = m
    return language

# print(f"Test text: {text}")
# print(f"Identified language: {identify_languagewords(text, modelswords, n_vals=range(1,3))}")

# Prints
# Test text: i was taught that the way of progress was neither swift nor easy.
# Language: english; similarity with test text: 0.7812347488239613
# Language: german; similarity with test text: 0.6638235631734796
# Language: dutch; similarity with test text: 0.6495872103674768
# Language: french; similarity with test text: 0.7073331083503462
# Language: italian; similarity with test text: 0.6635204671187273
# Language: spanish; similarity with test text: 0.6811923819801172
# Identified language: english




# t = "mij werd geleerd dat de weg van vooruitgang noch snel noch gemakkelijk is."  
# print(identify_languagewords(t, modelswords, n_vals=range(1,3)))

# t = "on m'a appris que la voie du progrès n'était ni rapide ni facile."  
# print(identify_languagewords(t, modelswords, n_vals=range(1,3)))

# t = "me enseñaron que el camino hacia el progreso no es ni rápido ni fácil."
# print(identify_languagewords(t, modelswords, n_vals=range(1,3)))



import typing
def check_not_in_language(text : str):
    flag = 1
    for m in raw_texts:
        lang_corpus = extract_wordgrams(text = m,n_vals=[1])
        text_corpus = extract_wordgrams(text = text, n_vals=[1])
        for t in text_corpus:
            if t in lang_corpus:
                flag = 0
    return flag 
    
