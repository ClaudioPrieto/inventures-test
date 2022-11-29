from itertools import permutations
from helpers import getAllUniqueCambinations, printSolutions

def compute25(numbers: str, target: int) -> list:

    numbersArray = list(numbers)
    solutions = []
    
    for operationsCombination in getAllUniqueCambinations(len(numbersArray) - 1):
            currentFormula = '{}{}{}{}{}{}{}'.format(numbersArray[0], operationsCombination[0], numbersArray[1], operationsCombination[1], numbersArray[2], operationsCombination[2], numbersArray[3])
            if currentFormula not in solutions and eval(currentFormula) == target:
                solutions.append(currentFormula)
    
    return solutions
                
def compute25NoOrder(numbers: str, target: int) -> list:
    
    numbersArray = list(numbers)  
    solutions = []

    for values in permutations(numbersArray):
        for operationsCombination in getAllUniqueCambinations(len(numbersArray) - 1):
            currentFormula = '{}{}{}{}{}{}{}'.format(values[0], operationsCombination[0], values[1], operationsCombination[1], values[2], operationsCombination[2], values[3])
            if currentFormula not in solutions and eval(currentFormula) == target:
                solutions.append(currentFormula)
    
    return solutions
 
if __name__ == "__main__":
    
    input = "3671"
    
    printSolutions(compute25NoOrder(input, 25))
    #printSolutions(compute25NoOrder(input, 25))
    
    