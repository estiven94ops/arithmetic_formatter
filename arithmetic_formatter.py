import re


def arithmetic_arranger(problems, show_answers=True):
        
    problem_size = len(problems)
    if problem_size < 6:
        counter = 0
        for problem in problems:
            has_operator = bool(re.search(r'[+\-]', problem))
            if has_operator:
                counter += 1 
                
        if counter == problem_size:
            counter2 = 0 
            for problem in problems:
                number_list = problem.split()
                if number_list[0].isnumeric() and number_list[2].isnumeric():
                    counter2 += 1
            if counter2 == problem_size: 
                counter3 = 0
                for problem in problems:
                    number_list = problem.split()
                    number1 = len(number_list[0]) 
                    number2 = len(number_list[2])  
                    if number1 < 5 and number2 < 5:
                        counter3 += 1
                if counter3 == problem_size:
                    topSentence = ""
                    bottomSentence = ""
                    lastSentence = ""
                    lines = ""
                    operation1 = (problems[0]).split()
                    number1 = str(operation1[0])
                    operator = str(operation1[1])
                    number2 = str(operation1[2])
                    if operator == "+":
                        number3 = int(number1) + int(number2)
                    else:
                        number3 = int(number1) - int(number2)
                    count_lines = int(len(str(max(int(number1), int(number2))))) + 2
                    count_spaces = (count_lines - int(len(str(abs(number3))))) 
                    if len(number1) > len(number2):
                        topSentence = "  " + number1
                        bottomSentence = operator + " " * (1 + (len(number1) - len(number2))) + number2
                        lines =  lines  + ("-" * (len(number1) + 2))
                    else:
                        topSentence = " " * (2 +(len(number2) - len(number1))) + number1
                        bottomSentence =  operator + " " + number2
                        lines =  lines + ("-" * (len(number2) + 2))
                        
                    if number3 < 0:
                        lastSentence = lastSentence  + ((" ") * (count_spaces - 1)) + str(number3)
                        print(lastSentence)
                    else:
                        lastSentence = lastSentence + ((" ") * count_spaces)  + str(number3)
                    
                    


                    for problem in problems[1:]:
                        operation = problem.split()
                        number1 = str(operation[0])
                        operator = str(operation[1])
                        number2 = str(operation[2])
                        if operator == "+":
                            number3 = int(number1) + int(number2)
                        else:
                            number3 = int(number1) - int(number2)
                        separator = "    "
                        count_lines = int(len(str(max(int(number1), int(number2))))) + 2
                        count_spaces = abs(count_lines - int(len(str(abs(number3))))) 

                        if len(number1) > len(number2):
                            topSentence = topSentence + separator + "  " + number1
                            bottomSentence = bottomSentence + separator + operator + " " * (1 + (len(number1) - len(number2))) + number2
                            lines =  lines + separator + ("-" * (len(number1) + 2))
                            
                            
                        else:
                            topSentence = topSentence + separator + " " * (2 +(len(number2) - len(number1))) + number1
                            bottomSentence = bottomSentence + separator + operator + " " + number2
                            lines =  lines + separator + ("-" * (len(number2) + 2))
                            
                        if number3 < 0:
                            lastSentence = lastSentence + separator + ((" ") * (count_spaces - 1)) + str(number3)
                        else:
                            
                            lastSentence = lastSentence + separator + ((" ") * count_spaces)  + str(number3)
                       
                    

                    
                    arranged_problems = f"{topSentence}\n{bottomSentence}\n{lines}"
                    #print(topSentence)
                    #print(bottomSentence)
                    #print(lines)
                    #print(lastSentence)
                    if show_answers:
                        arranged_problems += "\n" + lastSentence
                    return arranged_problems

                else:
                    return ("Error: Numbers cannot be more than four digits.")
            else:    
                return ("Error: Numbers must only contain digits.")              
        else:
            return ("Error: Operator must be '+' or '-'.")




    else:
        return ('Error: Too many problems.')
    
       
    
if __name__ == "__main__":
    #print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
    #print(f'\n{arithmetic_arranger(["1 + 2", "1 - 9380"])}')
    #print(f'\n{arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])}')
    #print(f'\n{arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])}')
    #print(f'\n{arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])}')
    #print(f'\n{arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])}')
    #print(f'\n{arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])}')
    #print(f'\n{arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])}')
    #print(f'\n{arithmetic_arranger(["3 + 855", "988 + 40"])}')
    print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"])}')