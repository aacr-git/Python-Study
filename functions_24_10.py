"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""


nums = [4,5,6,2]


def find_fs (nums):
    nums = [5,5,6,5]
    suma = 0
    for index, numbers in enumerate(nums):
        for indexes, numeritos in enumerate(nums):
            suma = numbers + numeritos
            if suma == 8:
                print(f" [{index}, {indexes}]")
                break
        else:
            print("None")
                
        break


find_fs(nums)
