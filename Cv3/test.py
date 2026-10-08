
# pi = 3.14159
# r = float(input("zadaj polomer: "))
# obvod = 2 * pi * r
# obsah = pi * r * r
# print("obvod je", obvod)
# print("obsah je", obsah)


# n = int(input("zadaj n: "))
# zrnka = 2 ** (n - 1)
# print(f"na {n}. políčku bude {zrnka} zrniek ryže")


# n = int(input("zadaj n: "))
# for i in range(1, n + 1):
#     print("*" * i)

# import random

# n = int(input("zadaj n: "))
# cestujuci = 100

# for i in range(n):
#     nastupili = random.randint(0, 9)
#     vystupili = random.randint(0, 9)
#     cestujuci = cestujuci + nastupili - vystupili
#     print(f"Vo vlaku bolo {cestujuci - nastupili + vystupili} ľudí, "
#           f"{nastupili} nastúpilo, {vystupili} vystúpilo. Zostalo {cestujuci}.")


# import random

# n = int(input("zadaj n: "))
# pocet_kociek = int(input("zadaj počet kociek: "))

# for i in range(n):
#     sucet = 0
#     for k in range(1, pocet_kociek + 1):
#         hodnota = random.randint(1, 6)
#         sucet += hodnota
#         print(f"na {k}. kocke padla {hodnota}")
#     print(f"ich súčet je {sucet}")
#     print("=================")


# n = int(input("zadaj číslo: "))
# postupnost = [n]

# while n != 1:
#     if n % 2 == 0:
#         n = n // 2
#     else:
#         n = 3 * n + 1
#     postupnost.append(n)

# print(", ".join(str(x) for x in postupnost))


# def obdĺznik(sirka, znak='*'):
#     print(znak * sirka)
#     print(znak + " " * (sirka - 2) + znak)
#     print(znak * sirka)

# obdĺznik(30, '#')
# obdĺznik(6)
# obdĺznik(19, 'O')


# def vyhod_medzery(text):
#     return text.replace(" ", "")

# print(vyhod_medzery(' mám rád Python '))
# print(vyhod_medzery(' '))


# n = int(input("Zadajte n: "))

# vektory = []
# for i in range(n):
#     vektor = [int(input(f"Zadajte {j+1}. súradnicu {i+1}. vektora: ")) for j in range(n)]
#     vektory.append(vektor)

# for i in range(n):
#     zoradene = sorted(vektory, key=lambda v: v[i])
#     print(f"Podľa {i+1}.:", end=" ")
#     for v in zoradene:
#         print(", ".join(str(x) for x in v), end=", ")
#     print()

