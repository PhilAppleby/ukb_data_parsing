import re
from collections import Counter

class Datahelper:
  def __init__(self):
  	self.excluded_words = {
      'over': 1,
      'the': 1,
      'counter': 1,
      'mild': 1,
      'a': 1, # this will be handled by the single letter test
      'it': 1,
      'in': 1,
      'of': 1,
      'to': 1,
      'co': 1,
      'vi': 1,
      'st': 1,
      'app': 1,
      'and': 1,
      'for': 1,
      'with': 1,
      'other': 1,
      'single': 1,
      'flavour': 1,
      'fruit': 1,
      'gel': 1,
      'oil': 1,
      'cream': 1,
      'solution': 1,
      'soluble': 1,
      'suspension': 1,
      'liquid': 1,
      'tablet': 1,
      'tablets': 1,
      'pill': 1,
      'pills': 1,
      'pastille': 1,
      'granules': 1,
      'mixture': 1,
      'ointment': 1,
      'effervescent': 1,
      'capsule': 1,
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
      'paediatric': 1,
      'mint': 1,
      'caramel': 1,
      'natural': 1,
      'vitamin': 1,
      'chondroitin': 1,
      'enzyme': 1,
      'bio': 1,
      'product': 1,
      'kit': 1,
      'cold': 1,
      'constipation': 1,
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
      'pharmacy': 1,
      'heartburn': 1,
      'fish': 1,
  }


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

  def get_normalised_sentence(self, sentence):
  	return re.sub(r'[\W_ ]+', ' ', sentence)

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

#def isMeasure(word):
#  """
#  Check is the word is a measure - digits followed by measurement abbreviations
#  or full words
#  """
#  if (re.match('^\d+(m*g|m*l|micrograms)$', word)) != None:
#    return True
#  return False

  def isMeasure(self, word):
    """
    The second version of this - does the word
    begin with a series of at least 1 digit (can be followed by
    anything or nothing)
    OR
    Do we have a stand alone measure symbol
    """
    if (re.match('^\d+', word)) != None:
      return True
    if (re.match('^(m*g|m*l|micrograms)$', word)) != None:
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

