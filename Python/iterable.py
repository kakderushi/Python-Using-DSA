# Iterable and iterator 
import sys
l=[ i for i in range(1000)]
print(sys.getsizeof(l))


l2=[1,2,4,5]
for i in l2:
    print(i)
    
dir(l2)
print(dir(l2))
    
# using it we can check the iterator    
'__iter__' in dir(l2) 

# iterble can be converted in iterator

print(iter(l2))



