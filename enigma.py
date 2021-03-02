import string
import random
from datetime import date

class Enigma: 
  letters = list(string.ascii_lowercase).append(' ')

  def generate_key(self):
    digits = random.sample(range(0, 10), 5)
    return ''.join([str(num) for num in digits])

  def generate_date(self):
    return date.today().strftime("%d%m%y")
