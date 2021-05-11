'''
~ represents 'not'
-> represents 'implies'
v represents 'or'
^ represents 'and'
<-> represents 'iff'
'''
import itertools

'''
The Sentence class parses the input from the user into a list of resolution solvable pairs.
'''
class Sentence:
    def __init__(self):
        self.statements = []    # stores the list of statements
        self.resolution = []    # stores the final resolution "pairs"

    '''
    Print the statements.
    '''
    def printStatements(self):
        for i in self.statements:
            print()
            for j in i:
                print(j)

    '''
    Print the final resolution "pairs".
    '''
    def printResolution(self):
        print(self.resolution)

    '''
    Add a statement after parsing.
    '''
    def addStatement(self, s):
        terms = []      # stores the terms in a statement
        counter = 0     # while loop counter
        para = True     # boolean for if there are parentheses

        s = s.strip()

        if "(" not in s:
            terms.append(Term(s))
            para = False

        while counter < len(s) and para:
            current = s[counter]
            if current == "(":
                temp = ""
                while s[counter] != ")" and counter < len(s):
                    temp += s[counter]
                    counter += 1
                terms.append(Term(temp+")"))
                counter += 1
            else:
                if current.isalpha() or current == "~":
                    terms.append(Term(current))
                counter += 1

        counter = 0
        while counter < len(terms):
            if str(terms[counter]) == "~":
                terms.pop(counter)
                terms[counter].negate()
            counter += 1

        for t in terms:
            if str(t) == "" or str(t) == "\n":
                terms.remove(t)
        self.statements.append(terms)

    '''
    Create all the pairs that are needed to do the resolution.
    '''
    def createResolutionStart(self):
        for j in range(len(self.statements)):
            for i in self.statements[j]:
                # print(i.getString())
                count = 0
                current = []
                isor = False
                # s = i.getString()
                s = str(i)
                while count < len(s):
                    if s[count] == "(":
                        count += 1
                        statement = ""
                        # current statement is everything inside the parentheses, if there are parentheses
                        while s[count] != ")" and count < len(s):
                            statement += s[count]
                            count += 1

                        if "^" in statement:
                            for r in statement.split("^"):
                                current.append(r.strip())

                        elif "v" in statement:
                            L = []
                            for r in statement.split("v"):
                                L.append(r.strip())
                            current.append(L)

                    elif s[count] == "v":
                        isor = True
                        for r in s.split("v"):
                            current.append(r.strip())

                    # elif s[count] == "^":
                    #     print(s)
                    #     L = []
                    #     for r in s.split("^"):
                    #         L.append(r.strip())
                    #     current.append(L)

                    count += 1

                if isor:
                    self.resolution.append(current)
                    continue

                for c in current:
                    self.resolution.append(c)

                if len(str(i)) == 1:
                    self.resolution.append([str(i)])

    def loop(self, res):
        graph = dict()
        L = []
        visited = set()
        # used = dict()
        # def sorter(v):
        #     return used[v]

        for x in res:
            L.append(tuple(x))
            # used[tuple(x)] = False
            graph[tuple(x)] = [0, None, None]
        while L:
            # print(L)
            breaker = False
            # L.sort(key = sorter)
            for i in range(len(L)):
                # if breaker:
                #     break
                left = L[i]
                for j in range(i+1, len(L)):
                    right = L[j]
                    new_level = max(graph[L[i]][0], graph[L[j]][0]) + 1
                    # print(visited)
                    if (L[i], L[j]) in visited:
                        # print("here")
                        continue
                    if L[i][0].strip("~") == L[j][0].strip("~") and ((L[i][0][0] == "~" and L[j][0][0] != "~") or (L[i][0][0] != "~" and L[j][0][0] == "~")):
                        new = tuple()
                        if len(L[i]) >= 2 and len(L[j]) >= 2:
                            new = (L[i][1], L[j][1])
                            if L[i][1] == L[j][1]:
                                new = tuple([L[i][1]])
                        elif len(L[i]) >= 2 and len(L[j]) < 2:
                            new = tuple([L[i][1]])
                        elif len(L[i]) < 2 and len(L[j]) >= 2:
                            new = tuple([L[j][1]])
                        if new not in L:
                            graph[new] = [new_level, L[i], L[j]]
                        L.remove(L[j]) # find a way to not remove from list without
                        L.remove(L[i])
                        L.append(right)
                        L.append(left)
                        if new != tuple() and new not in L:
                            L.append(new)
                        if (new == tuple()):
                            return graph
                        visited.add((L[i], L[j]))
                        breaker = True
                        break
                    elif len(L[j]) >= 2 and L[i][0].strip("~") == L[j][1].strip("~") and ((L[i][0][0] == "~" and L[j][1][0] != "~") or (L[i][0][0] != "~" and L[j][1][0] == "~")):
                        new = tuple()
                        if len(L[i]) >= 2 and len(L[j]) >= 2:
                            new = (L[i][1], L[j][0])
                            if L[i][1] == L[j][0]:
                                new = tuple([L[i][1]])
                        elif len(L[i]) >= 2 and len(L[j]) < 2:
                            new = tuple([L[i][1]])
                        elif len(L[i]) < 2 and len(L[j]) >= 2:
                            new = tuple([L[j][0]])
                        if new not in L:
                            graph[new] = [new_level, L[i], L[j]]
                        L.remove(L[j])
                        L.remove(L[i])
                        L.append(right)
                        L.append(left)
                        if new != tuple() and new not in L:
                            L.append(new)
                        if (new == tuple()):
                            return graph
                        visited.add((L[i], L[j]))
                        breaker = True
                        break
                    elif len(L[i]) >= 2 and L[i][0].strip("~") == L[j][0].strip("~") and ((L[i][1][0] == "~" and L[j][0][0] != "~") or (L[i][1][0] != "~" and L[j][0][0] == "~")):
                        new = tuple()
                        if len(L[i]) >= 2 and len(L[j]) >= 2:
                            new = (L[i][0], L[j][1])
                            if L[i][0] == L[j][1]:
                                new = tuple([L[i][0]])
                        elif len(L[i]) >= 2 and len(L[j]) < 2:
                            new = tuple([L[i][0]])
                        elif len(L[i]) < 2 and len(L[j]) >= 2:
                            new = tuple([L[j][1]])

                        if new not in L:
                            graph[new] = [new_level, L[i], L[j]]
                        # they get removed and then added back so that they move to the end of the list, giving priority to nodes that have not yet been used, which generally results in a nicer looking graph.
                        L.remove(L[j])
                        L.remove(L[i])
                        L.append(right)
                        L.append(left)

                        if new != tuple() and new not in L:
                            L.append(new)
                        if (new == tuple()):
                            return graph
                        visited.add((L[i], L[j]))
                        breaker = True
                        break
                    elif len(L[i]) >= 2 and len(L[j]) >= 2 and L[i][0].strip("~") == L[j][0].strip("~") and ((L[i][1][0] == "~" and L[j][1][0] != "~") or (L[i][1][0] != "~" and L[j][1][0] == "~")):
                        new = (L[i][1], L[j][1])
                        if L[i][1] == L[j][1]:
                            new = tuple([L[i][1]])
                        if new not in L:
                            graph[new] = [new_level, L[i], L[j]]
                        L.remove(L[j])
                        L.remove(L[i])
                        L.append(right)
                        L.append(left)
                        if new not in L:
                            L.append(new)
                        visited.add((L[i], L[j]))
                        breaker = True
                        break
            if not breaker:
                break
        return graph

    def solve(self):
        L = list(itertools.permutations(self.resolution, len(self.resolution)))
        graphs = []
        min_graph = None
        for combo in L:
            this_graph = self.loop(combo)
            if tuple() in this_graph.keys() and (min_graph == None or len(min_graph) > len(this_graph)):
                min_graph = this_graph
            else:
                graphs.append(this_graph)
        if min_graph != None:
            self.prune_graph(min_graph)
            return min_graph
        elif len(graphs) > 0:
            return graphs[0]

    def prune_graph(self, graph):
        queue = []
        visited = set()
        visited.add(tuple())
        queue.append(tuple())
        while queue:
            v = queue.pop(0)
            left = graph[v][1]
            right = graph[v][2]
            if left != None and left not in visited:
                visited.add(left)
                queue.append(left)
            if right != None and right not in visited:
                visited.add(right)
                queue.append(right)
        not_in = set()
        for k in graph.keys():
            if k not in visited:
                not_in.add(k)
        for n in not_in:
            if graph[n][0] != 0:
                graph.pop(n)




