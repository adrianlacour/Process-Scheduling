#Authors: Adrian LaCour, Brad Dennis'
#Execution: python3 proj.py
import time #To keep track of the process burst time
import random #To generate the random numbers
#import timeit #Couldn't use this because the python version is too old on the CSE machines
import operator

f = open("results.txt", "wt")


#All 5 processes have the same speed and memory. Assign 200 processes to the
#5 processors. The used algorithm is SJF
def question1():
    processes = []#List to store the process burst times
    waitTime = []#List to store the wait time for each process
    turnAroundTime = 0#Stores the turn Around Time of all of the processes
    #Create lists to hold 1/5 of the processes
    processor1 = []
    processor2 = []
    processor3 = []
    processor4 = []
    processor5 = []

    #randomly generate 200 processes, with burst times between (10*10^6 and 50*10^12)
    # (10,000,000 - 50,000,000,000,000)
    for i in range(1, 201):
        processes.append(random.randint(10000000, 50000000000001))#Append to list

    processes.sort()#Sort the processes based on the their burst time, in ascending order

    #Assigns the processes to the processors, in order. Assignments could also be done in 2d array
    for i in range(0, 40, 5):
        processor1.append(processes[i])
        processor2.append(processes[i + 1])
        processor3.append(processes[i + 2])
        processor4.append(processes[i + 3])
        processor5.append(processes[i + 4])

    #Do the SJF algorithm, with processors = 1GHz = 1 cycle per nanosecond
    startTime = time.time()
    while True:
        #Break if there are no more processes left for all of the processors
        if(len(processor1) == 0 and len(processor2) == 0 and len(processor3) == 0 and len(processor4) == 0 and len(processor5) == 0):
            break

        #Check if the process is empty and if the current burst time greater than 0
        if processor1 and processor1[0] > 0:
            processor1[0] -= 1000000000
        else:#If burst time is less than 0 and there is still something in the list, pop the 1st element
            if processor1:
                processor1.pop(0)

        if processor2 and processor2[0] > 0:
            processor2[0] -= 1000000000
        else:
            if processor2:
                processor2.pop(0)

        if processor3 and processor3[0] > 0:
            processor3[0] -= 1000000000
        else:
            if processor3:
                processor3.pop(0)

        if processor4 and processor4[0] > 0:
            processor4[0] -= 1000000000
        else:
            if processor4:
                processor4.pop(0)

        if processor5 and processor5[0] > 0:
            processor5[0] -= 1000000000
        else:
            if processor5:
                processor5.pop(0)

    #Elapsed time
    endTime = time.time()
    turnAroundTime = endTime - startTime
    averageTurnAroundTime = float(turnAroundTime / 200)#Divide the total time by 200 (which is n)
    f.write(str(averageTurnAroundTime) + "\n")


