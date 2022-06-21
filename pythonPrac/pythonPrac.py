                            


import os
import datetime
import math
studentList = []
userName = "uxc"
psswd = "Uxc2022"
credentialsCheck = False
#data validation 7
while credentialsCheck == False:
    userNameInput = input("Enter Username: ")
    psswdInput = input("Enter Password: ")
    os.system("cls.")
    if userNameInput == userName and psswdInput == psswd:
        i=0
        # data validation 1
        flag3 = False
        while flag3 == False:
            
            schoolName = input("Enter School Name: ")
            if schoolName == "":
                print("you need to enter school name")
                flag3 = False
            else:
                flag3 = True
        courseEndDate = input("Enter Course End Date: ")
        #data validation 2
        flag0 =False
        while not flag0:
            try:
                numOfStud = int(input("Enter number of students: "))
                if numOfStud < 20:
                    flag0 = True
                else:
                    print("number of students cannot exceed 20")
                    flag0 = False
            except:
                print("enter a digit")  
        # data validation 3
        while i <numOfStud:
            student = {}
            flag4 = False
            while flag4 == False:

                studentName = input("Enter student name: ")
                if studentName == "":
                    print("you need to enter a name!!")
                    flag4 = False
                else:
                    flag4 = True
            # data validation 4
            flag = False
            mathAvg = 0
            engAvg = 0
            sciAvg = 0
            while not flag:      
                try:
                    mathMarks = int(input("Enter maths marks: "))
                    if mathMarks > 100:
                        print("you cannot enter marks more than 100")
                        flag =False
                    else:
                        mathAvg = mathMarks/100*100
                        flag =True
                except:
                    print("you need to enter a number ")
            # data validation 5
            flag1 = False
            while not flag1:
                try:
                    engMarks = int(input("Enter English marks: "))
                    if engMarks > 100:
                        print("you cannot enter marks more than 100")
                        flag1 =False
                    else:
                        engAvg = engMarks/100*100
                        flag1 = True
                except:
                    print("you need to enter a number ")
            #data validation 6 
            flag2 = False
            while not flag2:
                try:
                    sciMarks = int(input("Enter Science marks: "))
                    if sciMarks > 100:
                        print("you cannot enter marks more than 100")
                        flag2 =False
                    else:
                        sciAvg = sciMarks/100*100
                        flag2 = True
                except:
                    print("you need to enter a number ")  
            averageMks = round((mathAvg + engAvg + sciAvg)/3,2)
            message = ""
            if averageMks <= 40:
                message = "Fail"
                print("You have got a",message)
                print(f"your average marks are {averageMks}")
            elif  40<averageMks<59:
                message = "Pass"
                print("you have got a ", message)
            elif 60<averageMks<=79:
                message = "Merit"
                print("you have got a ", message)
            else:
                message = "Distinction"
                print("you have got a ", message)
            student["name"] = studentName
            student["maths_avg"] = mathMarks
            student["eng_Avg"] = engAvg
            student["sci_Avg"] = sciAvg
            student["average Marks"]= averageMks
            student["Grade"] = message
            studentList.append(student)
            os.system("cls.")
            print("*******************************")
            print(f"\t\tcertificate of appreciation\t\t\n\tSchool Name: {schoolName}\n\tCourse End Date: {courseEndDate}\n\tname: {studentName}\n\tyou have got a {message}\n\twith a total average marks of {averageMks}")
            print("*******************************")
            i += 1      
        def by_average_score(student):
            return student["average Marks"]
        studentList.sort(reverse=True, key=by_average_score)
        #print(studentList)
        os.system("cls")
        datetimeObject = datetime.datetime.now().strftime("%m-%d %H-%M")
        fileTime = str(datetimeObject)
        openFile = open(f"student_details_{fileTime}.txt","w")
        for i in studentList:
            print(i)
            seq = f"{i}\n"
            openFile.writelines(seq)
        openFile.close()
        credentialsCheck = True
    else:
        print("unauthorised access")     
print("programme ended.......")



