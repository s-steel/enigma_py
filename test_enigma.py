from enigma import Enigma 
import unittest
from datetime import date


def test_generating_key():
  enigma = Enigma()
  key = enigma.generate_key()

  assert len(list(key)) == 5
  assert isinstance(key, str) == True

def test_generate_date():
  enigma = Enigma()
  date = enigma.generate_date()

  assert isinstance(date, str) == True
  assert len(list(date)) == 6

def test_get_offset():
  enigma = Enigma()
  date = '040895'
  offset = enigma.get_offset(date)
  expected = '1025'

  assert expected == offset

def test_get_shift():
  enigma = Enigma()
  key = '02715'
  date = '040895'
  expected = [3, 27, 73, 20]
  shift = enigma.get_shift(key, date)

  assert expected == shift

def test_shift_letter():
  enigma = Enigma()
  char_1 = 'a'
  shift_1 = 3
  char_2 = 'q'
  shift_2 = 15
  char_3 = 'y'
  shift_3 = 2

  assert enigma.shift_letter(char_1, shift_1) == 'd'
  assert enigma.shift_letter(char_2, shift_2) == 'e'
  assert enigma.shift_letter(char_3, shift_3) == ' '

def test_encrypt_message():
  enigma = Enigma()
  key = '02715'
  date = '040895'
  message = 'hello world'
  encrypted_message = enigma.encrypt_message(message, key, date)

  assert 'keder ohulw' == encrypted_message

def test_encrypt_with_key_date():
  message = 'hello world'
  key = '02715'
  date = '040895'
  enigma = Enigma()

  outcome = enigma.encrypt(message, key, date)

  expected = {
              'encryption': 'keder ohulw',
              'key': '02715',
              'date': '040895'
              }

  assert outcome == expected

def test_encrypt_with_exclamation():
  message = 'hello world!'
  key = '02715'
  date = '040895'
  enigma = Enigma()

  outcome = enigma.encrypt(message, key, date)

  expected = {
              'encryption': 'keder ohulw!',
              'key': '02715',
              'date': '040895'
              }

  assert outcome == expected

def test_encryption_with_special_chars():
  message = '? : # * }'
  key = '01020'
  date = '010203'
  enigma = Enigma()

  outcome = enigma.encrypt(message, key, date)

  expected = {'encryption': '?l:b#l*b}',
              'key': '01020',
              'date': '010203'
              }

  assert expected == outcome


# More tests without a key or date for encryption 
# These would need to be mocked out 

# def test_encrypt_with_only_key():
#   message = 'hello world'
#   key = '02715'
#   enigma = Enigma()
#   outcome = enigma.encrypt(message, key)
#   expected = {
#               'encryption': 'keder ohulw',
#               'key': '02715',
#               'date': date.today().strftime("%d%m%y")
#               }

#   assert outcome == expected

# def test_encrypt_without_key_or_date():
#   message = 'hello world'
#   enigma = Enigma()
#   outcome = enigma.encrypt(message)

#   assert outcome['encryption'] == 'keder ohulw'
