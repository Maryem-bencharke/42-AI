import random
import sys
print("can you guess the right number?")
print("the number you are looking for is between 1 and 99.")
print("If you want to quit the game entrer exit.")
sys.argv[0]=input("what's your guess between 1 and 99:")
n=sys.argv[0]
a=random.randint(1,99)
m=0
while True:
    m+=1
    try:
        if n=='exit':
            print("Goodbye")
            break
        n=int(n)
        if n < a:
            print("Too low!")
            n=int(input("try another one:"))
        if n > a:
             print("Too high!")
             n=int(input("try another one:"))
        if n == a:
            print("congratulations, you've got it! you get the number after",m,"tries.")
            break
    except ValueError:
        print("that is not a number:try another one.") 
        break
