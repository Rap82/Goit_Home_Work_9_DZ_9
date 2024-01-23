def interval_generator(x, y):
    while x <= y:
        yield x
        print (x)
        x += 1


five_to_ten_generator = interval_generator(5, 10)
print(five_to_ten_generator)
for i in five_to_ten_generator:
    print(i)


import re
def generator_numbers(string=""):
    result = re.search(r"\d+", string)
    while result:
        string = string[result.end():]
        yield int(result.group())
        result = re.search(r"\d+", string)

def sum_profit(string): # Більш правильний код оголошення функції *sum_profit(string) для  конкретного нашого випадку , але він недає повного розуміння переваг ітератора *yield
    summa = 0 
    mygenerator = generator_numbers(string) 
    for parser_str in mygenerator : 
        summa += parser_str 
    return summa 

# def sum_profit(string): Те саме оголошення тільки з можливість модифікацї проміжних результатів повернених з *generator_numbers(string)
#     summa = 0
#     parser_str = generator_numbers(string)
#     while True:
#         try:
#             number = next(parser_str)
#         except StopIteration:
#             return summa
#         else:
#             summa += number

