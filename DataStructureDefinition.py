import win32evtlog
import xml.etree.ElementTree as ET
import ctypes
import os
import DissmilarityAlgorithm
import time
import KeyValues

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# Parses log archive file then deletes archive
def parse_log(inputPath, inputfile, predict, save, all):
    if inputPath == "":
        mypath = 'C:\Windows\System32\winevt\Logs\\'
    else:
        mypath = inputPath

    if inputfile == "":
        files = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    else:
        files = [inputfile]
    
    DissAlgorithm = DissmilarityAlgorithm.Dissimilarity()
    DissAlgorithm.LoadStatePKL()

    # Loops through every file
    for filename in files:
        if filename.startswith('Archive-Microsoft-Windows-Sysmon%4Operational') or all or inputfile:
            print("Opening file", filename)
            startTime = time.time()
            totalEvents = 0
            query_handle = win32evtlog.EvtQuery(mypath + filename, win32evtlog.EvtQueryFilePath)
            anomalyCount = 0
            anomalyCounts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            while True:                
                event = win32evtlog.EvtNext(query_handle, 1)
                if len(event) > 0:
                    # parse xml content
                    try:
                        xml = ET.fromstring(win32evtlog.EvtRender(event[0], win32evtlog.EvtRenderEventXml))

                        SystemInfo = xml[0]
                        EventData = xml[1]

                        eventAttribs = []                    
                        
                        for child in EventData:
                            eventAttribs.append([child.text])

                        EventID = int(SystemInfo[1].text)
                        if EventID != 255:
                            eventAttribs = KeyValues.createDataStructure(eventAttribs, EventID)

                            if predict:
                                if DissAlgorithm.Predict(eventAttribs, int(EventID) - 1):
                                    anomalyCount += 1
                                    # print("Anomaly found for EID: ", EventID)
                                    anomalyCounts[EventID - 1] += 1
                            else:
                                DissAlgorithm.Train(eventAttribs, int(EventID) - 1)
                            totalEvents += 1
                    except:
                        pass
                else:
                    break

            query_handle.close()
            if predict:
                pass
            else:
                DissAlgorithm.SaveStatePKL()

            if save == False:
                os.remove(mypath + filename)
            print("Total time:", time.time() - startTime, "seconds")
            print("Total events: ", totalEvents)
            if anomalyCount != 0:
                for i in range(16):
                    if anomalyCounts[i] > 0:
                        print(anomalyCounts[i], " anomalies found for Event ID ", (i+1))
                print(anomalyCount, " total anomalies found\n")

        else:
            pass