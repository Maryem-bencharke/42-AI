import sys
sys.argv[0]=input("entrez un nombre:")
n =sys.argv[0]
try:
    n=int(n)
    if n==0:
        print("I am zero")
    if n%2==0 and n!=0:
         print("I'm even")
    if n%2!=0 and n!=0:
        print("I'm odd")
except ValueError:
    print("ERROR")


