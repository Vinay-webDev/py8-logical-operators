#LOGICAL OPERATORS [and,or,not(bit different to understand!)] = these are used to check if two or more conditional statements are true

temp = int(input("what is the temperature outside?: "))
if temp >=0 and temp <= 30:     #***both conditional statements(i.e temp) must be true in order to become if statement true. if any one false the statement is flase too***
    print("temperature is good. go outside!")
if temp < 0 or temp > 30:  #*** any one  conditional statement needs to be true*** it doesn't care if other one false!
   print("temperature is bad. stay inside!")

#(not) we can check one or more conditional statements instead of two or more conditional statements
#what 'not' will do is if the conditional statement is true it flip it to flase,if false it flip it to true!

if not(temp >=0 and temp <= 30):
      print("temperature is good. go outside!")
if not (temp < 0 or temp > 30):
    print("temperature is bad. stay inside!")

if not(temp >=0 and temp <= 30):
    print("temperature is bad. stay inside!")
if not (temp < 0 or #temp > 30):
    print("temperature is good. go outside!")
