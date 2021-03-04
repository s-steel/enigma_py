import string
import random
from datetime import date

class Enigma: 
  letters = list(string.ascii_lowercase)
  letters.append(' ')

  def generate_key(self):
    digits = random.sample(range(0, 10), 5)
    return ''.join([str(num) for num in digits])

  def generate_date(self):
    return date.today().strftime("%d%m%y")

  def get_offset(self, date):
    return str(int(date) * int(date))[-4:]

  def get_shift(self, key, date):
    offset = self.get_offset(date)
    shift = [
      int(key[:2]) + int(offset[:1]),
      int(key[1:3]) + int(offset[1:2]),
      int(key[2:4]) + int(offset[2:3]),
      int(key[3:5]) + int(offset[3:4])
    ]
    return shift

  def shift_letter(self, letter, shift):
    letter_index = self.letters.index(letter)
    if letter_index + shift > 27:
      shift = (letter_index + shift) % 27
      return self.letters[shift]
    else:
      return self.letters[letter_index + shift]

  def encrypt_message(self, message, key, date):
    new_message = []
    index = 0
    shift = self.get_shift(key, date)
    for char in list(message.lower()):
      new_letter = self.shift_letter(char, shift[index])
      new_message.append(new_letter)
      if index >= 3:
        index = 0
      else:
        index += 1

    return ''.join(new_message)

#   def encrypt(self, message, key, date):
#     new_message = []
#     shift = self.get_shift(key, date)
#     if len(message) == 0:
#       ''
#     else:
#       # self.shift_letter(message[0], shift[0]) + encrypt(strip(message[1:-1]), date)
#       # new_message = self.shift_letter(message[0], shift[0]) + self.encrypt(message[1:-1], key, date)
#     # for char in list(message.lower()):
#     #   new_msg.append(self.letters[new_loc])
#       return new_message

#     def rev_str(s)
#   if s.empty?
#     ''
#   else 
#     s[-1] + rev_str(s.slice(0..-2))
#   end
# end