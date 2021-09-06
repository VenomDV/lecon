date=input("Qelle est la date (j/m/a) ? : ")
"""
for element in date :
    if element == "/":
        print(end= " ")
    else:
        print(element,end= "")"""

for element in date :
    if element.isdigit():
        print(element,end="")
    else:
        print(end=" ")