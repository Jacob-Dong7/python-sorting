class merge_sort:
    def __init__(self):
        return
    
    #[8, 3, 5, 2]
    #[8, 3]    [5, 2]
    #[8] [3]   [5] [2]
    #[3,8] [4, 9]
    def sort(self, numbers):
        numbers_len = len(numbers)
        if numbers_len <= 1:
            return numbers
        
        mid = int(numbers_len / 2)
        left = numbers[:mid]
        right = numbers[mid:]

        left = self.sort(left) #
        right = self.sort(right)
        result = self.merge(left, right)
        return result


    def merge(self, left, right):
        result = []
        i = 0 # i = 1 j = 2
        j = 0 #
        while i < len(left) and j < len(right):
            if left[i] >= right[j]:
                result.append(right[j])
                j += 1
            else:
                result.append(left[i])
                i += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        return result

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
        print("Merge Sort Output")
        print("==================================================")
        for i in range(len(numbers)):
            if i + 1 == len(numbers):
                print(f"{numbers[i]}]")
            elif i == 0:
                print(f"[{numbers[i]}, ",end="")
            else:
                print(f"{numbers[i]}, ",end="")
        print("==================================================")
        print("Merge Sort Result:")
        print(f"Size of array = {len(numbers)}")
        print(f"Time taken = {time:.6f} seconds")
        print("==================================================")
