#Kalman filter - 1 that related to State Update Equation. 
#Refer to https://www.kalmanfilter.net/alphabeta.html
#Main function can be invoked by passing 3 command line arguments
#   startEstimation - starting estimation of the state to be error corrected across multiple measurements 
#   totalIterations - number of iterations of the filter. Final estimation stabilises after a certain number of iterations
#   errorPercentage - since there is no physical device to share actual measurement in each iteration, a random algo is used
#Sample command - python3 FirstFilter.py 10000 1000 1
import sys
import random

#Define object to hold the measurements and calculations. 
class FirstFilterData:
    def __init__(self, se, cm, it, ti, ce, pe, er):
        self.startEstimation = se
        self.currentMeasurement = cm
        self.iterationNumber = it
        self.totalIterations = ti
        self.nextEstimation = ce
        self.previousEstimation = pe
        self.errorPercentage = er
    def printStats(self):
        print(f"New measurement : {self.currentMeasurement}, previous estimation : {self.previousEstimation}, current estimation : {self.nextEstimation}" )
    
#Initialise the 3 main part of equation
FFData = FirstFilterData(0,0,0,0,0,0,0)

#State Update Equation
#currentEstimation = previousEstimation + ((currentMeasurement - previousEstimation) / iterationNumber )  

def calculateCurrentEstimation():
    #Step 1 - Set previous estimation before applying the filter to calculate current estimation
    FFData.previousEstimation = FFData.nextEstimation
    
    #Step 2 - In the absence of a measuring device, a random number is used for current measurement
    startRange = FFData.startEstimation * (1 - (FFData.errorPercentage/100) )
    endRange = FFData.startEstimation * (1 + (FFData.errorPercentage/100))
    FFData.currentMeasurement = random.randint(startRange, endRange)

    #Step 3 - Calculate the current estimation using filter formula
    tempEstimation = FFData.previousEstimation + ((FFData.currentMeasurement - FFData.previousEstimation) / FFData.iterationNumber) 
    FFData.nextEstimation = int(tempEstimation)

    FFData.printStats()

def processInput():
    print("## Input process has started ", sys.argv[1], sys.argv[2])
    FFData.startEstimation = int(sys.argv[1])
    FFData.totalIterations = int(sys.argv[2])
    FFData.errorPercentage = int(sys.argv[3])
    FFData.iterationNumber = 1

    while FFData.iterationNumber <= FFData.totalIterations:
        calculateCurrentEstimation()
        FFData.iterationNumber += 1
    
if __name__ == "__main__":
    processInput()