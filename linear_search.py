'''
	Линейный пойск - базовый алгоритм пойска который ищет все 
	элементы в списке и находит требуемое значение.
'''


def linear_search(list):
	'''Функция линейного пойска'''

	list = [4, 8, 16, 32, 64, 128, 256]
	target = int(input('Введите цель: '))
	for i in range(len(list)):
		if list[i] == target:
			return i
	return -1


print(linear_search(list))

