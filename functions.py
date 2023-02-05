import math
import random
import itertools


# 1
def convert_grams_to_ounces(grams: float) -> float:
    ounces: float = 28.3495231 * grams
    return ounces


# 2
def fahrenheit_to_celsius(f: float) -> float:
    c: float = (5 / 9) * (f - 32)
    return c


# 3
def solve(numheads: int, numlegs: int) -> tuple:
    for chickens in range(0, numheads + 1):
        rabbits = numheads - chickens
        if numlegs == (chickens * 2 + rabbits * 4):
            return chickens, rabbits
    return 0, 0


# 4
def filter_prime(numbers: list) -> list:
    if_prime = lambda x: all(x % i != 0 for i in range(2, x))
    result_it = filter(if_prime, numbers)
    result_list = list(result_it)
    return result_list


# 5
def permutations(string: str) -> None:
    print([x for x in itertools.permutations(string, len(string))])


# 6
def reverse_words(sentence: str) -> str:
    reversed_words: list = reversed(sentence.split())
    return " ".join(reversed_words)


# 7
def has_33(nums: list) -> bool:
    for i in range(len(nums) - 1):
        if nums[i:i + 2] == [3, 3]:
            return True
    return False


# 8
def spy_game(nums: list) -> bool:
    nums = sorted(nums, key=lambda x: x == 0)
    return nums[:3] == [0, 0, 7]


# 9
def sphere_volume(radius: float) -> float:
    return (4 / 3) * (math.pi * (radius ** 3))


# 10
def unique_list(numbers: list) -> list:
    result = []
    for num in numbers:
        if num not in result:
            result.append(num)
    return result


# 11
def is_palindrome(string: str) -> bool:
    return string == string[::-1]


# 12
def histogram(numbers: list) -> None:
    for num in numbers:
        print('*' * num)


# 13
def guess_the_number() -> None:
    name: str = input("Hello! What is your name? ")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    secret_number: int = random.randint(1, 20)
    i: int = 1
    while True:
        print("Take a guess.")
        guess: int = int(input())
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            break
        i += 1
    print(f"Good job, {name}! You guessed my number in {i} guesses!")
    return
