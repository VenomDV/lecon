txt=str(input("ecrire une phrase : "))
reversed_str=txt[::-1]
print(reversed_str)

taille = len(txt)
for i in range(taille-1,-1,-1):
    print(txt[i],end="")