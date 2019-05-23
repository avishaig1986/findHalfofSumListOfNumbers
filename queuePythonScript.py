
'''
The Follong script adds numbers from a given list until it finds a combination of numbers which their sum is equal to half of the sum of the list
Tested with Python 3.7.3 Win 10.
'''

tasksInMinList = [25, 4, 30, 7, 14, 10, 4, 6, 5, 25];
workers = 2


def CalculateOtherQueue(partial=[]):

	# remove the number 
    for p in partial:
    	tasksInMinList.remove(p)
    print ("*** First queue values: %s ***" % partial)
    print ("*** Second queue values: %s ***" % tasksInMinList)
    quit()

def subset_sum(numbers, halfOfSum, partial=[]):

	# print the given parameters
	# the partial parameter will have a value at least from the second recursive of the function
    s = sum(partial)
    print ("partial %s" % partial)
    print ("sum: %s" % s)
    
    # if the combination of adding numbers which equal to half of the list sum found, call the function CalculateOtherQueue and pass these numbers 
    if s == halfOfSum:
        print ("s is equal to halfOfSum")
        print ("partial %s halfOfSum %s" % (partial, halfOfSum))
        CalculateOtherQueue(partial)
     
    # if the combination was not found yet,  
    if s >= halfOfSum:
        print ("s is not equal to halfOfSum")
        return

    # attempt to find the half of the sum by adding numbers from the list
    for i in range(len(numbers)):
        print ("range is %s" % (numbers))
        number = numbers[i]
        print ("current number value: %s" % number)
        print ("current index value: %s" % i)
        remaining = numbers[i+1:]
        print ("current remaining value: %s" % number)

        # if the current combination was not found yet, keep calling the func recursively
        subset_sum(remaining, halfOfSum, partial + [number]) 


subset_sum(tasksInMinList,sum(tasksInMinList)/workers)