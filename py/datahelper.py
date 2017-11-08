import re
from collections import Counter

class Datahelper:
  def __init__(self):
    self.cls_phrases = {}
    self.excluded_words = {
      'over': 1,
      'the': 1,
      'counter': 1,
      'mild': 1,
      'a': 1, # this will be handled by the single letter test
      'it': 1,
      'in': 1,
      'on': 1,
      'non': 1,
      'of': 1,
      'to': 1,
      'co': 1,
      'vi': 1,
      'st': 1,
      'bp': 1,
      'app': 1,
      'and': 1,
      'aid': 1,
      'for': 1,
      'with': 1,
      'other': 1,
      'single': 1,
      'flavour': 1,
      'fruit': 1,
      'gel': 1,
      'oil': 1,
      'cream': 1,
      'aloe': 1,
      'solution': 1,
      'soluble': 1,
      'suspension': 1,
      'liquid': 1,
      'tablet': 1,
      'tab': 1,
      'tablets': 1,
      'pill': 1,
      'pills': 1,
      'pastille': 1,
      'granules': 1,
      'mixture': 1,
      'ointment': 1,
      'effervescent': 1,
      'capsule': 1,
      'cap': 1,
      'suppository': 1,
      'supplement': 1,
      'compound': 1,
      'caustic': 1,
      'pellet': 1,
      'elixir': 1,
      'drops': 1,
      'inhaler': 1,
      'sachet': 1,
      'sachets': 1,
      'syrup': 1,
      'lozenge': 1,
      'lozenges': 1,
      'spray': 1,
      'paste': 1,
      'gum': 1,
      'tincture': 1,
      'oral': 1,
      'injection': 1,
      'injectable': 1,
      'applicator': 1,
      'ampoule': 1,
      'syringe': 1,
      'pack': 1,
      'combination': 1,
      'prefilled': 1,
      'continuous': 1,
      'patch': 1,
      'gastro': 1,
      'resistant': 1,
      'relief': 1,
      'wool': 1,
      'sand': 1,
      'fat': 1,
      'aloe': 1,
      'iu': 1,
      'cover': 1,
      'bath': 1,
      'powder': 1,
      'solvent': 1,
      'formula': 1,
      'green': 1,
      'yellow': 1,
      'red': 1,
      'blue': 1,
      'orange': 1,
      'buff': 1,
      'golden': 1,
      'white': 1,
      'paediatric': 1,
      'mint': 1,
      'caramel': 1,
      'natural': 1,
      'vitamin': 1,
      'enzyme': 1,
      'bio': 1,
      'product': 1,
      'kit': 1,
      'cold': 1,
      'dry': 1,
      'unknown': 1,
      'free': 1,
      'leg': 1,
      'body': 1,
      'eye': 1,
      'stomach': 1,
      'breath': 1,
      'sleep': 1,
      'drowsy': 1,
      'litre': 1,
      'actuated': 1,
      'vantage': 1,
      'numark': 1,
      'care': 1,
      'galpharm': 1,
      'pharmacy': 1,
      'fish': 1,
      'aluminium': 1,
      'sodium': 1,
      'zinc': 1,
      'acid': 1,
      'forte': 1,
      'simple': 1,
      'plus': 1,
      'multi': 1,
      'adult': 1,
      'liver': 1,
  }

  def load_cls_phrases(self, fh):
    hdr = fh.readline()
    for line in fh:
      data = line.strip().split(',')
      # guards against unparseable debug lines
      if len(data) < 2:
        continue
      code = data[0]
      phrase_array = [data[1].lower().strip()]
      if len(data) > 2:
        phrase_array += data[2].lower().strip().split('|')
    
      for phrase in phrase_array:
        for key in self.get_key_list(phrase):
          if key not in self.cls_phrases:
            self.cls_phrases[key] = []
          self.cls_phrases[key].append(code)

    return len(self.cls_phrases)

  def get_phrase_dictionary(self):
    return self.cls_phrases

  def match_phrase(self, phrase):
    """
    Attempt to match the argument phrase to the cls_phrases dictionary 
    (built from all words passed in at init time)
    A phrase is matched iff:
    The whole string matches matches OR
    The prefix trigram matches OR
    The prefix bigram matches OR
    A single word, which is not an excluded word, matches  

    Return:
    A matched code from the classification system or None
    """
    key = None
    match_phrase = None
    for key in self.get_key_list(phrase):
      if key in self.cls_phrases:
        match_phrase = key
        break
    
    if match_phrase == None:
      return None, key
    return self.get_most_common(self.cls_phrases[match_phrase]), key

  def get_key_list(self, phrase):
    ngram = self.get_normalised_phrase(phrase)
    key_list = [ngram]
    word_list = ngram.split()
    if len(word_list) > 2:
      key_list.append(' '.join(word_list[0:3]))
    if len(word_list) > 1:
      key_list.append(' '.join(word_list[0:2]))

    for word in [x for x in word_list if self.isExcluded(x.strip()) == False]:
      key_list.append(word)

    return key_list

  def isExcluded(self, word):
    """
    """
    if self.isExcludedWord(word) == False: 
      if self.isMeasure(word) == False:
        if self.isSingleLetter(word) == False:
          return False
    return True 

  def isExcludedWord(self, word):
    """
    """
    if word in self.excluded_words:
      return True
    return False 

  def get_most_common(self, lst):
    """
    Return the most commonly occuring value in a list
    """
    data = Counter(lst)
    return data.most_common(1)[0][0]

  def get_normalised_phrase(self, sentence):
  	return re.sub(r'[\W_ ]+', ' ', sentence).lower()

  def format_bnf_code(self, code):
    code = code.strip()
    ch = code[0:2]
    s = code[2:4]
    ss = '00'
    if len(code) >=6:
      ss = code[4:6]
    if ss != '00':
      return "%d.%d.%d" % (int(ch),int(s),int(ss))
    return "%d.%d" % (int(ch),int(s))

  def isMeasure(self, word):
    """
    The second version of this - does the word
    begin with a series of at least 1 digit (can be followed by
    anything or nothing)
    OR
    Do we have a stand alone measure symbol
    """
    #if (re.match('^\d+', word)) != None:
    #  return True
    if (re.match('(m*g|m*l|micrograms)$', word)) != None:
      return True
    return False

  def isSingleLetter(self, word):
    """
    Check if the word consists of a single letter (generated by string
    normalisation)
    """
    if (re.match('^\w$', word)) != None:
      return True
    return False


