import os

def read_cook_book():
    with open('recipes.txt', 'rt', encoding='utf8') as reading_cook_book:
        for line in reading_cook_book:
            name_of_the_dish = line.strip()
            ingredients_count = reading_cook_book.readline()
            dishs = []
            for i in range(int(ingredients_count)):
                ingredient = reading_cook_book.readline()
                ingredient_name, quantity, measure = ingredient.split(' | ')
                ingredient_dict = {"ingredient_name": ingredient_name, "quantity": quantity, "measure": measure}
                dishs.append(ingredient_dict)

            cook_book[name_of_the_dish] = dishs
            reading_cook_book.readline()
        print(cook_book)


cook_book = {}
read_cook_book()


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
                    ingridients_dict[ingridients['ingredient_name']]['quantity'] = \
                    ingridients_dict[ingridients['ingredient_name']]['quantity'] + \
                    int(ingridients['quantity']) * person_count
        else:
            print('Такого блюда нет!')
    return print(ingridients_dict)

get_shop_list_by_dishes(['Утка по-пекински', "Омлет"], 3)

def sorted_files_by_len_strings():
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