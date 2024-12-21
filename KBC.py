def kbc():
    print('''Que number 1 For 10k: 
                 Bharat ka Rashtrapati kaun hai?
                 A) Narendra Modi
                 B) Amit Shah
                 C) Droupadi Murmu
                 D) Jagdeep Dhankhar")''')
    ans1 = input("Your answer is : ")
    if(ans1== 'A'):
        print("Congratulations You won the 10k")
        print(''' Que number 2 for 1 lhk :
                      Vitaran mein sabse teji se badhne wala desh kaun hai?
                      A) Chine
                      B) Bharat
                      C) America
                      D) Japan''')
        ans2 = input("Your answer is : ")
        if(ans2=='B'):
            print("Congratulations You won the 10k")
            print("Thank You") 
        else:
            print("You lost The Game")

    else:
        print("You lost The Game")
    

print("CHOSSE OPTION 1 or 2")
print("1. ENTER IN KBC GAME")
print("2. EXIT")

option = int(input("Enter the option"))

match option:
    case 1:
        print("ALL THE BEST")
        kbc()
        
    case _:
        print("Thank You")

