from itertools import permutations
from helpers import getAllUniqueCombinations, printSolutions, generateFormula, generateParenthesisFormula

def compute25(numbers: str, target: int) -> list:
    numbersArray = list(numbers)
    operationsCombinations = getAllUniqueCombinations(len(numbersArray) - 1)
    solutions = []
    
    for combination in operationsCombinations:
            currentFormula = generateFormula(numbersArray, combination)
            if currentFormula not in solutions and eval(currentFormula) == target:
                solutions.append(currentFormula)
    
    return solutions
                
def compute25NoOrder(numbers: str, target: int) -> list:
    numbersArray = list(numbers)
    operationsCombinations = getAllUniqueCombinations(len(numbersArray) - 1)
    solutions = []

    for values in permutations(numbersArray):
        for combination in operationsCombinations:
            currentFormula = generateFormula(values, combination)
            try:
                evaluation = eval(currentFormula)
                if currentFormula not in solutions and evaluation == target:
                    solutions.append(currentFormula)
            except ZeroDivisionError:
                print ("WARNING: Invalid Equation")
    
    return solutions
 
def compute25Parenthesis(numbers: str, target: int) -> list:
    numbersArray = list(numbers)
    parenthesisCombinations = ['x$x$x$x', '(x$x)$x$x', 'x$(x$x)$x', 'x$x$(x$x)', '(x$x)$(x$x)', '(x$x$x)$x', 'x$(x$x$x)', '((x$x)$x)$x', '(x$(x$x))$x', 'x$((x$x)$x)', 'x$(x$(x$x))']
    operationsCombinations = getAllUniqueCombinations(len(numbersArray) - 1)
    solutions = []
    
    for values in permutations(numbersArray):
        for operCombination in operationsCombinations:
            for parenthCombination in parenthesisCombinations:
                currentFormula = generateParenthesisFormula(values, operCombination, parenthCombination)
                try:
                    evaluation = eval(currentFormula)
                    if currentFormula not in solutions and evaluation == target:
                        solutions.append(currentFormula)
                except ZeroDivisionError:
                    print ("WARNING: Invalid Equation")
    
    return solutions
 
if __name__ == "__main__":
    
    input = "8251"
    
    printSolutions(compute25(input, 25))
    print('-------')
    printSolutions(compute25NoOrder(input, 25))
    print('-------')
    printSolutions(compute25Parenthesis(input, 25))
    
    