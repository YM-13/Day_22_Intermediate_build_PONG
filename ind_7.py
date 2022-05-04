my_list = [7, 5, 3, 3, 2]

while True:
	chislo = int(input("Введите число: "))
	for n in my_list:
		if chislo > n or chislo == n:
			my_list.insert(my_list.index(n), chislo)
			break
		elif chislo < my_list[-1]:
			my_list.append(chislo)
			break


	print(my_list)
