import re
from collections import Counter

class Datahelper:
  def __init__(self):
    self.cls_phrases = {}
# Explicit exclusions - short words and measures are taken out elsewhere
    self.excluded_words = {
      'active': 1,
      'activated': 1,
      'artificial': 1,
      'band': 1,
      'coconut': 1,
      'food': 1,
      'biscuit': 1,
      'biscuits': 1,
      'good': 1,
      'choice': 1,
      'house': 1,
      'half': 1,
      'total': 1,
      'alka': 1,
      'alpha': 1,
      'beta': 1,
      'night': 1,
      'nurse': 1,
      'dome': 1,
      'continus': 1,
      'depot': 1,
      'micro': 1,
      'over': 1,
      'long': 1,
      'slow': 1,
      'hayfever': 1,
      'counter': 1,
      'mild': 1,
      'with': 1,
      'other': 1,
      'single': 1,
      'double': 1,
      'triple': 1,
      'once': 1,
      'flavour': 1,
      'fruit': 1,
      'cream': 1,
      'need': 1,
      'needs': 1,
      'aloe': 1,
      'infusion': 1,
      'preparation': 1,
      'preparations': 1,
      'preps': 1,
      'shampoo': 1,
      'shower': 1,
      'enema': 1,
      'soap': 1,
      'solution': 1,
      'soln': 1,
      'contact': 1,
      'diluent': 1,
      'blocker': 1,
      'emulsion': 1,
      'emuls': 1,
      'emulsifying': 1,
      'lotion': 1,
      'lotio': 1,
      'soluble': 1,
      'suspension': 1,
      'paint': 1,
      'liquid': 1,
      'tablet': 1,
      'tablets': 1,
      'pill': 1,
      'pills': 1,
      'perles': 1,
      'pastille': 1,
      'chewable': 1,
      'granules': 1,
      'mixture': 1,
      'mixtures': 1,
      'remedy': 1,
      'remedies': 1,
      'therapy': 1,
      'therapies': 1,
      'emollient': 1,
      'peel': 1,
      'gppe': 1,
      'ointment': 1,
      'effervescent': 1,
      'capsule': 1,
      'spansule': 1,
      'caplet': 1,
      'cycle': 1,
      'husk': 1,
      'strong': 1,
      'strength': 1,
      'suppository': 1,
      'supplement': 1,
      'compound': 1,
      'comp': 1,
      'caustic': 1,
      'pellet': 1,
      'elixir': 1,
      'drops': 1,
      'autohaler': 1,
      'turbohaler': 1,
      'inhaler': 1,
      'sachet': 1,
      'sachets': 1,
      'syrup': 1,
      'dried': 1,
      'castor': 1,
      'oily': 1,
      'salt': 1,
      'salts': 1,
      'saline': 1,
      'tears': 1,
      'ophthalmic': 1,
      'complexes': 1,
      'comp': 1,
      'aqua': 1,
      'aqueous': 1,
      'hormone': 1,
      'sugar': 1,
      'plain': 1,
      'anti': 1,
      'retard': 1,
      'drug': 1,
      'lozenge': 1,
      'lozenges': 1,
      'spray': 1,
      'paste': 1,
      'tincture': 1,
      'oral': 1,
      'injection': 1,
      'injectable': 1,
      'applicator': 1,
      'ampoule': 1,
      'syringe': 1,
      'duopack': 1,
      'pack': 1,
      'combination': 1,
      'prefilled': 1,
      'continuous': 1,
      'dispersible': 1,
      'patch': 1,
      'gastro': 1,
      'resistant': 1,
      'relief': 1,
      'wool': 1,
      'sand': 1,
      'aloe': 1,
      'ortho': 1,
      'auto': 1,
      'health': 1,
      'cover': 1,
      'bath': 1,
      'powder': 1,
      'resin': 1,
      'solvent': 1,
      'solv': 1,
      'mist': 1,
      'saliva': 1,
      'balsam': 1,
      'tonic': 1,
      'additive': 1,
      'liniment': 1,
      'recon': 1,
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
      'peppermint': 1,
      'mint': 1,
      'pine': 1,
      'caramel': 1,
      'natural': 1,
      'vitamin': 1,
      'vitamins': 1,
      'enzyme': 1,
      'product': 1,
      'cold': 1,
      'unknown': 1,
      'free': 1,
      'body': 1,
      'nose': 1,
      'stomach': 1,
      'scalp': 1,
      'intramuscular': 1,
      'breath': 1,
      'sleep': 1,
      'drowsy': 1,
      'litre': 1,
      'actuated': 1,
      'vantage': 1,
      'numark': 1,
      'care': 1,
      'galpharm': 1,
      'merck': 1,
      'pharmacy': 1,
      'fish': 1,
      'aluminium': 1,
      'calcium': 1,
      'sodium': 1,
      'sodium chloride': 1,
      'disodium': 1,
      'zinc': 1,
      'magnesium': 1,
      'undecenoic': 1,
      'oxide': 1,
      'phosphate': 1,
      'hydrate': 1,
      'acetate': 1,
      'fumarate': 1,
      'sandoz': 1,
      'pain': 1,
      'mite': 1,
      'remover': 1,
      'removers': 1,
      'acid': 1,
      'alcohol': 1,
      'coal': 1,
      'extract': 1,
      'mineral': 1,
      'forte': 1,
      'simple': 1,
      'plus': 1,
      'multi': 1,
      'vita': 1,
      'adult': 1,
      'liver': 1,
      'factor': 1,
      'human': 1,
      'methyl': 1,
      'piperazine': 1,
      'deep': 1,
  }

  def load_cls_phrases(self, fh):
    #hdr = fh.readline()
    for line in fh:
      data = line.strip().split(',')
      # guards against unparseable lines
      if len(data) < 2:
        continue
      code = data[0]
      phrase_array = [data[1].lower().strip()]
      if len(data) > 2:
        syn_array = data[2].lower().strip().split('|')
        for syn in [s for s in syn_array if s not in phrase_array]:
          phrase_array.append(syn) 
    
      for phrase in phrase_array:
        for key in set(self.get_key_list(phrase)):
          if key not in self.cls_phrases:
            self.cls_phrases[key] = []
          #print "%s -> %s" % (key, str(code))
          self.cls_phrases[key].append(code)

    return len(self.cls_phrases)

  def get_phrase_dictionary(self):
    return self.cls_phrases

  def get_phrase_dictionary_keys(self):
    return sorted(self.cls_phrases.keys())

  def get_excluded_words(self):
    return sorted(self.excluded_words.keys())

  def match_all_phrases(self, inphrases):
    """
    Attempt to match the argument phrases to the cls_phrases dictionary 
    First attempt a match of all phrase, then all trigrams, then all
    bigrams, then single words 

    Return:
    A matched code from the classification system or None
    """
