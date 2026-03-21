from Bubble_sort import bubble_sort
from Selection_sort import selection_sort
from Merge_sort import merge_sort
import time
import os
def main():
    #python3 src/Main.py
    while True:
        print("==================================================")
        print("Sorting")
        print("==================================================")
        print("[1] Bubble Sort With File")
        print("[2] Bubble Sort With Array")
        print("[3] Selection Sort With File")
        print("[4] Selection Sort With Array")
        print("[5] Merge Sort With Array")
        print("[6] Merge Sort With File")
        print("[-1] Exit")
        print("==================================================")

        user_input = input("Select Option: ")
        if user_input == "1":
             file = get_file()
             bubblesort_file(file)
        elif user_input == "2":
             bubblesort()
        elif user_input == "3":
             file = get_file()
             selectionsort_file(file)
        elif user_input == "4":
             selectionsort()
        elif user_input == "5":
             mergesort()
        elif user_input == "6":
             file = get_file()
             mergesort_file(file)
        elif user_input == "-1":
             exit()
def mergesort():
     algorithm = merge_sort()

     numbers = get_array()
     algorithm.print_original(numbers)
     start_time = time.time()
     result = algorithm.sort(numbers)
     end_time = time.time()
     time_taken = end_time - start_time
     algorithm.print(result, time_taken)

def mergesort_file(file):
     try:
          with open(file) as f:
               numbers_str = f.readlines()
     except FileNotFoundError:
          print("File does not exist")
          return
     numbers = [int(number) for number in numbers_str]
     algorithm = merge_sort()
     algorithm.print_original(numbers)
     start_time = time.time()
     result = algorithm.sort(numbers)
     end_time = time.time()
     time_taken = end_time - start_time
     algorithm.print(result, time_taken)
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

def list_files():
     folder = os.path.join(os.path.dirname(__file__), "..", "tests")
     file = os.listdir(folder)
     in_files = [f for f in file if f.endswith(".in")]
     print("==================================================")
     print("Test Files:")
     print("==================================================")
     for f in in_files:
          print(f)
     print("==================================================")
def get_file():
     list_files()
     file = input("Enter File Name: ")
     return os.path.join("tests", file)

def selectionsort():
     algorithm = selection_sort()
     numbers = get_array()
     algorithm.print_original(numbers)
     start = time.time()
     algorithm.sort(numbers)
     end = time.time()
     algorithm.print(numbers, end - start)

def selectionsort_file(file):
     try:
          with open(file) as f:
               numbers_str = f.readlines()
     except FileNotFoundError:
          print("File does not exist")
          return
     algorithm = selection_sort()
     time_taken = 0
     numbers = [int(number) for number in numbers_str]
     algorithm.print_original(numbers)
     start_time = time.time()
     algorithm.sort(numbers)
     end_time = time.time()

     time_taken = end_time - start_time
     algorithm.print(numbers, time_taken)

def bubblesort():
     algorithm = bubble_sort()
     numbers = get_array()
     algorithm.print_original(numbers)

     time_taken = 0

     start_time = time.time()
     algorithm.sort(numbers)
     end_time = time.time()
    
     time_taken = end_time - start_time
     algorithm.print(numbers, time_taken)

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