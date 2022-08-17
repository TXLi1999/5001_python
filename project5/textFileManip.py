'''
Tuoxin Li
02/24/2022
Using this project to do something with the text file
'''

import sys

def all_upper_case(fileName):
    '''
    Function: uppercase all the letters in the specified file
    params:filename
    return:create a new file
    '''
    #print feedback
    print("Converting all letters to upper case")
    #open input file
    file = open(fileName, "r")
    #get contents as a string
    contents=file.read()
    #convert contents to upper case
    contents_upper=contents.upper()
    out_file_name=input("Please enter output file name:")
    out_file = open(out_file_name,"w")
    #send contents to output file
    out_file.write(contents_upper)
    #close all file hables
    out_file.close()
    file.close


def remove_a_letter(fileName, letter):
    '''
    Function: remove the specified letter in the specified file
    params:filename
    return:create a new file
    '''
    print("Removing letter : ", letter, "from file : ", fileName)
    #open input file
    file = open(fileName, "r")
    #get contents as a string
    contents=file.read()
    #remove the letter
    contents_removeL=contents.replace(letter,"")
    out_file_name=input("Please enter output file name:")
    out_file = open(out_file_name,"w")
    #send contents to output file
    out_file.write(contents_removeL)
    #close all file hables
    out_file.close()
    file.close


def remove_a_word(fileName, word):
    '''
    Function: remove the specified word in the specified file
    params:filename
    return:create a new file
    '''
    print("Removing word : ", word, "from file : ", fileName)
    #open input file
    file = open(fileName, "r")
    #get contents as a string
    contents=file.read()
    #remove the word and a space in front of the word
    contents_removeW=contents.replace(" " + word,"")
    out_file_name=input("Please enter output file name:")
    out_file = open(out_file_name,"w")
    #send contents to output file
    out_file.write(contents_removeW)
    #close all file hables
    out_file.close()
    file.close

def reverse_file(fileName):
    '''
    Function: reverse the words in the specified file
    params:filename
    return:create a new file
    '''
    print("Reversing file : ", fileName)
    #open input file
    file = open(fileName, "r")
    #get contents as a string
    contents=file.read()
    #split the string so we can operate the words
    contents_split=contents.split(" ")
    #make a string to let the words go from the end to the first
    revers_contents=''.join(contents_split[::-1])
    #A slight problem is that because we split by a space, so the result won't show space
    out_file_name=input("Please enter output file name:")
    out_file = open(out_file_name,"w")
    #send contents to output file
    out_file.write(revers_contents)
    #close all file hables
    out_file.close()
    file.close


def pattern_count(fileName, letter):
    '''
    Function: count how many times the specified letter appears
    params:filename
    return:print
    '''
    #open input file
    file = open(fileName, "r")
    #get contents as a string
    contents=file.read()
    #set a count number
    count=0
    for i in contents:
        if i == letter: #when the specified letter appears, count 1
            count +=1
    print("The pattern appears ", count, "times!")

def word_count(fileName, word):
    '''
    Function: count how many times the specified word appears
    params:filename
    return:print
    '''
    #open input file
    file = open(fileName, "r")
    #get contents as a string
    contents=file.read()
    #set a count number
    count=0
    #split the string so we can operate the words
    contents_split=contents.split(" ")

    for i in contents_split:
        if i == word: #when the specified letter appears, count 1
            count +=1
    print("The word appears ", count, "times!")

def encode_file(fileName):
    '''
    Function: increase the ASCII of the letters in the specified file by 1
    params:filename
    return:create a new file
    '''
    print("Encoding file : ", fileName)
    #open input file
    file = open(fileName, "r")
    #get contents as a string
    contents=file.read()
    #make the string into list
    new_content=list(contents)
    for i,char in enumerate(new_content):
        #we don't want see puncuations, spaces are converted
        if new_content[i] != " " and new_content[i] != "," and new_content!="." and new_content[i] !="\n": #some elements are not included, here is to show some of the details are considered
            #ord is to change elements into numerical mode, chr is to change numeric into the specified elements
            new_content[i] =chr(ord(char)+1)
    #transfer content into string
    output= ''.join(new_content)
    out_file_name=input("Please enter output file name:")
    out_file = open(out_file_name,"w")
    #send contents to output file
    out_file.write(output)
    #close all file hables
    out_file.close()
    file.close

