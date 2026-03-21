class selection_sort:
    def __init__(self):
        return
    
    #[3, 4, 1, 2]
    #[1, 4, 3, 2]
    #[1, 2, 3, 4]
    def sort(self, numbers):
        number_len = len(numbers)
        for i in range(number_len):
            found = False
            smallest = numbers[i]
            for j in range(i, number_len):
                
                if numbers[j] < smallest:
                    found = True
                    smallest = numbers[j]
                    index = j
            if found == True:
                temp = numbers[i]
                numbers[i] = smallest
                numbers[index] = temp

    def print_original(self, number):
        print("==================================================")
        print("Original")
        print("==================================================")
        for i in range(len(number)):
          if i + 1 == len(number):
               print(f"{number[i]}]")
          elif i == 0:
               print(f"[{number[i]}, ",end="")
          else:
               print(number[i],end=", ")        
            

    def print(self, numbers, time):
        print("==================================================")
        print("Selection Sort Output")
        print("==================================================")
        for i in range(len(numbers)):
            if i + 1 == len(numbers):
                print(f"{numbers[i]}]")
            elif i == 0:
                print(f"[{numbers[i]}, ",end="")
            else:
                print(f"{numbers[i]}, ",end="")
        print(f"Time taken = {time:.6f} seconds")
        print("==================================================")
