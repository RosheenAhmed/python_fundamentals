# task - Take user weight as input, ask user if he/she has entered his weight in kg or lbs
# k or kg and l for lbs
# if the weight is in kgs then covert and print it into lbs
# if the weight is in lbs then convert and print in into kgs

# sudo code
# 1- take user weight in input and store it in a variable
# 2- take user choice as k or l to covert accordingly
# 3- If this choice is kg then covert and print it in lbs
# 4- else convert and print it in kgs

weight = input("enter your weight ")
choice = input("Enter k for killogram and l for pounds ")
if choice == 'k':
    weight = float(weight) * 2.20462
    print (f"your weight in lbs = {weight}")
else:
    weight = float(weight) * 0.453592
    print ("your weight in kg =" + str(weight))









