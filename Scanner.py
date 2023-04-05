"""
4308 Concepts of Programming Languages
February 22, 2022
Morgan Stafford
Ethan Fitzgerald
Samuel Futral
Adnan Eid
example: D:\Classes\CS 4308\Modules_3_5_7_Project Resources\SCL_Project\welcome.scl
"""
import re


class Scanner:
    fileAddress = ""
    identifiersArr = []
    valueArr = []
    opArr = []
    keyArr = []
    constantsArr = []
    specialChArr = []
    ParsedFile = []

    def __init__(self, filename):
        self.fileAddress = filename
        print(filename)

    def run(self):
        operators = ['+', '-', '', '/', '%', '=', '==', '!=', '<', '>', '<=', '>=', '&&', '||', '!']
        keywords = ['if', 'import', 'description', 'forward', 'declarations', 'function', 'return', 'type',
                    'parameters',
                    'array', 'of', 'specifications', 'enumerate', 'is', 'struct', 'else', 'while', 'do', 'break',
                    'continue', 'integer', 'float', 'char', 'double', 'void', 'symbol', 'variable']
        specialCharacters = [';', ',', '(', ')', '{', '}', '"']
        constants = ['[]','\n']
        fileName = open(self.fileAddress, "r")
        fileToParse = fileName.readlines()
        fileSeparatedBySpaces = []
        SCLtokens = []
        i = 0
        skipComment = False  # Boolean Placeholder
        for line in fileToParse:
            line = line.replace('"', ' " ')
            if line.find('description') != -1:  # Gets rid of the comments before the code
                skipComment = True
                continue
            if line.find('*/') != -1:  # Gets rid of the comments before the code
                skipComment = False
                continue
            if not skipComment:
                fileSeparatedBySpaces.append(line.split())
        for i in fileSeparatedBySpaces:
            skipComment = False
            for x in i:
                if x.find('//') != -1:
                    skipComment = True
                    continue
                if not skipComment:
                    SCLtokens.append(x)
        self.ParsedFile = SCLtokens
        """print('The tokens are: ' + str(SCLtokens) + '\n')"""
        valueString = ''
        #sameValue = False
        # i = 0
        for word in SCLtokens:  # Traverses Array to Distinguish Grammar Types
            if re.match(r'\b[0-9]+(?:\.+[0-9]+)*\b', word):
                self.constantsArr.append(word)
            if word in keywords:
                self.keyArr.append(word)
            if word in operators:
                self.opArr.append(word)
            if word in specialCharacters:
                self.specialChArr.append(word)
            if word not in self.keyArr and word not in self.opArr and word not in self.specialChArr and word \
                    not in self.constantsArr:
                self.identifiersArr.append(word)
        fileName.close()

        # prints grammar type arrays
    def printTokenTypes(self):
        print('Keywords: ' + str(self.keyArr) + '\n')
        print('Operators: ' + str(self.opArr) + '\n')
        print('Special Characters: ' + str(self.specialChArr) + '\n')
        print('Identifiers ' + str(self.identifiersArr) + '\n')
        print('Constants ' + str(self.constantsArr) + '\n')


''''The scanner implementation must include an array of the keywords used in the subset of SCL or other
selected programming Language, an array (or list) of the identifiers (variables), and other
tokens (such as operators, keywords, constants, and/or special characters.)'''
