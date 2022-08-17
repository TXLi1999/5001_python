'''
Tuoxin Li
CS 5001 Project 9
04/7/2022

'''
#Possible words
dictionary = {
    "ancy" : "hide",
    "nevr" : "meet",
    "cok" : "me",
    "he" : "mark",
    "ite" : "sponsor",
    "rond" : "at",
    "elt" : "during",
    "tiht" : "midnight",
    "hnd" : "noon",
    "hen" : "dawn",
    "singlar" : "by",
    "minr" : "by",
    "rew" : "oaktree",
    "smply" : "fountain",
    "ight" : "farmhouse",
    }




def main():
    # open both files
    file1 = open("file1.txt", "r",encoding='utf-8')
    file2 = open("file2.txt", "r",encoding='utf-8')

    # use sets to find the unique words
    file1_set = set()
    file2_set = set()

    # loop through each file and add line by line into the set
    for i in file1:
        for j in i.split(" "):
            file1_set.add(j.strip())

    # file2
    for i in file2:
        for j in i.split(" "):
            file2_set.add(j.strip())

    # determine which words are difference in each
    # print the difference between file1 and file2
    dif1=file1_set.difference(file2_set)
    dif2=file2_set.difference(file1_set)
    dif_full=dif1.copy()
    dif_full.update(dif2)
    #list=list(dif_full)
    # print the difference between file2 and file1
    print("The words in file 1 but not in file 2 are", dif1,"\nThe words in file 2 but not in file 1 are", dif2,"\nThe whole difference is",dif_full)
    print("The hidden infomation is : ",end=" ")
     # replace the appropriate words using the dictionary
    for key,value in dictionary.items():
        if key in dif_full:
            print(value,end=" ")
   
    # close files
    file1.close()
    file2.close()

main()