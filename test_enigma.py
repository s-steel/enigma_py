from enigma import Enigma 
import unittest


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

# # encrypt a message with a key and date
# pry(main)> enigma.encrypt("hello world", "02715", "040895")
# #=>
# #   {
# #     encryption: "keder ohulw",
# #     key: "02715",
# #     date: "040895"
# #   }

# # decrypt a message with a key and date
# pry(main) > enigma.decrypt("keder ohulw", "02715", "040895")
# #=>
# #   {
# #     decryption: "hello world",
# #     key: "02715",
# #     date: "040895"
# #   }


# from enigma import Enigma

# def test_encrypting_message():
#     message = 'hello world'
#     key = '02715'
#     date = '040895'
#     enigma = Enigma()

#     outcome = enigma.encrypt(message, key, date)

#     expected = {
#     'encryption': 'keder ohulw',
#     'key': '02715',
#     'date': '040895'
#     }

#     assert outcome == expected