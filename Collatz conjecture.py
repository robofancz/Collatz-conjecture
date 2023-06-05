import operator
import time 


LoopCount = {}
MaxSteps = 0
MaxStepsNumber = 0

def CollatzConjecture(x):
    global MaxSteps
    global MaxStepsNumber
    counter = 0
    sx = x
    while x > 1:
        if x in LoopCount:
            counter += LoopCount[x]
            break
        # test if the number x is even
        if x % 2 == 0:
            #even
            x = x//2
        else:
            #odd
            x = 3*x+1
        counter = counter + 1

    LoopCount[sx] = counter
    if counter > MaxSteps:
        MaxSteps = counter
        MaxStepsNumber = sx
    #print (f'in: {sx:>5} result: {x} loops:  {counter:>5}')

CurrentNumber = 1 
StartTime = time.time_ns ()
LastTime = StartTime
while True:
    CollatzConjecture (CurrentNumber)
    CurrentTime = time.time_ns ()
    if CurrentTime - LastTime > 1000000000:
        currentsteps = LoopCount[CurrentNumber]
        print (f'Current number: {CurrentNumber:>12,} Number of steps: {currentsteps:>5,} Max number of steps {MaxSteps:>5,} For the number {MaxStepsNumber:>12,} Elapsed seconds: {(CurrentTime-StartTime)//1000000000}')
        LastTime = CurrentTime
    CurrentNumber = CurrentNumber + 1