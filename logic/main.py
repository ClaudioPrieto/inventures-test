from itertools import permutations
from helpers import getAllUniqueCombinations, printSolutions, generateFormula

def compute25(numbers: str, target: int) -> list:

    numbersArray = list(numbers)
    solutions = []
    
    for operationsCombination in getAllUniqueCombinations(len(numbersArray) - 1):
            currentFormula = generateFormula(numbersArray, operationsCombination)
            if currentFormula not in solutions and eval(currentFormula) == target:
                solutions.append(currentFormula)
    
    return solutions
                
def compute25NoOrder(numbers: str, target: int) -> list:
    
    numbersArray = list(numbers)  
    solutions = []

    for values in permutations(numbersArray):
        for operationsCombination in getAllUniqueCombinations(len(numbersArray) - 1):
            currentFormula = generateFormula(values, operationsCombination)
            if currentFormula not in solutions and eval(currentFormula) == target:
                solutions.append(currentFormula)
    
    return solutions
 
if __name__ == "__main__":
    
    input = "3671"
    
    printSolutions(compute25(input, 25))
    print('-------')
    printSolutions(compute25NoOrder(input, 25))
    
    