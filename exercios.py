sal = float(input("Salário: "))

if sal <= 1903.99:
    ir = sal * 0.075 - 142.80
elif sal <= 2826.66:
    ir = sal * 0.15 - 354.80
elif sal <= 3751.06:
    ir = sal * 0.225 - 636.13
elif sal >= 4664.68:
    ir = sal * 0.275 - 869.36

sal_liq = sal - ir

print(f"""
    Salario.......: {sal: 9.2f}
    ir............: {ir: 9.2f}
    sal_liq.......: {sal_liq: 9.2f}
""")
