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
        

class HeapSort :

    def conver_to_maxheap(arr) : 
        n = len(arr)
        for i in range(n //2 -1,-1,-1) :
            HeapSort.heapify(arr, i , n)
    


    def heapify(arr, i , n) :
        largest = i
        leftIndex= (2 * i) + 1
        rightIndex = (2 * i ) + 2

        if leftIndex < n and arr[largest] <  arr[leftIndex] :
            largest = leftIndex

        if rightIndex < n and arr[largest] < arr[rightIndex] :
            largest = rightIndex

        if largest != i:
            temp = arr[i]
            arr[i] = arr[largest]
            arr[largest] = temp
            HeapSort.heapify(arr, largest,n)


    def heap_sort(arr) :
        n = len(arr)
        HeapSort.conver_to_maxheap(arr)

        for i in range(n-1, 0 , -1) :
            arr[0] , arr[i] = arr[i] , arr[0]
            HeapSort.heapify(arr, 0,i)




        
