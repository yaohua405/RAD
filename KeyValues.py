#Function returning a list of only key attributes. Argument: 'arr' is a list of 1s and 0s
def createDataStructure(EventData, EventID):
    activeValues = []
    EventID -= 1
    if len(KeyAttributes[EventID]) > 0:
        for i, val in enumerate(KeyAttributes[EventID]):
            if val == 1:
                activeValues.append(EventData[i])
        return activeValues
    else:
        print("\nErr: list argument contains no data.\n")

KeyAttributes = [[ 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1], #1
                [ 0, 0, 0, 1, 1, 0, 1],                                         #2
                [ 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0],              #3
                [ 0, 0, 0, 0 ],                                                 #4
                [ 0, 0, 1, 1, 1],                                               #5
                [ 0, 0, 0, 1, 1, 1],                                            #6
                [ 0, 0, 0, 1, 1, 0, 1, 1, 1 ],                                  #7
                [ 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1 ],                            #8
                [ 0, 0, 0, 1, 1 ],                                              #9
                [ 0, 0, 0, 0, 0, 1, 0, 0, 1, 0 ],                               #10
                [ 0, 0, 0, 1, 1, 0],                                            #11
                [ 0, 1, 0, 0, 0, 1, 1, 0],                                      #12
                [ 0, 0, 0, 0, 1, 1, 1, 0, 0],                                   #13
                [ 0, 0, 1, 1, 1, 1, 0],                                         #14
                [ 0, 0, 0, 1, 1, 0, 0],                                         #15
                [ 0, 0, 1],                                                     #16
                [ 0, 0, 0, 0, 1, 1, 1],                                         #17
                [ 0, 0, 0, 0, 1, 1, 1],                                         #18
                [ 0, 0, 1, 1, 1, 1, 1],                                         #19
                [ 0, 0, 1, 1, 1, 1, 1],                                         #20
                [ 1, 1, 1, 1, 1, 1],                                            #21
                [ 0, 0, 0, 0, 1, 1, 0, 1],                                      #22
                [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],                                #23
                [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],                             #24
                [ 1, 1, 1, 1, 1, 1],                                            #25
                [ 0, 0, 0, 0, 1, 1, 1, 0 ]]                                     #26