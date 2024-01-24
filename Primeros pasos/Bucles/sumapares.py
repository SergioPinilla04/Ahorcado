sumtotal1 = 0
sumtotal2 = 0
for contador in range(2, 100, 2):
    sumtotal1 = sumtotal1 + contador
for contador in range(1, 100, 2):
    sumtotal2 = sumtotal2 + contador
print("Total pares: ", sumtotal1, "Total impares: ", sumtotal2)