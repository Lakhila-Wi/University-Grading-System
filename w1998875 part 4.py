#Intializing varriables
pas=0
defer=0
fail=0

result=0
result=='y'

num_pro=0
num_trail=0
num_ret=0
num_ex=0

total=0

count_1=0
count_2=0
count_3=0
count_4=0

list_1=[]
list_2=[]
list_3=[]
list_4=[]

list_of_list=[]
list_of_list_1=[]
list_of_list_2=[]
list_of_list_3=[]

Outco_dict={}
input_dict={}

#creating functions
#Creating function for get progrees
def progress(pas,defer,fail):
    global num_pro
    if pas==120 and defer==0 and fail==0:
        print('progress')
        num_pro=num_pro+1
        return True     
    return False
#Creating function for get Module trailer
def trailer(pas,defer,fail):
    global num_trail
    #change it as and to or
    if pas==100 and (defer==20 or fail==0):
        print('Progress (Module trailer)')
        num_trail=num_trail+1
        return True 
    elif pas==100 and (defer==0 or fail==20):
        print('Progress (Module trailer)')
        num_trail=num_trail+1 
        return True
    return False
#Creating function for get do_not_prgress
def do_not_Progress(pas,defer,fail):
    global num_ret
    if pas==80 and (defer<41 or fail<41):
        print('Module retriever')
        num_ret=num_ret+1
        return True
    elif pas==60 and (defer<=60 or fail<=60):
        print('Module retriever')
        num_ret=num_ret+1
        return True
    elif pas==40:
        while (defer>=20 and fail<=60):
            if (defer<=80 or fail<=60):
                print('Module retriever')
                num_ret=num_ret+1
            break 
        return True
    elif pas==20:
        while (defer>=40 and fail<=60):
            if (defer<=100 or fail<=60):   
                print('Module retriever')
                num_ret=num_ret+1
            break
        return True
    elif pas==0: 
        while (defer<=120 and fail<=60 ):
            if (defer<=60  or fail<=60 ):
                print('Module retriever')
                num_ret=num_ret+1
            break
        return True
    return False

#Creating function for get exclude
def Exclude(pas,defer,fail):
    global num_ex
    if pas==40 and (defer==0 or fail==80):
        print('Exclude')
        num_ex=num_ex+1
        return True        
    elif pas==20 and (defer<21 or fail>=80):
        print('Exclude')
        num_ex=num_ex+1
        return True
    elif pas==0 and (defer<=40 or fail>=80):
        print('Exclude')
        num_ex=num_ex+1
        return True
    return False

#Creating function for get Histogram    
def histogram(num_pro,num_trail,num_ret,num_ex):
    print("------------------------------------------------------------------------")
    print('Progress ',num_pro,'\t : ', '*' *num_pro )
    print('Trailer ',num_trail,'\t : ' ,'*' *num_trail)
    print('Retriever ',num_ret, "\t : " , '*' *num_ret)
    print('Excluded ',num_ex, "\t : ", '*' * num_ex)
    total=num_ex+num_ret+num_pro+num_trail
    print('\n')
    print(total," outcomes in total")
    print("------------------------------------------------------------------------")
    return

#Looping the code until the user enter enter stop    
while True:
    Id=input('Enter student id: ')        #Getting id for the dictionary
    #getting pass value
    try:
        pas=int(input('Enter your number of credits at pass: '))
        #Checking the input is in the range 
        if pas not in range(0,130,20):
            print("Out of range")
            pas=int(input('Enter your number of credits at pass: '))
            
    except ValueError:
        #if the user input sting, display error massege
        print('Integer required')
        pas=int(input('Enter your number of credits at pass: '))
        if pas not in range(0,130,20):
            print("Out of range")
            pas=int(input('Enter your number of credits at pass: '))
    #getting defer value       
    try:
        defer=int(input('Enter your number of credits at Defer: '))
        if defer not in range(0,130,20):
            print("Out of range")
            defer=int(input('Enter your number of credits at Defer: '))
            
    except ValueError:
        #if the user input sting, display error massege
        print('Integer required')
        defer=int(input('Enter your number of credits at Defer: '))
        if defer not in range(0,130,20):
            print("Out of range")
            defer=int(input('Enter your number of credits at Defer: '))
    #getting fail value 
    try:
        fail=int(input('Enter your number of credits at fail: '))
        if fail not in range(0,130,20):
            print("Out of range")
            fail=int(input('Enter your number of credits at fail: '))

    except ValueError:
        #if the user input sting, display error massege
        print('Integer required')
        fail=int(input('Enter your number of credits at fail: '))
        if fail not in range(0,130,20):
            print("Out of range")
            fail=int(input('Enter your number of credits at fail: '))
    #Checking the user entered final value is qual to the 120
    final=pas+defer+fail
    final=int(final)
    if final<=120:
        #progress(pas,defer,fail)
        isprogress=progress(pas,defer,fail)
        if isprogress==True:
            count_1=count_1+1
            list_1.append(pas)
            list_1.append(defer)
            list_1.append(fail)    
            output = "Progress"

        #trailer(pas,defer,fail)
        istrailer=trailer(pas,defer,fail)
        if istrailer==True:
            count_2=count_2+1
            list_2.append(pas)
            list_2.append(defer)
            list_2.append(fail)
            output = "Progress (module trailer)"
    
        #Exclude(pas,defer,fail)
        isexclude=Exclude(pas,defer,fail)
        if isexclude==True:
            count_3=count_3+1
            list_3.append(pas)
            list_3.append(defer)
            list_3.append(fail) 
            output = "Exclude"
        #do_not_Progress(pas,defer,fail)
        isdonotprogress=do_not_Progress(pas,defer,fail)
        if isdonotprogress==True:
            count_4=count_4+1
            list_4.append(pas)
            list_4.append(defer)
            list_4.append(fail)
            output = "Do not progress (module retriever)"
        #Adding outputs for the dictionary
        Outco_dict[Id]={
            'output': output,
            'marks': [pas, defer, fail]
        }
        input_dict[Id]=[pas, defer, fail]

        print()
            
    else:
        print('Total incorect')
    
    list_of_list=list_1.copy() 
    list_of_list_1=list_2.copy() 
    list_of_list_2=list_3.copy() 
    list_of_list_3=list_4.copy()

    #Asking user like to continue or quit
    print("Would you like to enter another set of data?")
    result=input("Enter \'y\' for yes or \'q\' for quit and view results: ")
    if result.lower()=='y':
        continue
    else:
        histogram(num_pro,num_trail,num_ret,num_ex)
        #Displaying the list that user input
        print("Progress - ",list_of_list)
        print("Trailer - ",list_of_list_1)
        print("Exclude - ",list_of_list_2)
        print("Do not Progress - ",list_of_list_3)
        #Disaplaying the dictionary
        for Id, marks in input_dict.items():            
            print(f"{Id} : {output} - {marks[0]}, {marks[1]}, {marks[2]}")
    break

    
 
#Creating the txt file 
with open("example_python.txt", 'w') as f:
    f.write("Progress - {}\n".format(list_of_list))
    f.write("Trailer - {}\n".format(list_of_list_1))
    f.write("Exclude - {}\n".format(list_of_list_2))
    f.write("Do not Progress - {}\n".format(list_of_list_3))


