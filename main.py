scam_words = ["free", "shipping", "discout", "discouted", "offer", "won", "limited", "warranty", "subscription", "membership", "deals", "opportunity", "exclusive", "promo", "click", "now", "winner", "congratulation", "http", "/"]

def scam_check(text):
  
  total_words = 0
  count = 0
  for word in text:
    total_words+=1
    for tword in scam_words:
      if tword in word:
        count+=1
  return count/total_words


new_check = "Y"
while new_check == "Y":
  response = input("Hi, this is a scam checker. Would you like to input text through a text file?[Y/N]: ")
  print("\n")
  
  if response == "Y":
    file_name = input("Enter the name of the text file: ")
    text = open(file_name+'.txt','r').read()
    print("Testing this text for scam: ")
    print(text)
    text_list = text.split(" ")
    percent = scam_check(text_list) * 100
  else:
    text_og = input("Enter the text you would like to check for scams: ").split(' ')
    percent = scam_check(text_og) * 100
  
  print("Scam likely percentage: ", end='')
  print(percent)
  print("\n")
  
  strictness_level = 0
  strict = 15
  
  while strictness_level < 1 or strictness_level > 3:
    strictness_level = int(input("Choose a strictness level between 1-3: "))
    print("\n")
    if strictness_level == 1:
      strict = 15
    elif strictness_level == 2:
      strict = 25
    elif strictness_level == 3:
      strict = 35
    else:
      print("Please enter a number between 1-3.")
      print("\n")
  
  if percent >= strict:
    print("This is a scam!")
    print("\n")
  else:
    print("This is not a scam!")
    print("\n")

  new_check = input("Would you like to check another text?[Y/N]: ")
