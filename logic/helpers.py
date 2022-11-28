from itertools import permutations, combinations_with_replacement

def printSolutions(solutions):
    for solution in solutions:
        print(solution)

def getAllUniqueCambinations(digitsQuantity):
    
    operations = ['+', '-', '*', '/']
    uniqueOperations = []
    
    for operationsCombination in combinations_with_replacement(operations, digitsQuantity):
        for oper in permutations(operationsCombination):
            if oper not in uniqueOperations:
                uniqueOperations.append(oper)
    
    return uniqueOperations
            