#   temporary - attempted matches
    attempted_matches = []
    phrase = ""
    step = "A"
    # ALL all full phrases 
    for phrase in inphrases:
      attempted_matches.append(phrase + ':' + step)
      if phrase in self.cls_phrases:
        return self.get_most_common(self.cls_phrases[phrase]), attempted_matches, phrase

    phrases = [self.get_normalised_phrase(p) for p in inphrases]

    # all normalised phrases 
    #for phrase in phrases:
    #  attempted_matches.append(phrase)
    #  if phrase in self.cls_phrases:
    #    return self.get_most_common(self.cls_phrases[phrase]), attempted_matches

    # 3 all prefix trigrams 
    step = "3"
    for ngram in [p.split()[0:3] for p in phrases if len(p.split()) > 3]:
      phrase = ' '.join(ngram)
      attempted_matches.append(phrase + ':' + step)
      if phrase in self.cls_phrases:
        return self.get_most_common(self.cls_phrases[phrase]), attempted_matches, phrase

    # 2 all prefix bigrams 
    step = "2"
    for ngram in [p.split()[0:2] for p in phrases if len(p.split()) > 2]:
      phrase = ' '.join(ngram)
      attempted_matches.append(phrase + ':' + step)
      if phrase in self.cls_phrases:
        return self.get_most_common(self.cls_phrases[phrase]), attempted_matches, phrase

    # 1 all valid words 
    step = "1"
    for phr_elem in phrases:
      for phrase in [w for w in phr_elem.split() if self.isExcluded(w.strip()) == False]:
        attempted_matches.append(phrase + ':' + step)
        if phrase in self.cls_phrases:
          return self.get_most_common(self.cls_phrases[phrase]), attempted_matches, phrase

    return None, attempted_matches, phrase

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
    if len(word_list) > 3:
      key_list.append(' '.join(word_list[0:3]))
    if len(word_list) > 2:
      key_list.append(' '.join(word_list[0:2]))

    for word in [x for x in word_list if self.isExcluded(x.strip()) == False]:
      if word not in key_list:
        key_list.append(word)

    return key_list

  def isExcluded(self, word):
    """
    """
    if self.isExcludedWord(word) == False: 
      if self.isMeasure(word) == False:
        if self.isShortWord(word) == False:
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

  def get_best_guess(self, lst):
    """
    Return the best guess at a value from 
    a list of strings
    """
    maxlen = 0
    pass
    #for elem in lst:

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
    if (re.match('^\d+$', word)) != None:
      return True
    #if (re.match('^\d\d$', word)) != None:
    #  return True
    #if (re.match('^\d\d\d$', word)) != None:
    #  return True
    if (re.match('^\d*(m*g|m*l|iu|mcg|uml|u1ml|mg4ml|micrograms|million|cm|mm|unit|units|hb)', word)) != None:
      return True
    return False

  def isShortWord(self, word):
    """
    Check if the word is longer than 3 chars 
    """
    if len(word) < 4:
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