def question2():
    processes = [[0 for x in range(2)]for y in range(200)] # List to store the process burst times and process memory
    processesMemory = []
    waitTime = []  # List to store the wait time for each process
    turnAroundTime = 0  # Stores the turn Around Time of all of the processes
    # Create lists to hold 1/5 of the processes
    SortedProcess=[]
    processor1 = []
    processor2 = []
    processor3 = []
    processor4 = []
    processor5 = []

    #processor memory in bytes
    processorMemory1 =  2000000000
    processorMemory2 =  2000000000
    processorMemory3 =  4000000000
    processorMemory4 =  4000000000
    processorMemory5 =  8000000000
    
    # randomly generate 200 processes, with burst times between (10*10^6 and 50*10^12)
    # (10,000,000 - 50,000,000,000,000) and the memory
    for i in range(1, 201):
        processes[i-1][0]=(random.randint(10000000, 50000000000001))  # Append to list the burst time
        processes[i-1][1]=(random.randint(262144, 8589934593))        # Append to list the memory in bytes

    processes.sort(key=lambda x:(x[0], x[1]))  # Sort the processes based on both burst time and memory usage

    for i in range(1, 201):
        processor1counter = 0
        processor2counter = 0
        processor3counter = 0
        processor4counter = 0

    # Assigns the processes to the processors, in order. Assignments could also be done in 2d array
    for i in range(0,200):
        if((processes[i][1]<= processorMemory1)and (processor1counter<=processor2counter)
                and (processor1counter<=processor3counter) and (processor1counter<=processor4counter)):

            processor1.append(processes[i][0])
            processor1counter = processor1counter + 1

        elif((processes[i][1]<=processorMemory2)and (processor2counter<=processor1counter)and (processor2counter<=processor3counter)
                and (processor2counter<=processor4counter)):
            processor2.append(processes[i][0])
            processor2counter = processor2counter + 1

        elif((processes[i][1]<=processorMemory3) and (processor3counter<=processor4counter)):
            processor3.append(processes[i][0])
            processor3counter = processor3counter + 1

        elif(processes[i][1]<=processorMemory4):
            processor4.append(processes[i][0])
            processor4counter = processor4counter + 1

        elif(processes[i][1] <= processorMemory5):
            processor5.append(processes[i][0])



    # Do the SJF algorithm, with processors = 1GHz = 1 cycle per nanosecond
    startTime = time.time()
    while True:
        # Break if there are no more processes left for all of the processors
        if (len(processor1) == 0 and len(processor2) == 0 and len(processor3) == 0 and len(processor4) == 0 and len(
                processor5) == 0):
            break

        # Check if the process is empty and if the current burst time greater than 0
        if processor1 and processor1[0] > 0:
            processor1[0] -= 1000000000
        else:  # If burst time is less than 0 and there is still something in the list, pop the 1st element
            if processor1:
                processor1.pop(0)

        if processor2 and processor2[0] > 0:
            processor2[0] -= 1000000000
        else:
            if processor2:
                processor2.pop(0)

        if processor3 and processor3[0] > 0:
            processor3[0] -= 1000000000
        else:
            if processor3:
                processor3.pop(0)

        if processor4 and processor4[0] > 0:
            processor4[0] -= 1000000000
        else:
            if processor4:
                processor4.pop(0)

        if processor5 and processor5[0] > 0:
            processor5[0] -= 1000000000
        else:
            if processor5:
                processor5.pop(0)

    # Elapsed time
    endTime = time.time()
    turnAroundTime = endTime - startTime
    averageTurnAroundTime = float(turnAroundTime / 200)  # Divide the total time by 200 (which is n)
    f.write(str(averageTurnAroundTime) + "\n")


def question3():
    processes = []  # List to store the process burst times
    waitTime = []  # List to store the wait time for each process
    turnAroundTime = 0  # Stores the turn Around Time of all of the processes
    
    # Create lists to hold 1/5 of the processes
    processor1 = []
    processor2 = []
    processor3 = []
    processor4 = []
    processor5 = []
    processor1speed = 2000000000
    processor2speed = 2000000000
    processor3speed = 3000000000
    processor4speed = 3000000000
    processor5speed = 4000000000
    # randomly generate 200 processes, with burst times between (10*10^6 and 50*10^12)
    # (10,000,000 - 50,000,000,000,000)
    for i in range(1, 201):
        processes.append(random.randint(10000000, 50000000000001))  # Append to list

    processes.sort()  # Sort the processes based on the their burst time, in ascending order
    # Assigns the processes to the processors, in order. Assignments could also be done in 2d array

    processor1counter = 0
    processor2counter = 0
    processor3counter = 0
    processor4counter = 0



    for i in range(0, 200):
        if((processes[i]<=processor1speed) and (processor1counter<=processor2counter)
                and (processor1counter<=processor3counter) and (processor1counter<=processor4counter)):
            processor1.append(processes[i])
            processor1counter = processor1counter + 1

        elif ((processes[i] <= processor2speed) and (processor2counter <= processor1counter) and (
                processor2counter <= processor3counter)
              and (processor2counter <= processor4counter)):
            processor2.append(processes[i])
            processor2counter = processor2counter + 1

        elif ((processes[i] <= processor3speed) and (processor3counter <= processor4counter)):
            processor3.append(processes[i])
            processor3counter = processor3counter + 1

        elif (processes[i] <= processor4speed):
            processor4.append(processes[i])
            processor4counter = processor4counter + 1

        elif (processes[i] <= processor5speed):
            processor5.append(processes[i])

    # Do the SJF algorithm, with processors 
    startTime = time.time()
    while True:
        # Break if there are no more processes left for all of the processors
        if (len(processor1) == 0 and len(processor2) == 0 and len(processor3) == 0 and len(processor4) == 0 and len(
                processor5) == 0):
            break

        # Check if the process is empty and if the current burst time greater than 0
        if processor1 and processor1[0] > 0:
            processor1[0] -= 2000000000
        else:  # If burst time is less than 0 and there is still something in the list, pop the 1st element
            if processor1:
                processor1.pop(0)

        if processor2 and processor2[0] > 0:
            processor2[0] -= 2000000000
        else:
            if processor2:
                processor2.pop(0)

        if processor3 and processor3[0] > 0:
            processor3[0] -= 3000000000
        else:
            if processor3:
                processor3.pop(0)

        if processor4 and processor4[0] > 0:
            processor4[0] -= 3000000000
        else:
            if processor4:
                processor4.pop(0)

        if processor5 and processor5[0] > 0:
            processor5[0] -= 4000000000
        else:
            if processor5:
                processor5.pop(0)

    # Elapsed time
    endTime = time.time()
    turnAroundTime = endTime - startTime
    averageTurnAroundTime = float(turnAroundTime / 200)  # Divide the total time by 200 (which is n)
    f.write(str(averageTurnAroundTime) + "\n")


