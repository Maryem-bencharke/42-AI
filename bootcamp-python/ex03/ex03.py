import string
def text_analyzer(c=input("entrez votre texte:")):
    ##c=input("entrez votre texte:",c)
    n=len(c)
    b=0
    d=0
    e=0
    a=0
    f=0
    for i in range(n):
        if c[i].isupper():
            a+=1
            b+=1
        if c[i].islower():
           a+=1
           d+=1
        if c[i]=="":
            a+=1
            f+=1
        if c[i] in string.punctuation:
            a+=1
            e+=1
    print("tyhe text contains",a,"characters")
    print(b,"upper letters")
    print(d,"lower letters")
    print(e,"punctuation marks")
    print(f,"spaces")
m=str(input())
text_analyzer(m)



        
   




