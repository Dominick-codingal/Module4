print("=====creating 2 sets=====")
basket1 = {"apple", "banana","mango", "apple", "grapes"}
basket2 = {"kiwi", "kiwi","mango", "cucumber", "grapes", "pineapple","papaya"}

print("Basket 1: ",basket1)
print("Basket 2: ",basket2)


print("\n=====Adding a new fruit to a basket=====")
basket1.add("Mandarin")
print("Basket 1 after adding 'Mandarin' : ",basket1)

print("\n=====common fruits in both baskets=====")

common_fruits = basket1.intersection(basket2)
print("Common fruits in both baskets: ", common_fruits)

print("\n=====creating an array=====")
import array as arr
fruits_count= arr.array('i', [4, 5, 8, 3, 3,2])
print("Fruits counts array:", fruits_count)