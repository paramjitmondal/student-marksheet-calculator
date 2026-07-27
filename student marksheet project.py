student_name=(input("Name:"))
subject_1=int(input("ENGLISH:"))
subject_2=int(input("COMPUTER:"))
subject_3=int(input("GENERAL KNOWLEDGE:"))
subject_4=int(input("DRAWING:"))
total=subject_1+subject_2+subject_3+subject_4
percentage=total/4
def calculate_grade(percentage):
    if percentage >= 90:
        print("GRADE:A+")
    elif percentage >= 80:
        print("GRADE:A")
    elif percentage >= 60:
        print("GRADE:B")
    elif percentage >= 50:
        print("GRADE:B+")
    else:
        print("FAILLLLLLL!!!!!!!")

calculate_grade(percentage)

