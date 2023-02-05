import typing

from functions import *


def print_function_result(func, *args) -> None:
    result = func(*args)
    args_str = ', '.join(map(str, args))
    print(f"{func.__name__}({args_str}) = {result}")


print_function_result(solve, 35, 94)
print_function_result(has_33, [1, 3, 3])
print_function_result(has_33, [1, 3, 1, 3])
print_function_result(has_33, [3, 1, 3])
print_function_result(spy_game, [1, 2, 4, 0, 0, 7, 5])
print_function_result(spy_game, [1, 0, 2, 4, 0, 5, 7])
print_function_result(spy_game, [1, 7, 2, 0, 4, 5, 0])
print_function_result(sphere_volume, 10)
print_function_result(unique_list, [1, 2, 3, 2, 1])
print_function_result(is_palindrome, 'kbtu')
print_function_result(is_palindrome, 'kbtutbk')
print_function_result(histogram, [4, 9, 7])
print_function_result(guess_the_number)
