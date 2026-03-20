from Bubble_sort import bubble_sort
import time
import os
def main():

    while True:
        print("==================================================")
        print("Sorting")
        print("==================================================")
        print("[1] Bubble Sort With File")
        print("[2] Bubble Sort With Array")
        print("[-1] Exit")
        print("==================================================")

        user_input = input("Select Option: ")
        if user_input == "1":
             file = get_file()
             print(file)
             bubblesort_file(file)
        elif user_input == "2":
             bubblesort()
             
        elif user_input == "-1":
             exit()

def get_array():
     numbers = []
     while True:
          print("\n==================================================")
          print("[1] Add Numbers")
          print("[2] Remove Number")    
          print("[3] Done")
          print("[4] Show")
          print("==================================================") 
          user_input = input("Select Option: ")
          if user_input == "1":
            print("==================================================") 
            add = int(input("Enter Number: "))
            print("==================================================") 
            if isinstance(add, int):
                numbers.append(add)
                print(f"{add} is added\n")
                continue
            else:
                print("Please enter an integer")
                continue
          elif user_input == "2":
            print("==================================================") 
            for i in numbers:
                 print(i,end=" ")        
            add = int(input("Enter index to delete: "))
            print("==================================================")  
          elif user_input == "3":
               return numbers  
          elif user_input == "4":
            for i in numbers:
                 print(i,end=" ")


def get_file():
     file = input("Enter File Name: ")
     return os.path.join("tests", file)

def bubblesort():
     numbers = get_array()
def bubblesort_file(file):
        algorithm = bubble_sort()
        try:
             with open(file) as f:
                  numbers_str = f.readlines()
        except FileNotFoundError:
             print("File does not exist")
             return
        numbers = [int(number) for number in numbers_str]
        algorithm.print_original(numbers)

        time_taken = 0

        start_time = time.time()
        algorithm.sort(numbers)
        end_time = time.time()
    
        time_taken = end_time - start_time
        algorithm.print(numbers, time_taken)
if __name__ == "__main__":
    main()