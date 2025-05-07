Report = {'Vaishnavi':45, 'Arun':90, 'Gaurav':35, 'Priya': 98, 'Sonali':88}
Stu_Name = input("Enter the student name: ")
if Stu_Name in Report:
    print(f'{Stu_Name}'"'s marks:", Report[Stu_Name])
else:
    print("Student not found.")