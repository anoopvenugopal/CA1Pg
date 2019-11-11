''' Student record
    1. Created a class for studentrec and declare init function
    2. wrote the driver code for the program
    3. Add display function for viewing the list
    4. sorted the list using bubble sort
    5. validated the input datas using regular expression
    6. created a function for appending data to list
    7. optimised the code
    8. add retrive function'''
import time
import sys
import re

class StudentRec:    
    def __init__(self,stId,stname,coursecode):
        self.stId=stId
        self.stname=stname
        self.coursecode=coursecode    
        
    def showall(self):                 #to view all students          
        print(self.stId,end='\t\t')
        print(self.stname,end='\t\t')
        print(self.coursecode)

class StudentHandler:

    def add(self,student):             #appending data to list
        st.append(student)
        
    def sort(self,s):                 #bubble sort for sorting
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if(int(s[i].stId)>int(s[j].stId)):
                    s[i],s[j]=s[j],s[i]
        return st
    
    def retrieve(self):                #remove the student having lowest IdNo 
        fStd=st[0]
        st.pop(0)
        return fStd
#Driver code        
st=list()
stud=StudentHandler()
while(True):
    choice=int(input(" 1: Press 1 to add students.\n 2: Press 2 to View all students.\n 3: Press 3 to pop the student with lowest ID.\n"))
    if choice==1:
        n=int(input('Enter no of students : '))
        
        print('Students details entry....')
        
        for i in range(n):
            print('Student : ',i+1)
            stId=input('\tID:')
            check=re.match("[0-9]{8}$",stId)
            while(not check):             
                print("\n Id must be 8 integers.")
                stId=input('\tID:')
                check=re.match("[0-9]{8}$",stId)            
                
            stname=input('\tName:')            
            
            coursecode=input('\tCourseCode:')
            while(not len(coursecode)==7):
                print("\n The course id must be 7 characters long.")
                coursecode=input('\tCourseCode:')
            std=(StudentRec(stId,stname,coursecode))
            stud.add(std)
        print('Successfuly added students to Record')
                
    elif choice==2:                 # for showall data
        st=stud.sort(st)
        if (len(st)==0):
            print('****List empty****')
        else:
            print('Student Information')
            print('Student Id\t\tName\t\tCourse Code')
            for i in range(len(st)):
                st[i].showall()
    elif choice==3:
        st=stud.sort(st)
        if (len(st)==0):
            print('****List empty****')
        else:
            a=stud.retrieve()
            print(' Id :'+a.stId+'\tName :'+a.stname+'\tCoursecode :'+a.coursecode)
            print('\nNew updated list\n')
            print('Student Id\t\tName\t\tCourse Code')
            for i in range(len(st)):
                st[i].showall()
            

    userch=input("\n Enter Y to continue or Press anykey to exit.")
    if userch=='Y' or userch=='y':
        continue
    else:
        print('Bye')
        sys.exit()
    

