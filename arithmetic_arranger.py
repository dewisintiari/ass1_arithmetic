def error_handling(num1, num2, operator):

    if len(num1) > 4:
        return "Error: Numbers cannot be more than four digits."
    
    elif len(num2) > 4:
        return "Error: Numbers cannot be more than four digits."
    
    elif operator != '+':
        if operator != '-':
            return "Error: Operator must be '+' or '-'."

    else:
        try:
            int(num1)
            int(num2)
        except :
            return "Error: Numbers must only contain digits."
    return ""

def arithmetic_arranger(problems, displayMode=False):

    # problems is in format "number 1 + operator + number 2" displayMode to show/not the solution    
    # The number of inputs for the calculation cannot be more than 5
   
    if len(problems) > 5:
        return "Error: Too many problems."
        quit()

    line1 = line2 = line3 = line4 = ""
    hspace = "    "

    for problem in problems:
        
        num1 = problem.split()[0]
        num2 = problem.split()[2]
        operator = problem.split()[1]

        # test if all conditions are satisfied
        test = error_handling(num1, num2, operator)
        if test != "":
            return test
            quit()

        space = max(len(num1), len(num2))
        line1 += num1.rjust(space+2)       
        line2 += operator + " " + num2.rjust(space)
        line3 += '-' * (space+2)
        if displayMode == True:
            val1 = int(num1)
            val2 = int(num2)
            if operator == '+':
                result = val1 + val2
            else:
                result = val1 - val2
            line4 += str(result).rjust(space+2)

        space = max(len(num1), len(num2))
        line1 += num1.rjust(space+6)       
        line2 += operator.rjust(5) + " " + num2.rjust(space)
        line3 += hspace + '-' * (space+2)
        if displayMode == True:
            val1 = int(num1)
            val2 = int(num2)
            if operator == '+':
                result = val1 + val2
            else:
                result = val1 - val2
            line4 += hspace + str(result).rjust(space+2)

    if displayMode == True:
        return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
        print('ok')
    else:
        return line1 + '\n' + line2 + '\n' + line3
