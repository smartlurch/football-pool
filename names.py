import random
import csv

def generate_football_pool_numbers(num_numbers, min_number, max_number):
    if num_numbers > (max_number - min_number + 1):
        print("Error: Not enough numbers in the given range to generate that many unique numbers.")
        return []

    numbers = random.sample(range(min_number, max_number + 1), num_numbers)
    return numbers

def main():
    num_numbers = 100 
    min_number = 0
    max_number = 99

    #pull in football schedule csv - columns are: date,home,away
            
            #generate numbers for home
    name_numbers = generate_football_pool_numbers(num_numbers, min_number, max_number)
            #generate numbers for away
            #clone pool template csv
            #insert numbers generated
            #save to new csv main-team-name-date.csv
#            print(date + ": " + home + " vs " + away)
            #print(home)
            #print(away)
 #           print(home + " numbers:")
  #          print(', '.join(map(str,home_numbers)))
   #         print(away + " numbers:")
    #        print(', '.join(map(str,away_numbers)))
    name_nums_merged = "\n".join(map(str,name_numbers)) 
    scoresFile = open("names.csv", "a")
    scoresFile.writelines(name_nums_merged)
    scoresFile.close()
if __name__ == "__main__":
    main()

