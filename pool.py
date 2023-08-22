import random
import csv

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

    #pull in football schedule csv - columns are: date,home,away
    with open("schedule.csv") as schedule_file:
        schedule_list = csv.reader(schedule_file, delimiter=',')
        #loop over each row
        for row in schedule_list:
            date = row[0]
            home = row[1]
            away = row[2]
            
            #generate numbers for home
            home_numbers = generate_football_pool_numbers(num_numbers, min_number, max_number)
            #generate numbers for away
            away_numbers = generate_football_pool_numbers(num_numbers, min_number, max_number)
            #clone pool template csv
            #insert numbers generated
            #save to new csv main-team-name-date.csv
            print(date)
            print(home)
            print(away)
            print("away numbers:")
            print(', '.join(map(str,away_numbers)))
if __name__ == "__main__":
    main()

