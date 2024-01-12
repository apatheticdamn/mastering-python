'''
Python has three Boolean operators, or logical operators: and , or , and not . You can use them to check if certain conditions are met before deciding the execution path your programs will follow.
'''

has_skills = True
has_criminal_record = False

if has_skills and not has_criminal_record:
    print("Yes you can join!")
elif has_skills and has_criminal_record:
    print("No you can't join because you have a criminal record!")
elif has_criminal_record and not has_skills:
    print("Man you should be in jail!")
else:
    pass