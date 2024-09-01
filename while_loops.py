# starting point
# condition
# increment

# counter = 1
# while counter <= 5:
#     print(counter)
#     counter = counter + 1

# moderate  calculator which work with two numbers
while True:
    print("\nWelcome to moderate calculator!\n")
    # as input function give us value in string so we are converting our string input into integer
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))

    # take input for operator like + - * /
    operation = input("""Enter the operation you want to perform
    + for addition
    - for subtractionn
    * for mulitplicatioin
    / for division
    0 for exit calculator
    """)
    if operation == "+":
        print(f"Sum = {num1 + num2}")
    elif operation == "0":
        print("Exiting calculator, good bye!")
        break # we use break keywork to terminate the loop
    else:
        print("In valid input")