def question4():
    processes = []  # List to store the process burst times
    waitTime = []  # List to store the wait time for each process
    turnAroundTime = 0  # Stores the turn Around Time of all of the processes
    # Create lists to hold 1/5 of the processes
    processor1 = []
    processor2 = []
    processor3 = []
    processor4 = []
    processor5 = []
    # randomly generate 200 processes, with burst times between (10*10^6 and 50*10^12)
    # (10,000,000 - 50,000,000,000,000)
    for i in range(1, 201):
        processes.append(random.randint(10000000, 50000000000001))  # Append to list



    processorSums=[0,0,0,0,0]


    for i in range(0, 200):
        lazyiest=processorSums.index(min(processorSums))

        if(lazyiest==0):
            processor1.append(processes[i])
            processorSums[0]= processorSums[0]+processes[i]

        if(lazyiest==1):
            processor2.append(processes[i])
            processorSums[1] = processorSums[1] + processes[i]

        if(lazyiest == 2):
            processor3.append(processes[i])
            processorSums[2] = processorSums[2] + processes[i]

        if(lazyiest == 3):
            processor4.append(processes[i])
            processorSums[3] = processorSums[3] + processes[i]

        if(lazyiest == 4):
            processor5.append(processes[i])
            processorSums[4] = processorSums[4] + processes[i]

    # Do the SJF algorithm, with processors = 1GHz = 1 cycle per nanosecond
    startTime = time.time()
    while True:
        # Break if there are no more processes left for all of the processors
        if (len(processor1) == 0 and len(processor2) == 0 and len(processor3) == 0 and len(processor4) == 0 and len(
                processor5) == 0):
            break

        # Check if the process is empty and if the current burst time greater than 0
        if processor1 and processor1[0] > 0:
            processor1[0] -= 1000000000
        else:  # If burst time is less than 0 and there is still something in the list, pop the 1st element
            if processor1:
                processor1.pop(0)

        if processor2 and processor2[0] > 0:
            processor2[0] -= 1000000000
        else:
            if processor2:
                processor2.pop(0)

        if processor3 and processor3[0] > 0:
            processor3[0] -= 1000000000
        else:
            if processor3:
                processor3.pop(0)

        if processor4 and processor4[0] > 0:
            processor4[0] -= 1000000000
        else:
            if processor4:
                processor4.pop(0)

        if processor5 and processor5[0] > 0:
            processor5[0] -= 1000000000
        else:
            if processor5:
                processor5.pop(0)

    # Elapsed time
    endTime = time.time()
    turnAroundTime = endTime - startTime
    averageTurnAroundTime = float(turnAroundTime / 200)  # Divide the total time by 200 (which is n)
    f.write(str(averageTurnAroundTime) + "\n")


f.write("Question 1" + "\n")
for i in range(1, 201):#Run 200 times for the trial set
    question1()#Call the question 1 function

f.write("Question 2" + "\n")
for i in range(1, 201):#Run 200 times for the trial set
    question2()

f.write("Question 3" + "\n") 
for i in range(1, 201):#Run 200 times for the trial set
    question3()

f.write("Question 4" + "\n")    
for i in range(1, 201):#Run 200 times for the trial set
    question4()
