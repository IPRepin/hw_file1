import os

def recipes_list():
	with open ('recipes.txt', 'r', encoding='utf-8') as recipes_list:
		for line in recipes_list:
			dish = line.strip()
			count_ingridients = recipes_list.readline()
			my_list = []
			for i in range(int(count_ingridients)):
				ingridients = recipes_list.readline()
				ingredient_name, quantity, measure = ingridients.split(' | ')
				all_ingridients = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure.strip()}
				my_list.append(all_ingridients)
				cook_book[dish] = my_list
			recipes_list.readline()


def get_shop_list_by_dishes(dishes, person_count):
	ingridients_dict = {}
	for dish in dishes:
		if dish in cook_book:
			for ingridients in cook_book[dish]:
				quantity_dict = {}
				if ingridients['ingredient_name'] not in ingridients_dict:
					quantity_dict['measure'] = ingridients['measure']
					quantity_dict['quantity'] = int(ingridients['quantity']) * person_count
					ingridients_dict[ingridients['ingredient_name']] = quantity_dict
				else:
					ingridients_dict[ingridients['ingredient_name']]['quantity'] = ingridients_dict[ingridients['ingredient_name']]['quantity'] + \
					 int(ingridients['quantity']) * person_count
		else:
			print('Такого блюда нет!')
	return print(ingridients_dict)

cook_book = {}
recipes_list()
get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)

def sorted_files_by_len_strings():
	'''This function creates file 'result.txt' with sorted strings by ascending from another 3 txt files and name each txt file and len strings'''
	with open ('1.txt', 'r', encoding='utf-8') as file1:
		file1_full = file1.read()
		file1.seek(0)
		file1_list = file1.readlines()
		path1 = '1.txt'
		name1 = os.path.basename(os.path.join(os.getcwd(), path1))
		len1 = str(len(file1_list))
	with open ('2.txt', 'r', encoding='utf-8') as file2:
		file2_full = file2.read()
		file2.seek(0)
		file2_list = file2.readlines()
		path2 = '2.txt'
		name2 = os.path.basename(os.path.join(os.getcwd(), path2))
		len2 = str(len(file2_list))
	with open ('3.txt', 'r', encoding='utf-8') as file3:
		file3_full = file3.read()
		file3.seek(0)
		file3_list = file3.readlines()
		path3 = '3.txt'
		name3 = os.path.basename(os.path.join(os.getcwd(), path3))
		len3 = str(len(file3_list))
	with open ('result.txt', 'w', encoding='utf-8') as result_file:
		if min(len1, len2, len3) == len1:
			result_file.write(name1 + '\n' + len1 + '\n')
			result_file.write(file1_full + '\n')
			if min(len2, len3) == len2:
				result_file.write(name2 + '\n' + len2 + '\n')
				result_file.write(file2_full + '\n')
				result_file.write(name3 + '\n' + len3 + '\n')
				result_file.write(file3_full + '\n')
			else:
				result_file.write(name3 + '\n' + len3 + '\n')
				result_file.write(file3_full + '\n')
				result_file.write(name2 + '\n' + len2 + '\n')
				result_file.write(file2_full + '\n')
		elif min(len1, len2, len3) == len2:
			result_file.write(name2 + '\n' + len2 + '\n')
			result_file.write(file2_full + '\n')
			if min(len1, len3) == len1:
				result_file.write(name1 + '\n' + len1 + '\n')
				result_file.write(file1_full + '\n')
				result_file.write(name3 + '\n' + len3 + '\n')
				result_file.write(file3_full + '\n')
			else:
				result_file.write(name3 + '\n' + len3 + '\n')
				result_file.write(file3_full + '\n')
				result_file.write(name1 + '\n' + len1 + '\n')
				result_file.write(file1_full + '\n')
		else:
			result_file.write(name3 + '\n' + len3 + '\n')
			result_file.write(file3_full + '\n')
			if min(len1, len2) == len1:
				result_file.write(name1 + '\n' + len1 + '\n')
				result_file.write(file1_full + '\n')
				result_file.write(name2 + '\n' + len2 + '\n')
				result_file.write(file2_full + '\n')
			else:
				result_file.write(name2 + '\n' + len2 + '\n')
				result_file.write(file2_full + '\n')
				result_file.write(name1 + '\n' + len1 + '\n')
				result_file.write(file1_full + '\n')

sorted_files_by_len_strings()