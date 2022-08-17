'''
Tuoxin Li
Project8
4/2/2022
'''
#create your own exception


class FileFormatError(Exception):
    def __init__(self):
        self.message = "File in incorrect format"

def get_avg(list_num):
    '''
    Function: calculate the average of a list
    Params: list_num--list
    '''
    #check type of input
    if type(list_num) != list:
        raise TypeError
        
    total = 0.0
    
    for i in range(len(list_num)):
        total += list_num[i]
    
    #manual check needed here because we want to kiss and move on
    if len(list_num) == 0 : return 0
    
    return total / len(list_num)
def monthconverter(month):
    '''
    Function:convert the month from numeric form into word form
    params:integer
    '''
    if month>12 or month<1 : #Check input
        raise TypeError("Value hould between 01 and 12")
    if month == 1:
        return "Jan"
    if month == 2:
        return "Feb"
    if month == 3:
        return "Mar"
    if month == 4:
        return "Apr"
    if month == 5:
        return "May"
    if month == 6:
        return "Jun"
    if month == 7:
        return "Jul"
    if month == 8:
        return "Aug"
    if month == 9:
        return "Sep"
    if month == 10:
        return "Otc"
    if month == 11:
        return "Nov"
    if month == 12:
        return "dec"

def print_avgs(data, city, starting_year, month, out_file_name): 
    '''
    Function:calculate the average pcrp of a city and output it in specified file
    Params: data--list  city--string  starting_year--int  out_file_name--file name(best to be like something.txt)
    Return: output a file
    '''
    #Check type error
    if type(data) != list: raise TypeError
    if  type(city) != str: raise TypeError
    if type(starting_year) != int: raise TypeError
    out_file = open(out_file_name,"w") #Write a file
    out_file.write(city.strip() +"Average Rainfall since "+monthconverter(month)+" :"+"\n") #write in the header
    for year in range(starting_year,2022):
        out_file.write(str(year) +" : "+  f"{get_avg(data[year-2010]):.3f}"  "\n") #write in the info
    out_file.close() #Always colse file after opening a file

def main():
    try:
        file_input=input("What's the file name you want to import?\n") #Ask for input file
        #try:
        file = open(file_input, "r") #open file
        lines=file.readlines()[1:] #ignore the header
        year_month_fall = [] #create a list for dragging the info out of the csv
        portland_data=[[],[],[],[],[],[],[],[],[],[],[],[]] #Create a list

        start_year=int(input("What's the starting year?\n")) #ask for which year to start
        start_month=int(input("From what month do you wish to start?(from 1 to 12)\n"))

        for line in lines:
            #Create a list to put the pcrp and the corresponding year and month. The form is "year-pcrp"
            rain=line.split(",")
            year_o = rain[3].strip('"').split("-")[0] #take the year data
            month_o = rain[3].strip('"').split("-")[1] #take the month data
            prcp= rain[9].strip('"')    #take the rainfall data
            yearprcp=str(year_o)+"-"+str(month_o)+"-"+str(prcp)
            year_month_fall.append(yearprcp)  

        for yy in range(2010,2022):
            for i in year_month_fall:
                year = int(i.strip("'").split("-")[0])
                month = int(i.strip("'").split("-")[1])
                string_rainfall = i.strip("'").split("-")[2]
                if year == yy and string_rainfall != '' and month>=start_month: #check if the value is corresponding to the year and if it's the month we want
                    portland_data[yy-2010].append(float(string_rainfall))
    
        while(True):
            try:
                selection = input("Do you wish to save the results? (Y or N)")
                if selection != "Y" and selection != "N": raise ValueError
                break
            except ValueError:
                print("Value Error : That wasn't an option.")
        
        if selection =="Y":
            #Output a file recording the infomation
            output_name=input("What's the name of the output file?\n")
            print_avgs(portland_data,"Portland",start_year,start_month,output_name)
        elif selection == "N":
            #Print the result
            print("Average rainfall since "+monthconverter(start_month)+" :")

            for year in range(start_year,2022):
                print(str(year) + " : " + f"{get_avg(portland_data[year-2010]):.3f}")

    except FileNotFoundError:
        print("Unable to open file. It doesn't appear to exist. Check your spelling and path. \nProgram will not continue")
    except OSError:
        print("Unable to write file or other OS error has occured")
    except TypeError:
        print("Unexpected type in function.")
    except FileFormatError:
        print("File was not in the correct format")
    except Exception:
        print("unhandled exception occured")
    finally:
        file.close()
        print("Program complete")

main()