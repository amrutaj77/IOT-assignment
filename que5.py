#5)The marks obtained by a student in 3 different subjects are input by the user. Your program should calc
#ulate the average of subjects and display the grade. The student gets a grade as per the following rules:
#Average Grade 
sub1 = int (input("Enter  the marks obtained in sub1:"))
sub2 = int (input("Enter the marks obtained in sub 2:"))
sub3 = int (input("Enter the marks obtained in sub3:"))
avg_marks = (sub1+sub2+sub3)/3 
print("Enter the average")
if avg_marks >= 90:
   print("grade : A") 
elif avg_marks >= 80:
    print("grade :B")
elif avg_marks >=70:
        print("grade :C") 
elif  avg_marks >=60:
            print("grade :D") 
    else:
                print("grade :F")