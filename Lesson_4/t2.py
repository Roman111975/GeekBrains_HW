#2. Представлен список чисел. Необходимо вывести элементы
#исходного списка, значения которых больше предыдущего элемента.
#Подсказка: элементы, удовлетворяющие условию, оформить в виде
#списка. Для формирования списка использовать генератор.
#my_list = [1, 25, 3, 45, 50]
#print(my_list)
#new_list = [el for el my_list if my_list[el] > my_list[el-1]]
#print(new_list)
my_list = [1, 2, 3, 2, 1]
print(my_list)
new_list=[my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]
print(new_list)