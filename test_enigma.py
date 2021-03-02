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