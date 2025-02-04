## numerosamigos



num1=int(input ("INgresa el primer numero:"))
num2=int(input ("INgresa el segundo numero:"))

suma1=0
suma2=0
for i in range (1 , num1):
    if (num1%i == 0):
        suma1 = suma1 + i

for i in range (1 , num2):
    if (num2%i == 0):
        suma2 = suma2 + i

if (suma1 == num2 and suma2 == num1):
    print ("Los numeros son bros!")
else:
    print("Los numeros no son bros :pipipipi: ")
