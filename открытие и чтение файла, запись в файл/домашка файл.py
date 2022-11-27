
with open('recipes.txt', 'rt', encoding='utf-8') as file:
   cook_book = { }
   for line in file:
       name_dich = line.strip()
       number_ingredient = int(file.readline())
       ingredient_name = [ ]
       for _ in range(number_ingredient):
           ing = file.readline().strip().split(' | ')
           name, quantity, measure = ing
           ingredient_name.append({'ingredient_name': name, 'quantity': int(quantity), 'measure': measure})
       file.readline()
       cook_book.update({name_dich : ingredient_name})

for key,value in cook_book.items():
    print(f' {key}: {value}')

print('*'*73)

def get_shop_list_by_dishes(dishes, person_count):
    ing_shop_list = { }
    for name_dich, ingredient in cook_book.items():
        if name_dich in dishes:

                for elem in ingredient:
                     a = elem.get('ingredient_name')
                     name_ing = elem.pop('ingredient_name')

                     if a not in ing_shop_list.keys():
                         ing_shop_list[a] = elem

                     else:
                         ing_shop_list[a]['quantity'] += elem['quantity']
                         ing_shop_list[a]['quantity'] *= person_count

    print(f'Список продуктов для приготовления {dishes} на {person_count} человек:', ing_shop_list)

get_shop_list_by_dishes(['Фахитос', 'Омлет'], 3)

print('*'*73)


c={}

with open('1.txt','rt', encoding='utf-8') as file_:
    b_count = file_.readlines()
    c [len(b_count), file_.name] = b_count

with open('2.txt', 'rt', encoding='utf-8') as file_:
    b_count = file_.readlines()
    c[len(b_count), file_.name] = b_count

with open('3.txt', 'rt', encoding='utf-8') as file_:
    b_count = file_.readlines()
    c[len(b_count), file_.name] = b_count


with open('10.txt', 'w', encoding='utf-8') as file_:
    for k, v in sorted(c.items()):
        file_.write(f'{k[1]}\n'
                    f'{k[0]}\n'
                    f'{"".join(v)}\n')


