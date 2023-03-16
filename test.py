# path = 'transactions22.csv'
# memSize = 1200000

# try: 
#     # highly risky actions:
#     fileHandle = openFile(path, 'x')
#     fileData = fileHandle.readAll()
#     memoryAddress = allocateMemory(memSize)

# # following exceptions could occur:
# except IOError as error:
#     print("IO error on {0}: {1}".format(path, error))
# except MemoryError as error:
#     print("Memory error for size {0}: {1}".format(memSize,error))

# else: 
#     # now do the work safely
#     processTransactions(fileData, memoryAddress)

# finally:
#     # release all sources
#     if fileHandle:
#         closeFile(fileHandle)
#     if memoryAddress:
#         disposeMemory(memoryAddress, memSize)  

# import re 
# def isFloat(string):
#     matched = re.match("^\d+\.\d+$", string)
#     return matched and matched.group(0) == string

# numberString = input('Geef een getal: ')
# if isFloat(numberString):
#     number = float(numberString)
#     print('Number = ', number)
# else:
#     print('Number : ', numberString, ' is geen getal!' )