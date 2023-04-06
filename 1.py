"""
Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150. 
Посчитать (желательно без использования статистических методов наподобие std, var, mean) среднее арифметическое, среднее квадратичное отклонение, 
смещенную и несмещенную оценки дисперсий для данной выборки.
"""
import numpy as np

arr = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])

#среднее арифмитическое
def arithmetic_mean(array):
    return sum(array)/len(array)

result1 = arithmetic_mean(arr)
print(f"среднее арифмитическое: {result1}")

#среднее квадратичное отклонение
def mean_square_deviation(array):
    square_dev=(array-arithmetic_mean(array))**2
    return (sum(square_dev)/len(square_dev))**(1/2)

result2 = mean_square_deviation(arr)
print(f"cреднее квадратичное отклонение: {result2}")

#смещенная и несмещенная оценка дисперсий
def dispers(array, biased_variance=False):
    square_dev=(array-arithmetic_mean(array))**2
    return sum(square_dev)/(len(square_dev)-1) if biased_variance else sum(square_dev)/len(square_dev)

#смещенная
result3 = dispers(arr)
#несмещенная
result4 = dispers(arr, True)

print(f"Смещенная дисперсия {result3}; Несмещенная дисперсия {result4}")