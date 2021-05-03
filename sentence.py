'''
~ represents 'not'
-> represents 'implies'
v represents 'or'
^ represents 'and'
<-> represents 'iff'
'''


class sentence:
    def __init__(self):
        self.statements = []
        self.resolution = []
        
    def printStatements(self):
        for i in self.statements:
            print()
            for j in i:
                print(j.getString())
        
    def addStatement(self,s):
        terms = []
        counter = 0
        para = True
        
        if "(" not in s:
            terms.append(term(s))
            para = False
        
        while (counter < len(s)) and para == True:
            current = s[counter]
            if current == "(":
                temp = ""
                while s[counter] != ")" and counter < len(s):
                    temp += s[counter]
                    counter += 1
                terms.append(term(temp+")"))
                counter += 1
            else:
                terms.append(term(current))
                counter += 1
                
        counter = 0
        while counter < len(terms):
            if terms[counter].getString() == "~":
                terms.pop(counter)
                terms[counter].negate()
            counter += 1
            
        self.statements.append(terms)

    def createResolutionStart(self):
        #print(self.statements[0][0].getString())
        for j in range(len(self.statements)):
            for i in self.statements[j]:
                count = 0
                current = []
                isor = False
                s = i.getString()
                while count < len(s):
                    if s[count] == "(":
                        #print("yes")
                        count += 1
                        statement = ""
                        while s[count] != ")" and count < len(s):
                            statement += s[count]
                            count += 1
                        
                        if "^" in statement:
                            y = statement.split("^")
                            for r in y:
                                current.append(r)
                        
                        elif "v" in statement:
                            x = statement.split("v")
                            current.append(x)
                            
                    if s[count] == "v":
                        isor = True
                    
                    count += 1
                    
                for i in current:
                    self.resolution.append(i)
                #if isor:
                    #current
                    
                
        
                
            
        print(self.resolution)
        
        
    def solve(self):
        count = [0]*len(self.statements)
        while True:
            for i in range(len(count)):
                if count[i] >= len(self.statements[i]):
                    break
        
            
        
     
class term:
    def __init__(self,s):
        self.string = s
        if "<" in self.string:
            self.convertIff()
        elif "-" in self.string:
            self.convertImplies()
        
    def getString(self):
        return self.string
    
    def convertIff(self):
        if "<" not in self.string:
            return None
        
        if self.string[0] == "(":
            self.string = self.string[1::]
        if self.string[len(self.string) - 1] == ")":
            self.string = self.string[0:len(self.string)-1]
        
        counter = 0
        while counter < len(self.string):
           if self.string[counter] == "<":
               break
           counter += 1
           
        newString = "( ~" + self.string[0:counter] + "^ ~" + self.string[counter+3::] + ") v (" + self.string[0:counter] + "^" + self.string[counter+3::] + ")"
        
        self.string = newString
        return newString
    
    def convertImplies(self):
        return None
    
    def negate(self):        
        count = 0
        alreadyNegated = False
        if self.string[0] == "~":
            self.string = self.string[1::]
            return self.string
        while count < len(self.string):
            # these characters don't really matter
            if self.string[count] == "~":
                self.string = self.string[0:count] + self.string[count+1:]
                alreadyNegated = True
                
            elif self.string[count] == "(" or self.string[count] == ")" or self.string[count] == " ":
                count += 1
                continue
            else:
                if self.string[count] == "^":
                    self.string = self.string[0:count] + "v" + self.string[count+1::]
                    count +=1
                    
                elif self.string[count] == "v":
                    self.string = self.string[0:count] + "^" + self.string[count+1::]
                    count += 1
                    
                else:
                    if alreadyNegated:
                        alreadyNegated = False
                        count += 1
                        continue
                    self.string = self.string[0:count] + "~" + self.string[count::]
                    count += 2
        
        return self.string
    
    
    

temp = sentence()
temp.addStatement("~(P <-> Q)")  
temp.addStatement("~(Q <-> R)")
temp.addStatement("~(P <-> R)")  
temp.createResolutionStart()






















