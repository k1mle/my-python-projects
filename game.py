import random

x = random.randint(1, 100)

attempts = 0

print("Я загадал чтсло от 1 до 100. Угадай!")

while True:

     attempts += 1

     a = int(input("Твой вариант: "))

     if a < x:

        print("Число больше!")


     elif a > x:

         print("Число меньше!")


     else :
         print (f"Молодец, ты угадал за {attempts} попыток!")
         break

     
