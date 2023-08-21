import random

def generate_football_pool_numbers(num_numbers, min_number, max_number):
    if num_numbers > (max_number - min_number + 1):
        print("Error: Not enough numbers in the given range to generate that many unique numbers.")
        return []

    numbers = random.sample(range(min_number, max_number + 1), num_numbers)
    return numbers

def main():
    num_numbers = 10 
    min_number = 0
    max_number = 9

    pool_numbersA = generate_football_pool_numbers(num_numbers, min_number, max_number)
    pool_numbersB = generate_football_pool_numbers(num_numbers, min_number, max_number)

    print("Home Team:")
    print(pool_numbersA)

    print("Away Team:")
    print(pool_numbersB)

if __name__ == "__main__":
    main()

