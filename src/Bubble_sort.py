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

                    



    def print(self, sample, time):
        print(f"Time taken = {time:.6f} seconds")
        for i in range(len(sample)):
            print(sample[i],end= " ")

                        




            