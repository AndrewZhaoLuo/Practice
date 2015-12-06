'''
Problem:
https://www.reddit.com/r/dailyprogrammer/comments/3u6o56/20151118_challenge_242_intermediate_vhs_recording/
'''
'''
Idea, sort tv shows by their end times. Then iterate through and keep track of the maximum
number of shows we can record recording up to a certain end time.

This can be done by adding 1 to the max total shows recorded up to a chosen show's start time.
Dynamic programming ftw
'''

class TvShow:
    def __init__(self, start, end):
        self.start = int(start)
        self.end = int(end)
        
    def __str__(self):
        return "start: " + str(self.start) + " end: " + str(self.end)
    
    def compareTo(self, other):
        #i don't like things crashing
        if not isinstance(other, TvShow):
            return 0
        return self.end - other.end
    
    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end

#swaps i1 and i2, returns what was originally in i1
def swapIndexes(i1, i2, array):
    temp = array[i1]
    array[i1] = array[i2]
    array[i2] = temp

    return temp

#general quicksort of an array which implements the method compareTo
def qsort(start, end, array):
    #pivot should generally be in the middle since middle ending shows tend to occur
    #in middle of the day
    if(start < end):
        pivot = swapIndexes((start + end) // 2, end, array)

        #place all elements less than pivot to left of pivot
        index = start
        for i in xrange(start, end):
            if array[i].compareTo(pivot) < 0:
                swapIndexes(i, index, array)
                index += 1

        #place pivot in this proper position
        swapIndexes(index, end, array)

        #sort our partitioned array
        qsort(start, index - 1, array)
        qsort(index + 1, end, array)

#read in file information
shows = []
print "Type file name"
f = open(str(raw_input()),'r')
for line in f:
    times = line.strip('\n').split(' ')
    shows.append(TvShow(times[0],times[1]))

#sort by endtime
qsort(0, len(shows) - 1, shows)

#each index, represents the maximum number of recorded shows up to that point
maxShows = 1
maxRecords = [0] * len(shows)
maxRecords[0] = 1
for c in xrange (1, len(maxRecords)):
    #don't forget to account for case of only choosing this show to record
    maxRecords[c] = 1 
    for p in xrange(0, c):
        if shows[c].getStart() >= shows[p].getEnd():
            maxRecords[c] = max(maxRecords[c], maxRecords[p] + 1)
    if maxRecords[c] > maxShows:
        maxShows = maxRecords[c]

print "Max shows VCR can record: " + str(maxShows)



