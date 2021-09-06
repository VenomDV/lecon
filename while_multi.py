i=0

nb=int(input("quelle est le nombre a multiplier ? : "))
limite = int(input("combien de fois voulais-vous multiplier ? : "))
"""
while i <= limite:
    print(f"{nb} x {limite} = {nb*i}")
   
    i+=1
"""
for i in range(limite+1):
    print(f"{nb} x {i} = {nb*i}")
    i+=1