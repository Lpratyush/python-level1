
3 of 162
(no subject)
Inbox

Raj Joshi
Attachments
Nov 14, 2024, 9:38 PM (12 hours ago)
to me

Week 2

 5 Attachments
  •  Scanned by Gmail
number_of_Students = int(input("Enter number of students"))
number_of_Size = int(input("Enter number of required group size"))
count = 0
adding_number_of_Size = 0
remaining_Students = 0

while number_of_Students >= adding_number_of_Size:
    adding_number_of_Size = number_of_Size + adding_number_of_Size
    count = count + 1
remaining_Students = adding_number_of_Size - number_of_Students
print(remaining_Students)
print(count)
    
# divide_Ans = int(number_of_Students)//int(number_of_Size)
# exact_Group = int(number_of_Students)// int(number_of_Size)
# remaining_Groups = int(number_of_Students)%int(number_of_Size)
# print(divide_Ans)