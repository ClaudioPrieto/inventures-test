from itertools import permutations, combinations_with_replacement

def printSolutions(solutions: list):
    if solutions:
        for solution in solutions:
            print(solution) 
    else:
        print("No Solution")

def getAllUniqueCombinations(digitsQuantity: int):
    operations = ['+', '-', '*', '/']
    uniqueOperations = []
    
    for operationsCombination in combinations_with_replacement(operations, digitsQuantity):
        for oper in permutations(operationsCombination):
            if oper not in uniqueOperations:
                uniqueOperations.append(oper)

    return uniqueOperations

def generateFormula(values: set, operations: set) -> str:
    return '{}{}{}{}{}{}{}'.format(values[0], operations[0], values[1], operations[1], values[2], operations[2], values[3])

def generateParenthesisFormula(values: set, operations: set, parentesis: str) -> str:
    currentOperation = 0
    currentValue = 0
    formulaList = list(parentesis)
    for i in range(len(parentesis)):
        if formulaList[i] == '$':
            formulaList[i] = operations[currentOperation]
            currentOperation += 1
        elif formulaList[i] == 'x':
            formulaList[i] = values[currentValue]
            currentValue += 1

    return ''.join(formulaList)