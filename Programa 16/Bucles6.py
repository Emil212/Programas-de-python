email=input("Introduce tu email: ")
for i in email:
    if i=="@":
        arroba=True
        break
else: #No forma parte del if, si no del for
    arroba=False
print(arroba)