class Term:
    def __init__(self,s):
        self.string = s.strip()
        if "<" in self.string:
            self.convertIff()
        elif "-" in self.string:
            self.convertImplies()

    def __str__(self):
        return self.string

    def convertIff(self):
        # strip parentheses if outside whole string
        if self.string[0] == "(":
            self.string = self.string[1::].strip()
        if self.string[len(self.string) - 1] == ")":
            self.string = self.string[0:len(self.string)-1].strip()

        # find the index of "<"
        index = 0
        while index < len(self.string):
           if self.string[index] == "<":
               break
           index += 1

        first_term = self.string[0:index].strip()
        second_term = self.string[index+3::].strip()
        newString = "(~" + first_term + " ^ ~" + second_term + ") v (" + first_term + " ^ " + second_term + ")"
        self.string = newString
        return newString

    def convertImplies(self):
        # strip parentheses if outside whole string
        if self.string[0] == "(":
            self.string = self.string[1::].strip()
        if self.string[len(self.string) - 1] == ")":
            self.string = self.string[0:len(self.string)-1].strip()

        index = 0
        while index < len(self.string):
           if self.string[index] == "-":
               break
           index += 1

        first_term = self.string[0:index].strip()
        second_term = self.string[index+3::].strip()
        newString = "~" + first_term + "v" + second_term
        self.string = newString
        return newString

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

if __name__ == "__main__":
    # print("STATEMENTS 1: ~(P <-> Q), ~(Q <-> R), ~(P <-> R)")
    temp = Sentence()
    temp.addStatement("~(P <-> Q)")
    temp.addStatement("~(Q <-> R)")
    temp.addStatement("~(P <-> R)")
    # temp.printStatements()
    temp.createResolutionStart()
    temp.printResolution()
    temp.solve()

    # print("STATEMENTS 2: F v G, H ^ (I -> F), H -> ~F, ~(G ^ ~I)")
    temp2 = Sentence()
    temp2.addStatement("F v G")
    temp2.addStatement("H ^ (I -> F)")
    temp2.addStatement("H -> ~F")
    temp2.addStatement("~(G ^ ~I)")
    # temp2.printStatements()
    temp2.createResolutionStart()
    temp2.printResolution()
    temp2.solve()
