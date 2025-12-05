#سیستم مدیریت زمان 

# لیست ادمینتور 
admin_information = [
    {"username": "abolfazl", "password": "sa"}
]

#صفحه اول 
print ("_______life management_______\n1-user name :\n2-password :")
user_name = input("\n1>")
password = input("\n2>")


#احراز هویت 

if user_name == admin_information[0]["username"] and password == admin_information[0]["password"]:
    pass
else:
    while True :
        print ("User name and password is not correct!\nplasse try again")
        user_name = input ("plasse enter your user name!\n>").strip()
        password = input ("plasse enter your password!\n>").strip()
        if user_name == admin_information[0]["username"] and password == admin_information[0]["password"]:
            break
        else :
            print ("User name and password is not correct!\nplasse try again")
            user_name = input ("plasse enter your user name!\n>").strip()
            password = input ("plasse enter your password!\n>").strip()
#_______________________________________________________________________________________________________

#TO DO LIST 

#لیست پیش فرض کار ها 
tasks = [
    {"task": "go to gym", "priority": "normal"},
    {"task": "eat diner",   "priority": "normal"},
    {"task": "do homworke", "priority": "high"}
]

#تابع add_task 
def add_task () :
    '''add new task'''
    print("add new task:")
    task = input ("please enter your task:\n>")
    priority = input ("determine the importance of your task :\n>")
   #چک کردن ورودی ها
    while task.strip() == "" :
        task = input ("Task cannot be empty \nplease enter your task2:\n>")

    #سیو کردن تسک در لیست 
    tasks.append({
        "task" : task,
        "priority" : priority
    })
    print (f'\nTask "{task}" added successfully :)\n\n')
    return tasks


#تابع get_task
def get_tasks () :
    '''show all tasks'''
    sorted_tasks = sorted(tasks, key=lambda item: item["task"])
    for i, t in enumerate(sorted_tasks, start=1):
        print(f"{i}. {t['task']} - {t['priority']}")
    print()

#تابع کل to do list 
def to_do_list () :
    '''
    Docstring for to_do_list
    '''
    #نمایش
    print ("__To Do List__\n")
    while True:
        person_choice = input('please enter youer choice:\n1-Add task\n2-get task\ntype "esc" to exit\n>')
        person_choice = person_choice.strip().lower()
        while person_choice == '':
            print('\nyour choice cannot be empty!')
            person_choice = input('\nplease enter youer choice:\n1-Add task\n2-get task\ntype "esc" to exit\n>')
            person_choice = person_choice.strip().lower()        
        if person_choice == "esc" :
            break
        person_choice_number = int(person_choice)
        if person_choice_number == 1 :
            add_task()
        if person_choice_number == 2 :
            get_tasks()

#____________________________________________________________________________________

#تابع گرفتن هزینه ها 

#لیست اول خالی هزینه ها 
expenses_list = []

#تابع  add expenses 
def add_expenses () :
    '''add new expenses'''
    print("add new expenses:")
    name_expenses  = input ("please enter your expenses name :\n>")
    price = input ("plase enter price expenses :\n>")
   #چک کردن ورودی ها
    while name_expenses.strip() == "" or price.strip() == "":
        name_expenses = input ("expenses name cannot be empty \nplease enter your expenses name :\n>")
        price = input ("price expenses cannot be empty \nplease enter your price expenses:\n>")
    #سیو کردن تسک در لیست 
    expenses_list.append({
        "name" : name_expenses,
        "price" : price
    })
    print (f'\nexpenses "{name_expenses}" added successfully :)\n\n')
    return admin_information

#تابع  get expenses

def get_expenses () :
    '''
    Docstring for get_expenses
    '''
    sorted_tasks = sorted(expenses_list, key=lambda item: item["price"])
    print(sorted_tasks)

