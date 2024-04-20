mylist=[1,2,3,4,5,6]
my_iterator=iter(mylist) # Get an iterator

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
#Continue calling next() until all element are exhasted

'''
The main difference between iterable and iterator

iterable:

An iterable is an object can be iterared over
it implements the __iter__ method which return an iterator


iterator:

An iterator is an object that repersent a stream of data
It implements both iter and next methond
'''