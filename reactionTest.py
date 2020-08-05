import time
import random
from os import system, name

nanoSecondsInMilliseconds = 1000000

def playGame():
    print("Gaming")

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

if __name__ == "__main__":
    print("Press any key to begin.")
    input()
    averageTime = 0
    for x in range(3):
        clear()
        print("Press any key when you see \"0\"")
        print("1")
        time.sleep(10)
        clear()
        print("0")
        timing = time.time_ns()
        input()
        timing = time.time_ns() - timing
        clear()
        print(str(timing/nanoSecondsInMilliseconds)+"ms")
        averageTime += timing
    print("Average time: " + str(averageTime/nanoSecondsInMilliseconds/3)+"ms")

