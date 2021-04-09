import string
import sys

if len(sys.argv) == 3:
    n1 = str(sys.argv[1])
    n2 = int(sys.argv[2])
    try:
        if len(sys.argv) == 3:
            n1=sys.argv[1]
            n2=sys.argv[2]
            L=[]
        n1=str(n1)
        n2=int(n2)
        word = n1.split()
        if type(n1)==str and  type(n2)==int:
            for t in word:
                if len(t) > n2:
                    print(t)
                    L.append(word)
        else:
            print("ERROR")
    except ValueError:
        print("ERROR")
else:
    print("ERROR")