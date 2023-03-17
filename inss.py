sal = float(input("Salário: "))

if sal >= 0 and sal <= 1302:
    inss = sal * 0.075

if sal > 1302 and sal <= 2572.29:
    inss = sal * 0.09

if sal > 2572.29 and sal <= 3856.94:
    inss = sal * 0.12

if sal > 3856.94 and sal <= 7507.49:
    inss = sal * 0.14

if sal > 7507.49:

