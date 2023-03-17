sal = float(input("Salário: "))

if sal <= 1302:
    inss = sal * 0.075
elif sal <= 2572.29:
    inss = sal * 0.09
elif sal <= 3856.94:
    inss = sal * 0.12
elif sal <= 7507.49:
    inss = sal * 0.14
else:
    inss = 1051.05

sal_lig = sal - inss

print(f"""
    Salario..............: R$ {sal : 9.2f}
    INSS.................: R$ {inss: 9.2f}
    Salário Liquido......: R$ {sal_lig: 9.2f}
""")
    

