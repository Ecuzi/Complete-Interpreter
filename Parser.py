"""
4308 Concepts of Programming Languages
March 26, 2023
Morgan Stafford
Ethan Fitzgerald
Samuel Futral
Adnan Eid
"""
import Scanner


class Parser:
    """example file: D:\Classes\CS 4308\Modules_3_5_7_Project Resources\SCL_Project\welcome.scl"""
    # file to send to scanner
    ScannerFileAddress = input("Enter Address of File: ")

    # runs the scanner from deliverable 1
    scan = Scanner.Scanner(ScannerFileAddress)
    scan.run()

    i = -1  # index assignment for get token
    noComments = scan.ParsedFile
    CurrentToken = ""
    TokenType = 0
    keywordsEntered = 0  # keeps track of if/ how many keywords have been entered
    operatorsEntered = 0  # keeps track of if/ how many operators have been entered
    termsEntered = 0  # keeps track of if/ how many terms have been entered

    def getNextToken(self):  # retrieves the next token from the scanned file that has comments removed
        NextToken = self.noComments[self.i + 1]
        self.i += 1
        return NextToken

    def NextTokenType(self):
        self.CurrentToken = self.getNextToken()
        if self.CurrentToken in self.scan.keyArr:  # keywords type 10
            self.TokenType = 10
        if self.CurrentToken in self.scan.opArr:  # operators type 29
            self.TokenType = 29
        if self.CurrentToken in self.scan.constantsArr:  # constants type 17
            self.TokenType = 17
        if self.CurrentToken in self.scan.specialChArr:  # Special Characters type 38
            self.TokenType = 38
        if self.CurrentToken in self.scan.identifiersArr:  # Identifiers type 56
            self.TokenType = 56
        return self.TokenType

    def EnterExit(self):
        if self.TokenType == 10:
            print('Entering <keywords>')
            self.keywordsEntered += 1
        if self.TokenType == 29:
            print('Entering <operators>')
            self.operatorsEntered += 1
        if self.TokenType == 17:
            print('Entering <terms>')
            self.termsEntered += 1
        if self.TokenType == 38:
            print('Entering <terms>')
            self.termsEntered += 1
        if self.TokenType == 56:
            print('Entering <terms>')
            self.termsEntered += 1
            while self.termsEntered != 0:  # exits out of all terms
                print('Exiting <terms>')
                self.termsEntered -= 1
            while self.operatorsEntered != 0:  # exits out of all operators
                print('Exiting <operators>')
                self.operatorsEntered -= 1
            while self.keywordsEntered != 0:  # exits out of all keywords
                print('Exiting <keywords>')
                self.keywordsEntered -= 1


parser = Parser()

for word in parser.noComments:
    print('Next token is: ' + str(parser.NextTokenType()) + '\n' + 'Next Lexeme is: ' + parser.CurrentToken)
    parser.EnterExit()
    print(' ')