nom=input("comment vous appelez vous ? : ")
age=int(input("vous avez quelle age ? : "))
print(f"Hello votre nom est {nom} et vous avez {age} ans.")

if age<14:
    print(f"Vous avez {age}. Accés gratuit.")
elif 14<=age<=18:
    print(f"Vous avez {age}. Accés payant.")
elif age>18:
    print(f"Vous avez {age}. Accés interdit.")