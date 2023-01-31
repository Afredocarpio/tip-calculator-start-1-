#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Bienvenido a la calculadora de propinas")
total_pagar = input("Cual es el total a pagar?: ")
personas = input("Entre cuantas personas se divide la cuenta: ")
propina = input("desea dar una propina del 10, 12 o 15 %: ")

result = float(total_pagar) * (int(propina) / 100)
result = (float(total_pagar) + result) / int(personas)
#print(f"total a pagar ${round(result)}")
#dar formato a la cadena con dos decimales
print("{:.2f}".format(result))