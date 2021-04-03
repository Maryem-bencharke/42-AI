import sys
string = sys.argv
i=len(sys.argv)-1
reverse = ""
t = 0
while i>= 1:
    t = len(string[i]) -1
    while t >= 0:
        if string[i][t].isupper():
            reverse += (string[i][t]).lower()
        else:
            reverse += (string[i][t]).upper()
        t = t - 1
    i -= 1
print(reverse)

