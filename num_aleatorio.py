import random



print("Intenta adivinar el numero aleatorio generado por el pc")
print("pista el numero esta entre 0 y 100")
print()
#generamos un numero aleatorio entre 1 y 100
num_ale = random.randint(1,100)

#pedimos el numero al usuario
num_user = int(input("Digite un numero entre 0 y 100: "))

intentos = 1


#importante tener en cuenta lo que es la condicion
while num_ale != num_user:
    
    if num_ale > num_user:
        print("Digite un numero mayor ")
    else:
        print("digite un numero menor")
    #importante tener en cuenta el incrmento primro se escribe el signo ya sea suma resta o otro y luego va el igual
    intentos +=1
    num_user = int(input("Digite otro numero "))


if num_ale == num_user and intentos == 1:
    print("!!Genial adivinaste el numero en un solo intento")
else:
    print(f"!!Genial adivinaste el numero en {intentos} intentos")