# CantTranslateEnough

NLP (UE20CS342) project - A multilingual language identifier and translator

### Observations

- higher the N-gram number, the more accurate the translation is since european languages have many similar words and sentence structures
- langages with similar scripts will be used since they are easier to implement using similarity distances
- complications with punctuation with respect to french and spanish
  - hypenated words and words with apostrophe need to be handled with a separate regex
  - hypenated words need to be considered as two separate words
  - apostrophe needs to be associated with the word preceding it
  - **solution** consider hypen and apostrophe as separate grams
