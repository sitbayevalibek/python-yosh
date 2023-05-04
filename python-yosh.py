# Yosh bo'yicha taqsimlaydigan kichik dastur
yosh = int(input("Yoshingizni kiriting: "))
if yosh<10:
    j = "Bola"
elif yosh<18:
    j = "O'smir"
elif yosh<60:
    j = "Katta"
else:
    j = "Keksa"
print(f"Siz {yosh} dasiz va siz {j} ekansiz")