def decode_file(fileName):
    '''
    Function: decrease the ASCII of the letters in the specified file by 1
    params:filename
    return:create a new file
    '''
    print("Decoding file : ", fileName)
    #open input file
    file = open(fileName, "r")
    #get contents as a string
    contents=file.read()
    #make the string into list
    new_content=list(contents)
    for i,char in enumerate(new_content):
        if new_content[i] != " " and new_content[i] != "," and new_content!="." and new_content[i] !="\n": #some elements are not included, here is to show some of the details are considered
            new_content[i] =chr(ord(char)-1)
    #transfer content into string
    output= ''.join(new_content)
    out_file_name=input("Please enter output file name:")
    out_file = open(out_file_name,"w")
    #send contents to output file
    out_file.write(output)
    #close all file hables
    out_file.close()
    file.close

def exclame(fileName):
    '''
    Function: Change all the period into exclamation
    params:filename
    return:create a new file
    '''
    print("Exclaming file : ", fileName)
    #open input file
    file = open(fileName, "r")
    #get contents as a string
    contents=file.read()
    #replace all the period into exclamation
    content_new=contents.replace(".","!")
    out_file_name=input("Please enter output file name:")
    out_file = open(out_file_name,"w")
    #send contents to output file
    out_file.write(content_new)
    #close all file hables
    out_file.close()
    file.close

def switch(fileName):
    '''
    Function: change her to him
    params:filename
    return:create a new file
    '''
    print("Gender switch file : ", fileName)
    #open input file
    file = open(fileName, "r")
    #get contents as a string
    contents=file.read()
    #Switch she to he
    content_new=contents.replace("she","he")
    content_new=contents.replace("She","He")
    content_new=contents.replace("her","his")
    #content_new=contents.replace("he","she")
    #content_new=contents.replace("He","She")
    #content_new=contents.replace("h1e","he")
    #content_new=contents.replace("H1e","He")
    out_file_name=input("Please enter output file name:")
    out_file = open(out_file_name,"w")
    #send contents to output file
    out_file.write(content_new)
    #close all file hables
    out_file.close()
    file.close
def main():
    if (len(sys.argv)>2): ## if the user called a file after this python file, run!
        if sys.argv[1] == "Upper":
            all_upper_case(sys.argv[2])  
        if sys.argv[1] == "RemoveL":
            Rmvletter=input("What is the letter that you want to remove?")
            remove_a_letter(sys.argv[2],Rmvletter)
        if sys.argv[1] == "RemoveW":
            Rmvword=input("What is the word that you want to remove?")
            remove_a_word(sys.argv[2],Rmvword)
        if sys.argv[1] == "Reverse":
            reverse_file(sys.argv[2])
        if sys.argv[1] == "Lcount":
            patterns=input("Please input the pattern: ")
            pattern_count(sys.argv[2],patterns)
        if sys.argv[1] == "WCount":
            word=input("Please input the pattern: ")
            word_count(sys.argv[2],word)
        if sys.argv[1] == "Encode":
            encode_file(sys.argv[2])
        if sys.argv[1] == "Decode":
            decode_file(sys.argv[2])
        if sys.argv[1] == "Exclamation":
            exclame(sys.argv[2])
        if sys.argv[1] == "GenderSwitch":
            switch(sys.argv[2])
        if sys.argv[1] != "Upper" and sys.argv[1] != "RomoveL" and sys.argv[1] != "RemoveW" and sys.argv[1] !="Reverse" and sys.argv[1] != "Lcount" and sys.argv[1] != "WCount" and sys.argv[1] !="Encode" and sys.argv[1] !="Decode" and  sys.argv[1] !="Exclamation" and sys.argv[1] !="GenderSwitch":
            print("Functions you want to perform- file name- word/letter to remove \nPossible inputs are: Upper, RomoveL, RemoveW, Reverse, Lcount, WCount, Encode, Decode, Exclamation, GenderSwitch")
    else:
        print("Functions you want to perform- file name- word/letter to remove \nPossible inputs are: Upper, RomoveL, RemoveW, Reverse, Lcount, WCount, Encode, Decode, Exclamation, GenderSwitch")



main()

