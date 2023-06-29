import random

print("""*****************************
           HELLO!!!           
WELCOME TO THE GUESSING GAME!
*****************************""")
b = random.randint(1, 20)
try_counter = 1
while True:
    try:
        a = int(input("   Make a guess(1-20):"))
    except ValueError:
        print("""🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴
 please enter an integer
🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴""")
        continue

    if a > 0 and a < 21:
        if a == b:
            print("""
🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳
 Yayy you made a correct guess!
🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳""")
            break
        else:
            print(" Incorrect guess Try Again")
        try_counter += 1
    else:
        print("""
🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴
Number must be between 1 and 20!
🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴""")
print(f"""
***********************************************
you required {try_counter} choices to make a correct guess
***********************************************
""")


#OR
# import sys
# import random
# b=random.randint(1,20)
# try_counter=1
# while True:
#     try:
#         a=int(sys.argv[1])
#     except ValueError:
#         print("please enter an integer")
#         continue

#     if a>0 and a<21:
#         if a==b:
#             print("\nYayy you made a correct guess")
#             break
#         try_counter+=1
#     else:
#         print("Number must be between 1 and 20")
# print(f"you required {try_counter} choices to make a correct guess")