#تابع  expenses
def expenses ():
    
    print("------------expenses managment------------")
    while True:
        expenses_choice = input('please enter youer choice:\n1-Add expenses\n2-get expenses\ntype "esc" to exit\n>')
        expenses_choice = expenses_choice.strip().lower()
        while expenses_choice == '':
            print('\nyour choice cannot be empty!')
            expenses_choice = input('please enter youer choice:\n1-Add expenses\n2-get get expenses\ntype "esc" to exit\n>')
            expenses_choice = expenses_choice.strip().lower()        
        if expenses_choice == "esc" :
            break
        expenses_choice_number = int(expenses_choice)
        if expenses_choice_number == 1 :
            add_expenses()
        if expenses_choice_number == 2 :
            get_expenses()

#_____________________________________________________________________

#new admintore 

#add new admin تابع 

def add_new_admin () :
    '''docstring add new admin'''
    print ('------add new amintore------')
    user_name = input ("plasse enter your user name!\n>")
    password = input ("plasse enter your password!\n>")
       #چک کردن ورودی ها
    while user_name.strip() == "" or password.strip() == "":
        user_name = input ("user name cannot be empty \nplease enter your user name :\n>")
        password = input ("password cannot be empty \nplease enter your password:\n>")
        
    
    #سیو کردن تسک در لیست 
    admin_information.append({
        "username" : user_name,
        "password" : password
    })
    print (f'\nnew admin "{user_name}" added successfully :)\n\n')
    return admin_information

#_______________________________________________________________________________________________________
#memory 

memory = []

#تابع Add memory 
def add_memory () :
    '''
    Docstring for add_memory
    '''
    print ('------Add new memory------')
    name_memory = input ('Please Enter name memory:\n>')
    timelin = input ('Please Enter the date of the memory :\n>')
    memory_description = input ('Please Enter Description of the memory:\n>')
    
    while name_memory.strip () == '' or timelin.strip () == '' or memory_description.strip () == '' :
        name_memory = input ('memory name can not be empty \nPlease Enter your memory name\n>')
        timelin = input ('timelin can not be empty \nPlease Enter timlin memory\n>')
        memory_description = input ('memor description can not be empity \nPlease Enter your memory description\n>')
    
    #سیو کردن در لیست خاطرات 
    memory.append({
        'name memory' : name_memory,
        'timelin' : timelin,
        'memory description' :memory_description
    })
    print(f'new memory "{name_memory}" added successfully \n\n')
    return memory
#تابع get memory 
def get_memory () :
    '''
    Docstring for get_memory
    '''
    print ('------memory booke------')
    memory_booke_stored = sorted(memory , key= lambda item : item['timelin'])
    print (memory_booke_stored)

#تابع دفترخاطرات 
def memory_booke () :
    '''
    Docstring for memory_booke
    '''
    print ('-------Memory Booke-------\n')
    while True :
        choice_memory = input ('Please enter your choice :\n1-Add new memory\n2-get memory booke\n**for exit enter esc**\n\n>')
        choice_memory = choice_memory.strip().lower()
        while choice_memory == '' :
            choice_memory = input ('Your chice can be empity please enter your chice :\n1-Add new memory\n2-get memory booke\n**for exit enter esc**\n\n>')
        if choice_memory == 'esc' :
            break
        choice_memory_number = int(choice_memory)
        if choice_memory_number == 1:
            add_memory()
        if choice_memory_number == 2:
            get_memory()    

#داشبورد اولیه
print (f'------------welcom {user_name}------------\n**enter esc for exit**')
while True:
    dashbord_choice = input('\nEnter your choice\n1-To Do List \n2-expenses\n3-memory booke \n4-add new admintor\n>')
    dashbord_choice = dashbord_choice.strip().lower()
    while dashbord_choice == '':
        print('\nyour choice cannot be empty!')
        dashbord_choice = input('\nEnter your choice\n1-To Do List \n2-expenses\n3-memory booke\n4-add new admintor\n>\ntype "esc" to exit\n>')
        dashbord_choice = dashbord_choice.strip().lower()        
    if dashbord_choice == "esc" :
        break
    dashbord_choice_number = int(dashbord_choice)
    if dashbord_choice_number == 1 :
        to_do_list ()
    if dashbord_choice_number == 2 :
        expenses ()
    if dashbord_choice_number == 3 :
        memory_booke()
    if dashbord_choice_number == 4 :
        add_new_admin()
