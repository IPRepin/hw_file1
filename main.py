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

