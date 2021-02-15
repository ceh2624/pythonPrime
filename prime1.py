import time
import math
import array

def convert(seconds): 
	hours = seconds / 3600
	hoursRem = seconds % 3600 # Remainder from hours calculation
	minutes = hoursRem / 60
	seconds = hoursRem % 60   # Remainder from minutes calculation
	
	strHours = "hour"			# **********************************
	if int(hours) != 1:			# Make adjustments for English grammer
		strHours = "hours"		# plural or singular given when needed
	strMinutes = "minute"
	if int(minutes) != 1:
		strMinutes = "minutes"	# **********************************

	print ("%i %s, %i %s, %.2f seconds." % (hours, strHours, minutes, strMinutes, seconds))

numArray = array.array('I')
limit = input('enter number for top limit of search ->')# User input stored as a string
limit = int(limit) # Typecast to integer
print (limit)
uLim = math.floor(math.sqrt(limit))

uLim = int(uLim)
print (uLim)
startTime = time.time() # Remember time programme begins...

for x in range(0, limit+1): # Populate the array
	numArray.append(x)

for y in range(2, uLim):
	chk = y 
	chk = int(chk)
	#print "chk = %i and y = %i and numArray[chk] = %i" % (chk, y, numArray[chk])
	while (chk < limit):
		if(numArray[chk] % y == 0 and numArray[chk] != y):
			numArray[chk] = 0
		chk = chk + 1
endTime = time.time() # Remember when it ends
count = 0 # to count number of prime numbers - - -
		
for z in range(2, limit):
	if numArray[z] != 0:
		print ("%i is a prime number." % numArray[z])
		count += 1 # counting prime numbers
fullTime = endTime - startTime
print ("Elasped time = %.2f seconds" %(fullTime))
print ("there are %i prime numbers up to %i" % (count, limit))
print ("The floor of the square root of %i is %i." % (limit, uLim))
print ()
print ("%.2f seconds breaks out to..." %(fullTime))

convert(fullTime)
