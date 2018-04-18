import sys 
import re


user_input = sys.argv[1]
if('.txt' in user_input and len(user_input) > 4):
  try:
    text = open(user_input, 'r', encoding='utf8').read()
    text = re.sub(r'[^a-zA-Z0-9]', ' ', text)
    text_arr = text.split()
    dict_arr = {}
    for i in text_arr:
      if(i in dict_arr):
        dict_arr[i.lower()] = dict_arr[i.lower()] + 1
      else:
        dict_arr[i.lower()] = 1
  
    final_dict = sorted(dict_arr.items(), key=lambda x: (-x[1],x[0]), reverse = False)
    for i in final_dict:
      print(i[0] + " - " + str(i[1]))

    
  except:
    print("File could not be found")
else:
  print("Incorrect file input, file must be .txt")
