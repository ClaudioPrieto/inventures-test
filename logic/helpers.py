from itertools import permutations, combinations_with_replacement

def printSolutions(solutions: list):
    for solution in solutions:
        print(solution)

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