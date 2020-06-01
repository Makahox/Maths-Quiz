
import random



def main():
    print("Welcome to the randomly generated maths quiz")
    print("Randomly generated maths problems will be displayed")
    print("Your answer will be checked, if correct you will be awarded 1 point")
    dif = input("please select your difficulty (E/M/H)").lower()
    score = 0
    if dif == "e":
        while True:
            ops = ["+", "-", "*"]
            num1 = random.randint(1,12)
            num2 = random.randint(1,10)
            operation = random.choice(ops)
            answer = eval(str(num1) + operation + str(num2))

    
            print("___", operation, num2, " = ", answer)
            user_inp = input("Enter answer: ")
            if user_inp == str(num1):
                print("Correct")
                score = score + 1
                print("Score: ", score)
                
            else:
                print("Incorrect")
                
            choice = input("Would you like to continue? (Y/N) :").lower()
            if choice == "y":
                continue
            elif choice == "n":
                print("Final Score: ", score)
                print("Thank you for playing!")
                break
            else:
                print("That is an invalid response")
                break

    elif dif == "m":
         while True:
            ops = ["+", "-", "*"]
            num1 = random.randint(1,100)
            num2 = random.randint(1,200)
            operation = random.choice(ops)
            answer = eval(str(num1) + operation + str(num2))

            print("___", operation, num2, " = ", answer)
            user_inp = input("Enter answer: ")
            if user_inp == str(num1):
                print("Correct")
                score = score + 1
                print("Score: ", score)
            else:
                print("Incorrect")
                
            choice = input("Would you like to continue? (Y/N) :").lower()
            if choice == "y":
                continue
            elif choice == "n":
                print("Final Score: ", score)
                print("Thank you for playing!")
                break
            else:
                print("That is an invalid response")
                break
    elif dif == "h":
        while True:
            ops = ["+", "-", "*", "/"]
            num1 = random.randint(1,200)
            num2 = random.randint(1,100)
            operation = random.choice(ops)
            answer = eval(str(num1) + operation + str(num2))
            if operation == "/":
                num1 = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 86, 87, 88, 90, 91, 92, 99, 100]
                num2 = []
                num1 = random.choice(num1)
                for i in range(1, num1):
                    if num1 % i == 0:
                        num2.append(i)
                num2 = random.choice(num2)
                answer = eval(str(num1) + operation + str(num2))
                

            print("___", operation, num2, " = ", answer)
            user_inp = input("Enter answer: ")
            if user_inp == str(num1):
                print("Correct")
                score = score + 1
                print("Score: ", score)
            else:
                print("Incorrect")
        
            choice = input("Would you like to continue? (Y/N) :").lower()
            if choice == "y":
                continue
            elif choice == "n":
                print("Final Score: ", score)
                print("Thank you for playing!")
                break
            else:
                print("That is an invalid response")
                break
    else:
        print("That is an invalid difficulty")


if __name__ == "__main__":
    main()
