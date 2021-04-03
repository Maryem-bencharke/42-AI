import sys
n1=int(sys.argv[1])
n2=int(sys.argv[2])
i=len(sys.argv)
if i<=3:
    if type(n1)==int and type(n2)==int:
                print("sum=",n1+n2)
                if n1>n2:
                    print("diff",n1-n2)
                else:
                    print("diff",n2-n1)
                print("produit",n1 * n2)
                if n2!=0:
                    print("le quotien",n1 / n2)
                else:
                    print("ERROR")
                if n2!=0:
                    print("remainder",n1 % n2)
                else:
                    print("ERROR")
if type(n1)!=int or type(n2)!=int:
        print("only numbers") 
