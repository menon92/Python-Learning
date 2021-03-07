'''
Does python call by value or referance ? 

Python is call by object refence
'''

__version__ = "0.0.1"
__author__ = "@menon"


import json


def get_even_numbers(numbers):
  numbers = [num for num in numbers if num % 2 == 0]


def do_change_in_list(numbers):
  numbers[0] = 100000


def do_change_in_dictionary(products):
  product['Apple'] = 100


def do_change_in_tuple(numbers):
  try:
    numbers[0] = -1
  except Exception:
   print(f"Object of type: {type(numbers)} does not mutable")


if __name__ == "__main__":
  numbers = [1, 2, 3, 4, 5, 6]
  get_even_numbers(numbers)
  print(f"Numbers: {numbers}")

  # print(locals())
  # print(globals())

  print("List objest does not modify")
  print("-" * 50)

  product = {"Apple": 200, "Orange": 300}

  print(f"Product before changes: {product}")
  print("-" * 50)

  do_change_in_dictionary(product)
  print(f"Product: {product}")
  print(f"Product type: {type(product)}")

  print("-" * 50)

  with open('product.json', 'w') as fp:
    json.dump(product, fp, indent=2, ensure_ascii=False)

  with open('product.json', 'r') as fp:
    product = json.load(fp)

  do_change_in_dictionary(product)
  print(f"Product: {product}")
  print(f"Product type: {type(product)}")

  print("-" * 50)

  print(f"Before making change in list: {numbers}")

  print("-" * 50)
  do_change_in_list(numbers)
  print(f"After making change in list: {numbers}")

  numbers_tuple = tuple(numbers)
  do_change_in_tuple(numbers_tuple)
  print(f"After makign chage in tuple: {numbers_tuple}")

  print("-" * 50)
