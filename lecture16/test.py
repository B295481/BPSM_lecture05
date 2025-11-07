answers = {}
answers['name'] = input("What is your name?\n")
answers['color'] = input("What is your favorite color"\n)
answers['python'] = input("Do you like python?\n")
answers['world'] = input("Is the world flat? True or False\n")
if answers['world'] not in ['True','False']:
  print("You didn't say True or False, please try again")
  while answers['world'] not in ['True','False']:
    answers['world'] = input("Is the world flat? True or False\n")
print("""
Your name is %s\n
Your favorite color is %s\n
You %s python\n
%s, the world is flat
"""%(answers['name'],answers['color'],answers['python'],answers['world']))