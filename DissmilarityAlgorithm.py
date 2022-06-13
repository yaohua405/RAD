from asyncio.windows_events import NULL
from difflib import SequenceMatcher
from os.path import exists
import pickle as p

threshhold = 0.9

def StringCompare(string1, string2):
    return 1 - SequenceMatcher(None, string1, string2).ratio()

class mode:
    modeattrs = []
    def __init__(self, attrs):
        self.modeattrs = attrs

    def GetCSVFormat(self):
        returnString = ""
        for attr in self.modeattrs:
            returnString += str(attr) + ","
        returnString = returnString.removesuffix(',')
        if len(returnString) > 4:
            returnString += "\n"
        return returnString

class machine:
    totalTrained = NULL
    num = NULL
    modes = []
    def __init__(self, num):
        self.num = num
        self.modes = []
        self.totalTrained = 0

    def PrintCurrentState(self):
        print(len(self.modes), " Modes")
        for mode in self.modes:
            print(mode.modeattrs[0])

    def predict(self, attrs): 
        dissimilarity = 1
        for m in self.modes:
            sum = 0
            i = 0
            for attr in attrs:
                if i < len(m.modeattrs):
                    sum += StringCompare(attr, m.modeattrs[i])
                    i += 1
            if len(attrs) != 0:
                avg = sum / len(attrs)
            else:
                avg = 0
            self.totalTrained += 1
            if avg < dissimilarity:
                dissimilarity = avg
            if dissimilarity < threshhold:
                return dissimilarity        
        return dissimilarity

    def AddMode(self, attrs):
        # print("Added mode to", self.num)
        self.modes.append(mode(attrs))

    def SaveState(self):
        outputFile = open("Machine" + str(self.num) + ".csv", "w")
        for mode in self.modes:
            endl = False
            for attr in mode.modeattrs:
                temp = str(attr)
                if temp.isspace() == False:
                    endl = True
                    outputFile.write(str(attr) + ",")
            if endl:
                outputFile.write("\n")

    def LoadState(self):
        if exists("Machine" + str(self.num) + ".csv"):
            inputFile = open("Machine" + str(self.num) + ".csv", "r")
            for line in inputFile.readlines():
                attrArr = line.split(",")
                if attrArr != []:
                    self.AddMode(attrArr)

    def SaveStatePKL(self):
        state = []
        for mode in self.modes:
            state.append(mode.modeattrs)
        return state

    def LoadStatePKL(self, modedata):
        for i in modedata:
            self.modes.append(mode(i))

class Dissimilarity:
    machines = []
    eventsTrained = 0

    def __init__(self):
        for i in range(26):
            self.machines.append(machine(i))
        print("Initiating algorithm")

    def Predict(self, attributes, n):
        dissimilarity = self.machines[n].predict(attributes)
        self.eventsTrained += 1
        if dissimilarity > threshhold:
            self.machines[n].AddMode(attributes)
            return True
        else:
            return False

    def Train(self, attributes, n):        
        dissimilarity = self.machines[n].predict(attributes)
        self.eventsTrained += 1
        if dissimilarity > threshhold:
            self.machines[n].AddMode(attributes)
            return True
        else:
            return False

    def PrintCurrentState(self):
        for i in range(26):
            # print("Machine ", (i+1))
            self.machines[i].PrintCurrentState()

    def SaveState(self):
        for machine in self.machines:
            machine.SaveState()
        outputFile = open("eventcount.csv", "w")
        for m in self.machines:
            outputFile.write(str(m.totalTrained) + ",")        

    def LoadState(self):
        if exists("eventcount.csv"):
            inputFile = open("eventcount.csv", "r")
            inputlines = inputFile.read()
            lines = inputlines.split(',')
            for i, line in enumerate(lines):
                if line != '':
                    self.machines[i].totalTrained = int(line)
        for machine in self.machines:
            machine.LoadState()

    def SaveStatePKL(self):
        machineList = []
        for machine in self.machines:
            machineList.append(machine.SaveStatePKL())
        with open("AlgorithmState.pkl", "wb") as f:
            p.dump(machineList, f)   
        outputFile = open("eventcount.csv", "w")
        for m in self.machines:
            outputFile.write(str(m.totalTrained) + ",")       

    def LoadStatePKL(self):
        if exists("eventcount.csv"):
            inputFile = open("eventcount.csv", "r")
            inputlines = inputFile.read()
            lines = inputlines.split(',')
            for i, line in enumerate(lines):
                if line != '':
                    self.machines[i].totalTrained = int(line)
        if exists("AlgorithmState.pkl"):
            with open("AlgorithmState.pkl", "rb") as f:
                dump = p.load(f)
            for i, x in enumerate(dump):
                self.machines[i].LoadStatePKL(x)