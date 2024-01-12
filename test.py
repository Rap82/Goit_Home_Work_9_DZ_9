def interval_generator(x, y):
    while x <= y:
        yield x
        print (x)
        x += 1


five_to_ten_generator = interval_generator(5, 10)
print(five_to_ten_generator)
for i in five_to_ten_generator:
    print(i)