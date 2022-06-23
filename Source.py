import random
import string  
def pwd_generator():
  for character in range(4):
   character=random.choice(string.ascii_lowercase)
   print(character, end = '')

  for number in range(4):
    number=random.randint(1,9)
    print(number, end = '')
  
pwd_generator()