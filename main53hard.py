#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols =int(input(f"How many symbols would you like?\n"))
nr_numbers =int(input(f"How many numbers would you like?\n"))

password = ""
for car in range(1, nr_letters +1): # pega o numero de letras escohlido pelo usuário para gerar quantas vezes o loop será feito: Ex. 4? de 1 ao numero escolhido +1 = 4(0,1,2,3,4)
    password += random.choice(letters) # variavel password recebe e acrescenta (+=) uma letra aleatoria da lista(randon.choice) em cada loop.

for car in range(1, nr_symbols  +1):
    password += random.choice(symbols)

for car in range(1, nr_numbers +1):
    password += random.choice(numbers)

#print(password)# importante = imprmi fora do loop para pegar a variavel somada.

pass_hard = ""
hard = list(password)
#print(hard)

random.shuffle(hard)
py_password = ""
for letra in hard:
    py_password += letra
#print(py_password)

print(f"Here is your password: {py_password}")
print(f"Aqui está a sua senha: {py_password}")