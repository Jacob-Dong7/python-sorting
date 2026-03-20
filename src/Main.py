from Bubble_sort import bubble_sort
import time
import os
def main():
    while True:
        print("[1] Bubble Sort with File")
        print("[-1] Exit")

        user_input = input("Select Option")
        if user_input == 1:
             file_name = input("Enter the file name, example test1.in")
             bubblesort(file_name)
        elif user_input == -1:
             exit()

def bubblesort(file):
        try:
             with open(file) as f:
                  numbers_str = f.readlines()
        except FileNotFoundError:
             print("File does not exist")
             return
        time_taken = 0
        algorithm = bubble_sort()
        sample = [0, -10, 5, 3, 3, -1, 999, -1000, 50, 2, 2, 1, -10, 999, 7]
        start_time = time.time()
        algorithm.sort(sample)
        end_time = time.time()
        time_taken = end_time - start_time
        algorithm.print(sample, time_taken)
if __name__ == "__main__":
    main()