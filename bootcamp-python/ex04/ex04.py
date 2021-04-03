import sys
sys.argv[1]=("entrez 1er nombre:")
sys.argv[2]=("entrez le 2eme nombre:")
n1=sys.argv[1]
n2=sys.argv[2]
i=len(sys.argv)
j=0
##while type(n1)==int and type(n2)==int:
try:
        n1=int(n1)
        n2=int(n2)
        for j in range(i):
            while j<=i:
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
except ValueError:
        print("ERROR") 
print("only numbers") 