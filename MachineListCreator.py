#Takes a machine name and a range of numbers, then outputs a list of machine IDs with the provided range and name


def MachineList():
    machinePrefix = input("Enter the prefix of the machine's ID (ex. bccx, bcpsm, bcwsm)")
    
    machineFirstSuffix = input("Enter the first suffix ID of the machine (ex. 1, 5, etc)")
    machineFirstSuffix = int(machineFirstSuffix)
    
    machineLastSuffix = input("Enter the last suffix ID of the machine (ex. 80, 90, etc)")
    machineLastSuffix = (int(machineLastSuffix) + 1)
    
    idNumberList = list(range(machineFirstSuffix, machineLastSuffix))

    finalIdNumberList = [str(i).zfill(3) for i in idNumberList]

    print ([machinePrefix + str(i) for i in finalIdNumberList])


MachineList()
