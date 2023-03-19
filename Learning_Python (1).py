"""
4308 Concepts of Programming Languages
February 22, 2022
Morgan Stafford
Ethan Fitzgerald
Samuel Futral
Adnan Eid
example: D:\Classes\CS 4308\Modules_3_5_7_Project Resources\SCL_Project\welcome.scl
"""
operators = ['+', '-', '', '/', '%', '=', '==', '!=', '<', '>', '<=', '>=', '&&', '||', '!']
keywords = ['if', 'import', 'description', 'forward', 'declarations', 
            'function', 'return', 'type', 'parameters', 'array', 'of', 'specifications', 'enumerate', 'is', 'struct'
            'else', 'while', 'do', 'break', 'continue', 'integer', 'float', 'char', 'double', 'void', 'symbol', 'variable']
specialCharacters = [';', ',', '(', ')', '{', '}']
constants = ['[]','\n']
identifiersArr = []
opArr = []   
keyArr = []
constantsArr = []
specialChArr = []

fileAddress = input("Enter Address of File: ") #Prompts user for scl file path
fileName = open(fileAddress, "r")
fileToParse = fileName.readlines()
fileSeperatedBySpaces = []
SCLtokens = []
i = 0
skipComment = False  #Boolean Placeholder
for line in fileToParse:
    if line.find('description') != -1: #Gets rid of the comments before the code
        skipComment = True
        continue
    if line.find('*/') != -1: #Gets rid of the comments before the code
        skipComment = False
        continue
    if not skipComment:
        fileSeperatedBySpaces.append(line.split()) 
for i in fileSeperatedBySpaces:
    skipComment = False
    for x in i:
        if x.find('//') != -1:
            skipComment = True
            continue
        if not skipComment:
            SCLtokens.append(x)
            
    
print('The tokens are: ' + str(SCLtokens) + '\n') 
for word in SCLtokens:  #Traverses Array to Distinguish Grammar Types
    if word in keywords:
        keyArr.append(word)
    if word in operators:
        opArr.append(word)
    if word in specialCharacters:
        specialChArr.append(word)    
    if word not in keyArr and word not in operators and word not in specialCharacters: 
        identifiersArr.append(word)
    if word in constants:
        constantsArr.append(word)
#prints grammar type arrays
print('Keywords: ' + str(keyArr) + '\n') 
print('Operators: ' + str(opArr)+ '\n') 
print('Special Characters: ' + str(specialChArr)+ '\n') 
print('Identifiers ' + str(identifiersArr)+ '\n') 
print('Constants ' + str(constantsArr)+ '\n') 

fileName.close()

''''The scanner implementation must include an array of the keywords used in the subset of SCL or other
selected programming Language, an array (or list) of the identifiers (variables), and other
tokens (such as operators, keywords, constants, and/or special characters.)'''




