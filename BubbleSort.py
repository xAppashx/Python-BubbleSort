
def BubbleSort(ArrayToSort): 
      
      Array = ArrayToSort.copy()
      
      #for Loop in range(1, len(Array), 1): 
      for Loop in range(len(Array) - 2, -1, -1):
            
            Key = Array[Loop]
            i = Loop + 1
            
            while (i < len(Array)) and (Array[i] < Key):
                  TempVar = Array[i - 1]
                  Array[i - 1] = Array[i]
                  Array[i] = TempVar
                  
                  i = i + 1
                  
            #while
            
      #for Loop in range
      
      return (Array)
#def BubbleSort





# Test of the use // Feel free to delete the following lines to use the funtions only
Array = [3, 2, 1, 4, 5, 14, 22, 63, 6, 53, 22, 12, 45, 213, 53, 233, 41, 98]

#Call the BubbleSort function and send only the array to sort as parameter
ArrayFinal = BubbleSort(Array)

print("Original array: ", Array)
print("Sorted array: ", ArrayFinal)