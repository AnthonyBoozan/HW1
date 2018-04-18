import sys 
import re


user_input_1 = sys.argv[1]
user_input_2 = sys.argv[2]
#Count keeps track of words in common
count = 0
if('.txt' in user_input_1 and '.txt' in user_input_2 and len(user_input_1) > 4 and len(user_input_2) > 4):
  try:
    text_1 = open(user_input_1, 'r', encoding='utf8').read()
    text_1 = re.sub(r'[^a-zA-Z0-9]', ' ', text_1)
    text_arr_1 = text_1.split()
    text_2 = open(user_input_2, 'r', encoding='utf8').read()
    text_2 = re.sub(r'[^a-zA-Z0-9]', ' ', text_2)
    text_arr_2 = text_2.split()
    dict_arr_1 = {}
    dict_arr_2 = {}

    for i in text_arr_1:
      dict_arr_1[i] = ""

    for i in text_arr_2:
      dict_arr_2[i] = ""

    dict_arr_1 = list(dict_arr_1.keys())
    dict_arr_2 = list(dict_arr_2.keys())

    for i in dict_arr_1:
      if(i in dict_arr_2):
        print(i)
        dict_arr_2.remove(i)
        count = count + 1

          
    print(str(count) + " words in common")
  except:
    print("File could not be found")
else:
  print("Invalid input, both files must be .txt")
