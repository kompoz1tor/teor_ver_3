'''
3. На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень. Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6. 
Найти вероятность того, что выстрел произведен:
a) первым спортсменом;
б) вторым спортсменом;
в) третьим спортсменом.
'''
B=1/3
S=B*0.9+B*0.8+B*0.6
summary = round(S, 4)
print(f'Полная вероятность наступления события А Р(А) = {summary}')

P1=round(B*0.9/S, 4)
P2=round(B*0.8/S, 4)
P3=round(B*0.6/S, 4)

print(f'Вероятность того, что выстрел произвёл первый спортсмен: {P1};\n'
      f'Вероятность того, что выстрел произвёл второй спортсмен: {P2};\n'
      f'Вероятность того, что выстрел произвёл третий спортсмен: {P3}.'
     )