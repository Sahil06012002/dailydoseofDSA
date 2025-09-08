from typing import List


class MinHeap :
    nums = []

    def __init__(self, nums):
        nums = nums


    def heapifyUp(index) :
        currentIndex = index

        parentIndex = (currentIndex-1)//2

        while(MinHeap.nums[parentIndex] > MinHeap.nums[currentIndex] ) :
            MinHeap.nums[parentIndex] , MinHeap.nums[currentIndex] = MinHeap.nums[currentIndex] , MinHeap.nums[parentIndex]
            currentIndex = parentIndex
            parentIndex = (currentIndex-1)//2
            if parentIndex < 0 :
                break 


    def heapifyDown(index) :
        parentIndex = index
        while((2 * parentIndex + 1) < len(MinHeap.nums)) :
            parentElement = MinHeap.nums[parentIndex]
            candidateIndex = [float("inf")] * 2
            
            leftChild = MinHeap.nums[(2 * parentIndex + 1)] 
            rightChild = MinHeap.nums[(2 * parentIndex + 2)]
            
            
            if leftChild < parentElement :
                candidateIndex[0] = 2 * parentIndex + 1

            if leftChild > parentElement and rightChild > parentElement :
                break 
            if rightChild < parentElement :
                candidateIndex[1] = 2 * parentIndex + 2

            smallerIndex = min(candidateIndex[0],candidateIndex[1])

            MinHeap.nums[smallerIndex] , MinHeap.nums[parentIndex] =  MinHeap.nums[parentIndex]  ,MinHeap.nums[smallerIndex]
            parentIndex = smallerIndex





        # check which one is more smaller







    
    def insert(self,element : int) :
        

        MinHeap.nums.append(element)

        if len(MinHeap.nums) > 0 :
            currentIndex = len(MinHeap.nums) -1
            MinHeap.heapifyUp(currentIndex)

        print(MinHeap.nums)

        

    def peek(self) :
        if len(MinHeap.nums) > 0 :
            print(MinHeap.nums[0])

        else :
            print("array is empty")


    def pop(self) :
        lastElement = MinHeap.nums[len(MinHeap.nums)]
        MinHeap.nums[0] = lastElement
        # i have to remove the last element
        MinHeap.nums.pop()

        MinHeap.heapifyDown() 



mh = MinHeap([])
mh.insert(45)
mh.insert(4)
mh.insert(42)




    







        




        

#     def sortC(self,nums : List[int]) :
#         HeapSort.minHeap(nums)
#         # print(nums)

# asol = HeapSort()
# asol.sortC("sahil")
        

