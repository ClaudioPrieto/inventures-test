from itertools import permutations
from helpers import getAllUniqueCambinations, printSolutions

def compute25(numbers: str, target: int) -> list:

    numbersArray = list(numbers)
    solutions = []
    
    for operationsCombination in getAllUniqueCambinations(len(numbersArray) - 1):
            currentFormula = ''.join([x for y in zip(numbersArray, operationsCombination) for x in y] + [numbersArray[-1]])
            if currentFormula not in solutions and eval(currentFormula) == target:
                solutions.append(currentFormula)
    
    return solutions
                
def compute25NoOrder(numbers: str, target: int) -> list:
    
    numbersArray = list(numbers)  
    solutions = []

    for values in permutations(numbersArray):
        for operationsCombination in getAllUniqueCambinations(len(numbersArray) - 1):
            currentFormula = ''.join([x for y in zip(values, operationsCombination) for x in y] + [values[-1]])
            if currentFormula not in solutions and eval(currentFormula) == target:
                solutions.append(currentFormula)
    
    return solutions
 
if __name__ == "__main__":
    
    input = "3671"
    
    printSolutions(compute25(input, 25))
    #printSolutions(compute25NoOrder(input, 25))
    
    