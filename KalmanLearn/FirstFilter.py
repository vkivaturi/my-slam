#Kalman filter - 1 that related to State Update Equation. 
#Refer to https://www.kalmanfilter.net/alphabeta.html
import sys

#Define object to hold the measurements and calculations. 
class FirstFilterData:
    def __init__(self, cm, it, ti, ce, pe):
        self.currentMeasurement = cm
        self.iterationNumber = it
        self.totalIterations = ti
        self.currentEstimation = ce
        self.previousEstimation = pe

#Initialise the 3 main part of equation
FFData = FirstFilterData(0,0,0,0,0)
print(FFData.currentEstimation)

#State Update Equation
#currentEstimation = previousEstimation + ((currentMeasurement - previousEstimation) / iterationNumber )  

def calculateCurrentEstimation(ffd):
    print("## Inside calculate current estimation iteration ", ffd.iterationNumber)

def processInput():
    print("## Input process has started ", sys.argv[1], sys.argv[2])
    FFData.currentMeasurement = sys.argv[1]
    FFData.totalIterations = sys.argv[2]
    FFData.iterationNumber = 1

    calculateCurrentEstimation(FFData)
    
if __name__ == "__main__":
    processInput()