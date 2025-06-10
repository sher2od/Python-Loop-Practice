from random import randint

sirli_son = randint(1, 10)  # Kompyuter 1 dan 10 gacha bir son o‘ylaydi
k = 0

while k < 3:
    taxmin = int(input("Parolni toping (1-10): "))
    k += 1
    if taxmin == sirli_son:
        print("Topdingiz!")
        break
    else:
        print("Notogri. Yana urinib koring.")

if k == 3 and taxmin != sirli_son:
    print("Urinishlar tugadi. Togri javob:", sirli_son)
