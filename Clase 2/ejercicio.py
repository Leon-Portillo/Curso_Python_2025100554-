n1= int(input("Ingrese el primer numero: "))
n2= int(input ("Ingrese el segund numero: "))

if ((n1%2 ==0) and (n2%2 ==0)):
    print("Ambos numeros son pares")
elif ((n1%2 ==0) and (n2%2 !=0)):
    print (f"{n1} es par")
    print (f"{n2} es impar")
elif ((n1%2 !=0) and (n2%2 ==0)):
    print (f"{n1} es impar")
    print (f"{n2} es par")
else: 
    print("los dos numeros son impares")