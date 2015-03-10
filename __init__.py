#!/usr/bin/env python

# Flashcard
# Very simple text-based quiz-yourself application

import os, sys

from store import Database

APP_PATH = os.path.dirname(os.path.abspath(__file__))
DB_PATH = APP_PATH + '/db'

def main_menu(CURRENT_CARD_SET = None):
  clear_screen()

  prompt('Please choose an Option from the Menu',False)
  if CURRENT_CARD_SET:
    prompt('current card set: %s\n' % (CURRENT_CARD_SET),False)
  choices = ['Create a New Card Set', 'Load Card Set', 'Add a Card to an Existing Card Set', 'Quiz yourself', 'Quit']
  print '\n'.join("({}) {}".format(n,v) for n,v in enumerate(choices,start=1))
  response = prompt('',True)

  if response in ['1']:
    create_new_card_set() 
  if response in ['2']:
    card_set = load_card_set()
  if response in ['3']:
    add_to_existing_card_set()
  if response in ['3']:
    quiz_yourself()
  if response in ['q','Q','5']:
    sys.exit(0)
  
  return card_set

def create_new_card_set(error_msg=None):
  clear_screen()
 
  if error_msg:
    name = clean_filename(prompt(error_msg))
  else:
    name = clean_filename(prompt('Please Enter a Name for your Cardset:'))

  if not name: 
    error_msg = "You didn't provide a valid name"
    create_new_card_set(error_msg)
 
  elif name and not file_exists(name):
    with open(APP_PATH + '/' + 'db/' + name + '.db','a+') as f:
      f.write('')
      prompt('Card Set %s created successfuly. Hit Enter to proceed' % (name))

  elif name and file_exists(name):
    error_msg = 'This file already exists. Please Choose Another Name:\n'
    create_new_card_set(error_msg)

def load_card_set():
  clear_screen()
  cardsets = [ (DB_PATH + '/' + f) for f in os.listdir(DB_PATH) if f.endswith('.db') ]
  cardsets.sort(key=os.path.getctime)
  prompt('Please Choose a Cardset:', False)
  print '\n'.join('({}) {}'.format(n,os.path.basename(v)) for n,v in enumerate(cardsets))  
  response = int(prompt())
  db = Database(cardsets[response])
  if db.db_name:
    CURRENT_CARD_SET = db.db_name
    prompt('Card Set Loaded!')

  return CURRENT_CARD_SET
 
def clean_filename(filename):
  return filename.replace(' ','_')

def add_to_existing_card_set():
  pass

def quiz_yourself():
  pass

def clear_screen():
  os.system('clear')

def file_exists(filename=None, loc=None):
  if loc is None:
    loc = APP_PATH + '/db'
  if filename:
    return os.path.isfile(loc + '/' + filename)
  else:
    print 'no filename passed' 
    return None

def perror(error=None):
  if error: print error
  

# prompts or just prints if you pass it prompt = False
def prompt(text='',response=True):
  text = text.strip()
  if response:
    return raw_input(text)
  else:
    print text + '\n'

def handle(response):
  pass





def main():
  card_set = None
  while True:
    card_set = main_menu(CURRENT_CARD_SET=card_set)
    card_set = os.path.basename(card_set).split('.db')[0].upper()
    

if __name__ == '__main__':
  main()
