stuper = input ('выберите операцию (введите "+", "-", "/")')
if stuper == '+':
    print('вы выбрали сумму:')
elif stuper == '-':
    print('вы выбрали разность:')
elif stuper == '*':
    print('вы выбрали умножение:')
else:
    stuper == '/'
    print('вы выбрали деление:')

# сумма
def summa (first, second):
    return first + second 
# вычитание
def sub (first, second):
    return first - second
# умножение 
def multi (first, second):
    return first * second
# ДЕЛЕНИЕ 
def div (first, second):
    return first / second


num1 = int(input('введите первое число ='))
num2 = int(input('Введите второе число ='))
print(f'сумма:{summa(num1, num2)}, вычитание: {sub(num1, num2)}, умножение: {multi(num1, num2)}, деление: {div(num1, num2)}')