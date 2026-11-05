basket1 = {'apple', 'banana', 'apple', 'mango', 'grape'}
basket2 = {'mango', 'kiwi', 'banana', 'kiwi'}
print("Basket 1: ", basket1)
print("Basket 2: ", basket2)

basket1.add('orange')
print("Basket 1 after adding element/fruit orange: ", basket1)

common_fruits = basket1.intersection(basket2)
print("Common fruits in both baskets are: ", common_fruits)

import array as ar
number_of_fruits = ar.array('i', [3, 5, 6, 2])
print("Number of fruits in basket 1: ", number_of_fruits)

number_of_fruits.insert(0, 9)
print("Number of fruits after adding 9 in index 0: ", number_of_fruits)
number_of_fruits.append(8)
print("Number of fruits after adding 8 more: ", number_of_fruits)

print(number_of_fruits.count(5))
reverse_array = number_of_fruits.reverse()
print(reverse_array)