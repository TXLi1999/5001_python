'''
Classes of errors include: syntax, convention, logic, and runtime

Describe each of these error types. 

Syntax: 
Convention: 
Logic: 
Runtime: 

1. Locate and fix all syntax errors so the code will run.
2. Identify convention errors. 
3. Can you spot any logic errors?
 
For runtime errors we'll need what we just learned

1. Review the below code and think about what could go wrong during runtime. 
2. Add comments for exceptions you can check for. 
3. Start by protecting your main with a try block and then adding excepts for raised exceptions.

Note: once you are handling an exception you lose the stack trace
'''

'''

Errors:
 
Syntax
for i in range(len(grades)): 
    temp = grades[i].split("-")

def cal_final_grade(grades)
all_grades = {}
all_grades[index]

Logic
file = open(file_name, "w")
return avg[0] / P_LABS + avg[1] / P_QUIZZES + avg[2] / P_TESTS + avg[3] / P_ICES
return avg[0] / P_LABS + avg[0] / P_QUIZZES + avg[0] / P_TESTS + avg[0] / P_ICES

file.close()

Convention

TOTAL
calFinalGrade


'''

#create your own exception
class FileFormatError(Exception):
    def __init__(self):
        self.message = "File in incorrect format"


def get_avg(list_num):
    
    #check type of input
    if type(list_num) != list:
        raise TypeError
        
    total = 0.0
    
    for i in range(len(list_num)):
        total += list_num[i]
    
    #manual check needed here because we want to kiss and move on
    if len(list_num) == 0 : return 0
    
    return total / len(list_num)
   

def cal_final_grade(grades):
    
    #check type
    if type(grades) != list:
        raise TypeError
    
    P_LABS = .5
    P_TESTS = .2
    P_QUIZZES = .25
    P_ICES = .05

    labs = []
    quiz = []
    tests = []
    ices = []
           
    for i in range(len(grades)):
        temp = grades[i].split("-")
        
        #make sure the input is correct
        if not temp[1].strip().isdecimal(): raise FileFormatError
        
        if temp[0].strip() == "LAB":
            labs.append(float(temp[1]))
            
        elif temp[0].strip() == "QUIZ":
            quiz.append(float(temp[1]))
            
        elif temp[0].strip() == "TEST":
            tests.append(float(temp[1]))
            
        elif temp[0].strip() == "ICE":
            ices.append(float(temp[1]))
          
        else:
            raise FileFormatError
                
    avg = [get_avg(labs), get_avg(quiz), get_avg(tests), get_avg(ices)]
    
    return avg[0] * P_LABS + avg[1] * P_QUIZZES + avg[2] * P_TESTS + avg[3] * P_ICES
    
#Protect your main code with a try block
def main():
    
    file_name = input("Please enter grade file : ")
    
    try:
        file = open(file_name, "r")
        all_grades = []
            
        for line in file:
            grades = line.split(",")
            first = grades[0]
            last = grades[1]
            
            final_grade = cal_final_grade(grades[2:])
            
            print("Final grade for ",last, ",",first," is :",f"{final_grade:.2f}")
            all_grades.append(final_grade)
       
       #input check with control flow loop
        while(True):
            try:
                selection = input("Do you wish to save the results? (Y or N)")
                if selection != "Y" and selection != "N": raise ValueError
                break
            except ValueError:
                print("Value Error : That wasn't an option.")
                
        if selection == "Y":
            out_file_name = input("Please enter new file name : ")
            out_file = open(out_file_name,"w")
            file.seek(0)
            index = 0
            for line in file:
                out_file.write(line.strip() + "," + str(all_grades[index]) + "\n")
                index += 1
            out_file.close()
        elif selection == "N":
            print("Then why did I go through all of the trouble of calculating grades?")
        #file.close()
        
    except FileNotFoundError:
        print("Unable to open file. It doesn't appear to exist. Check your spelling and path. \nProgram will not continue")
    except OSError:
        print("Unable to write file or other OS error has occured")
        #out_file.close()
        #file.close()
    except TypeError:
        print("Unexpected type in function.")
        #out_file.close()
        #file.close()
    except FileFormatError:
        print("File was not in the correct format")
    except Exception as error:
        print("unhandled exception occured")
        #print(error)
    finally:
        #out_file.close()
        file.close()
        print("Program complete")
   
main()