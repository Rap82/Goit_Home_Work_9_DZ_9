# ===================  Home work 9 ========================
# =================    Функції (декоратори, замикання)  =================

    # 1. Функція як об'єкт першого класу
    # 2. Області видимості (LEGB)
    # 3. ЗАМИКАННЯ
    # 4.  КАРРУВАННЯ
    # 5. Декоратори
    # 6. Ітератори/генератори (ключове слово yield)
    # 7. Лямбда-функції (анонімні функції)
    # 8. MAP
    # 9. Filter

# ================================================================


# ================================ Звдання 1 / Task 1 ======================================

#  # ================================ Функція як обєкт першого класу . Виклик функції з іншої функції. ======================================

# Wikipedia

# У програмуванні функція, яка приймає як аргументи інші функції або повертає іншу функцію в якості результату.
# Основна ідея у тому, що функції мають той самий статус, як і інші об'єкти даних.

# Оскільки у Python функції – це об'єкти першого класу, то вони є HOF (High Order Functions), 
# ця властивість активно використовується для розробки програмного забезпечення.

# На практиці це означає, що ми можемо працювати з функціями у Python точно так, як з будь-якими іншими типами даних:

# можемо створювати змінні і записувати в них функції;

#   def func(x, y):
#       return x + y

#   func_alias = func
#   result = func_alias(2, 3)
#   print(result)  # 5
# можемо передавати функцію як аргументи для інших функцій;

#   def sum_func(x, y):
#       return x + y

#   def subtraction_func(x, y):
#       return x - y

#   def tricky_func(x, y, func):
#       return func(x, y)

#   sum_result = tricky_func(2, 3, sum_func)
#   min_result = tricky_func(2, 3, subtraction_func)

#   print(sum_result)  # 5
#   print(min_result)  # -1
# можемо повертати з функції інші функції.

#   def sum_func(x, y):
#       return x + y

#   def subtraction_func(x, y):
#       return x - y

#   def get_operator(operator):
#       if operator == '+':
#           return sum_func
#       elif operator == '-':
#           return subtraction_func
#       else:
#           print('Unknown operator')

#   sum_action_function = get_operator("+")
#   print(sum_action_function(2, 3))    # 5

#   sub_action_function = get_operator("-")
#   print(sub_action_function(2, 3))    # -1
# Таким чином з функціями у Python можна працювати так само, як і з будь-якими іншими об'єктами.


# ++++++++++++++++++++++++++++++++++++++Умова / Condition ++++++++++++++++++++++++++++++++++++++++

# Повернемося до завдання про систему оцінок в університеті, які мають такий вигляд:

# Оцінка	Бали	Оцінка ECTS	    Пояснення

# 1	    0-34	    F	       Unsatisfactorily
# 2	    35-59	    FX	       Unsatisfactorily
# 3	    60-66	    E	       Enough
# 3	    67-74	    D	       Satisfactorily
# 4	    75-89	    C	       Good
# 5	    90-95	    В	       Very good
# 5	    96-100	    A	       Perfectly

# Минулого разу ми реалізували дві функції. Перша - get_grade, 
# приймає ключ в оцінці ECTS і повертає відповідну п'ятибальну оцінку (перший стовпчик таблиці).
# Друга - get_description, теж приймає ключ у оцінки ECTS, але повертає пояснення оцінки у текстовому форматі (останній стовпчик таблиці).
# На неіснуючий ключ функції повинні повертати значення None.

# Реалізуйте функцію вищого порядку get_student_grade, яка приймає параметр option. Якщо він дорівнює значенням "grade", 
# то функція повертає функцію get_grade, а якщо його значення дорівнює "description", то повертає функцію get_description. 
# Якщо параметр за значенням не співпав із заданими, то функція get_student_grade повинна повертати значення None.

# ++++++++++++++++++++ Код / Code ++++++++++++++++++++++++++++++++++++

# def get_grade(key):
#     ''' Функція за ключем *key , повертає значення з словника *grade.\
#         якщо вказати невіриний ключ поверне заначення *None.'''
#     grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
#     return grade.get(key, None)


# def get_description(key):
#     ''' Функція за ключем *key , повертає значення з словника *description.\
#         якщо вказати невіриний ключ поверне заначення *None.'''
#     description = {
#         "A": "Perfectly",
#         "B": "Very good",
#         "C": "Good",
#         "D": "Satisfactorily",
#         "E": "Enough",
#         "FX": "Unsatisfactorily",
#         "F": "Unsatisfactorily",
#     }
#     return description.get(key, None)

# def get_student_grade(option):
#     '''Функція приймає один аргумент *option, і якщо він містить змінні *get_description або *get_grade, \
#     то повертає відповідні функції за іменем оголошених функції після  оператора def *імя_функції(*аргументи_або_без_аргументів).\
#         Якщо аргументи, в оголошених функціях, відсутні в тілі коду обо повертати з основної функції тільки імя додаькової функції,\
#               то повертає клас *<function *імя_функції at *область_памяті_OS> на який вказує *optionю \
#                 Якщо аргумент оголошений в коді, і, в основновній функції повертає фінкцію, а не тільки їмя, то поверне результат отриманий з додаткової функції '''
 
#     if option == get_description: # Перевірка чи *option = get_description
#         return get_description    # якщо виконалась умова *if option == get_description - поверне *<function get_description at 0x000001B3B7327F60>
    
#     elif option == get_grade:     # Перевірка чи *option = get_grade
#         return get_grade          # якщо виконалась умова *elif option == get_grade - поверне *<function get_grade at 0x000001CB0CBF8A40>
#     else:
#        return None                # Поверне *None якщо жодна з попередніх умов невиконається .


# # key = "A" # Тестове значення.    
# # option = get_description # Тестове значення  # *<function get_description at 0x000001B3B7327F60>
# # option = get_grade  # Тестове значення  #  *<function get_grade at 0x000001CB0CBF8A40>
# # option = "asd"  # Тестове значення # *None

# # print(get_student_grade(option)) 

# +++++++++++++++++++++++ Для автоперевіки Код буде наступний +++++++++++++++++

# def get_student_grade(option):
    
#    if option == "description":
       
#        return get_description
   
#    elif option == "grade": 
#        return get_grade
#    else:
#        return None
   
# ================================ Звдання 2 / Task 2 ======================================







  

