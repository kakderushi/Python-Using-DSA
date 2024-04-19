'''
 A chocalte factory is packing chocolates into the packets. The Chocolate packets here represent an array of N number
 of interger values. The task is to find the empty packet(0) and push it to the end of the conveyor belt(array)
 
 
 Input= N=8 arr=[4,5,0,1,9,0,5,0]
 here are 3 empty packets in the given set. these 3 empty packets represented as 0 should be pushed towards the end of the array
  
   Output:
   
   4,5,1,9,5,0,0,0
   
'''
def push_empty_packets_to_end(n,arr):
    i=0
    while i<n:
        if arr[i]==0:
     # remove the zero form its current position
            arr.pop(i)
    # append it to the end of the array
            arr.append(0)
            
            n-=1
        else:
            # move to the next element
            i+=1
            
    return arr

            

# Driver Code
n=8
arr=[4,5,0,1,9,0,5,0]
result=push_empty_packets_to_end(n,arr)
print("Result :", result)
