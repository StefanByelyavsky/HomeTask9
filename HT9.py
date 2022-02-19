import random
lst = [random.randint(1, 100) for i in range(random.randint(3, 10))]
print(lst)
lst_a = []
lst_a.append(lst[0])
lst_a.append(lst[2])
lst_a.append(lst[-2])
print(lst_a)