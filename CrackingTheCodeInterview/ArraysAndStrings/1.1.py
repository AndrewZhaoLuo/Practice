'''
Question:

Implement an algorithm to detmerine if a string has all unique characters.
What if you cannot use additional data structures?
'''

def isMedian(n1, o1, o2):
    if(n1 >= o1 and n1 <= o2) or (n1 >= o2 and n1 <= o1):
        return True
    return False

def switchPlaces(i1, i2, array):
    temp = array[i1]
    array[i1] = array[i2]
    array[i2] = temp

    return temp

def qsort(start, end, array):
    if(start < end):
        #find a pivot by sampling from the start, middle, and end of array and choosing the median
        sP = array[start]
        mP = array[int((start + end)/2)]
        eP = array[end]
        iP = 0    #initial index

        if isMedian(sP, mP, eP):
            iP = start
        elif isMedian(mP, sP, eP):
            iP = (start + end)/2
        else:
            iP = end

        #move pivot to end of array we are working in
        pivot = switchPlaces(iP, end, array)
    
        #then iterate through array, putting all elements less than pivot to the left of where
        #the pivot shall be!
        pivotI = start
        for i in xrange(start, end):
            if array[i] <= pivot:
                switchPlaces(i, pivotI, array)
                pivotI += 1

        #place our pivot in the right place
        switchPlaces(pivotI, end, array)

        #qsort our partioned array
        qsort(start, pivotI - 1, array)
        qsort(pivotI + 1, end, array)
            
#with a data structure, use a table for easy lookup if a character had already been there
def allUnique(string):
    count = [0] * 128 #assuming ascii, limited character set
    for i in xrange(0, len(string)):
        if count[ord(string[i])] == 1:
            return False

        count[ord(string[i])] = 1

    return True

#without data structures
def allUnique2(string):
    #1
    #with no way to store we've met a character, we're in a sorry spot
    #one thing we can do is figure out the minimum number of comparisons needed
    #in this case it's n^2 time, since the 0th digit checks all digits from the 1st
    #the 1st digits checks from the 2nd to the end
    #ie n-1 + n-2 + n-3 + ... 1 = n(n-1)/2 - n

    #2
    #we can also use an O(nlogn)-typical sorting algorithm to sort all the characters
    #in our array. Then we can iterate and make sure no adjacent elements are equal
    #this would run in O(nlogn + n) time, nlogn from the sort, and n from iterating through
    #our sorted string

    #3
    #on a note of sorting, feed in a presorted string with every character
    #in it, use binary search to find a character and then setting the character at that
    #index to a value like -1 to mark its been searched
    #this may count as an additional data structure, since it goes beyond temporary variables
    #this would run O(nlogn) time since binary search is a log n search, and we do it
    #once for each character in our string (n times)
    
    #2 is probably the safest choice for this q
    qsort(0, len(string) - 1, string)
    for i in xrange(0, len(string) - 1):
        if string[i] == string[i + 1]:
            return False
    return True

string1 = ['a','d','b','c']
string2 = "abcd"

print allUnique2(string1)
print allUnique(string2)


'''
Optimizations I missed:

checking string length, ie a string with 1000000 chars cannot have unique chars.
since there are not that many unqiue chars!

knowing how many chars can be allocated for ascii and unicode. asking about ascii vs unicode
'''
