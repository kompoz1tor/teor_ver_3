'''
В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых. 
Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. Какова вероятность того, что 3 мяча белые?
'''
from math import factorial
def combinations(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))

P1=(combinations(3,2)/combinations(8,2))*(combinations(5,3)*combinations(7,1)/combinations(12,4))
print(f'Вероятность события "из первой корзины не вытащили ни одного белого мяча, из второй вытащили 3 белых мяча" = {P1}')

P2=(combinations(5,1)*combinations(3,1)*combinations(5,2)*combinations(7,2))/(combinations(8,2)*combinations(12,4))
print(f'Вероятность события "из первой корзины вытащили 1 белый мяч, из второй вытащили 2 белых мяча" = {P2}')

P3=(combinations(5,2)*combinations(5,1)*combinations(7,3))/(combinations(8,2)*combinations(12,4))
print(f'Вероятность события "из первой корзины вытащили 2 белых мяча, из второй вытащили 1 белый мяч" = {P3}')

print(f'Вероятность того, что из вытащенных мячей 3 белые  = {P1+P2+P3}')