import time
class bubble_sort:
    def __init__(self):
        return
    
    def sort(self, sample):
        sample_len = len(sample)
        for i in range(sample_len):
            for j in range(sample_len - 1):
                
                if sample[j + 1] < sample[j]:
                    temp = sample[j + 1]
                    sample[j + 1] = sample[j]
                    sample[j] = temp

    def print_original(self, number):
        print("\n==================================================")
        print("Original")
        print("==================================================\n")
        for i in range(len(number)):
          if i + 1 == len(number):
               print(f"{number[i]}]")
          elif i == 0:
               print(f"[{number[i]}, ",end="")
          else:
               print(number[i],end=", ")  


    def print(self, sample, time):
        print("\n==================================================")
        print("Sorted Output")
        print("==================================================\n")
        for i in range(len(sample)):
            if i == 0:
                print(f"[{sample[i]}, ",end="")
            elif i + 1 == len(sample):
                print(f"{sample[i]}]",end="\n")
            else:
                print(sample[i],end= ", ")
        print("\n==================================================")
        print("Bubble Sort Result:")
        print(f"Size of array = {len(sample)}")
        print(f"Time taken = {time:.6f} seconds")
        print
        print("==================================================\n")
                        




            