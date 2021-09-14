# import requests
import numpy as np

# print("Hello World")

# x = 10
# y = 11
# z = x + y

# print(f"Z je {z}")

# r = requests.get('https://www.geeksforgeeks.org')
# print(r)

# a = np.array([[7,8,5],[3,5,7]])
# print(a)

# a, b = 1, 2
# print("soucet je ", a + b)

# def reassign(lst):
#     lst = [0, 1]

# def append(lst):
#     lst.append(1)

# lst = [0]
# print(lst)
# reassign(lst)
# print(lst)
# append(lst)
# print(lst)

# map function
# def doubler(a):
#   return a * 2

# arr = np.linspace(1, 10, 10)
# arr2 = map(doubler, arr)

# print(arr)
# arr = list(arr)
# print(arr)
# print(arr[0:-1:2])
# print(arr[::2])


class Hrnek():
  def __init__(self, vyska, prumer):
    self.vyska = vyska
    self.prumer = prumer
    self.barva = ""


def obarvi_hrnek(hrnek):
  hrnek.barva = "zluta"
  print(hrnek)

def zvetsi_hrnek(hrnek):
  hrnek.vyska *= 2
  hrnek.prumer *= 3
  print(hrnek)


def vypocti_objem(h, d):
  h = 10
  objem = h * 3.14 * d / 4
  return objem

# ridici kod
# h1 = Hrnek(1,1)
# h2 = Hrnek(2,2)

# o1 = vypocti_objem(h1.vyska, h1.prumer)

h = 1
d = 1
o1 = vypocti_objem(h, d)
print(o1)

# obarvi_hrnek(h1)
# obarvi_hrnek(h2)

# zvetsi_hrnek(h1)
# zvetsi_hrnek(h2)