from matplotlib import pyplot as plt

class Pet_details(): #class is created to logically group data and functions in a way that's easy to reuse and easy to build upon if need be 
    
    def __init__(self, id, name, type, age, owner): #initialising
        self.pet_id=id
        self.pet_name=name
        self.pet_type=type
        self.pet_age= age
        self.pet_owner=owner
        

    def print_details(self):
        """prints all the details"""
        print('Pet Details')
        print('-----------')
        print('Pet_id:', self.pet_id)
        print('Pet_name:',self.pet_name)
        print('Pet_type:',self.pet_type)
        print('Pet_age:',self.pet_age)
        print('Pet_owner:',self.pet_owner)
        
    
def numinput(num):# to make sure user enters integer
  if num.isnumeric():
    return True
  else:
    return False
        
def idinput(num):# To make sure all the IDs are unique
    IDs=[]
    for a in pets_list:
        IDs.append(a.pet_id)
        
    if num in IDs:
        return True
    else:
        return False
        
def menu():
         print('======================ASSIGNMENT-2=========================')
         print('-----------------------------------------------------------','\n')
         print('===========================================================')
         print('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬PET MANAGEMENT SYSTEM¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬')
         print('===========================================================')
         print('     [1]     Display pets information')
         print('     [2]     Display the youngest and eldest pet')
         print('     [3]     Add new pet')      
         print('     [4]     Search for pet details')
         print('     [5]     Pets managed by pet owner')
         print('     [6]     Pet details in ascending order')
         print('     [7]     Display graph')
         print('     [8]     Rewrite the file')
         print('     [9]     Exit')
         print('-----------------------------------------------------------')
        
 
def read(file_name):
    try:#error handling in case file is not present
      with open(file_name, mode='r') as reader: #using with statement reduces the typing effort
          for line in reader:
              line=line.rstrip('/n')
              id, name, type, age, owner=line.split(', ')
              a=Pet_details(id, name, type, age, owner)
              pets_list.append(a)
    except:
        print('file error')
 
        
def displayall():
    Total=len(pets_list)
    for i in pets_list:
        i.print_details()
        
    #creating empty objects   
    types=set()
    report={}
    #adding to a set
    for a in pets_list:
        types.add(a.pet_type)
    #adding to a dictionary
    for a in types:
        number=0
        for obj in pets_list:    
            if (a==obj.pet_type):
                number+=1
        report.update({a: number})
        
    print(end='\n')
    print('============================')
    print('-----------SUMMARY----------',end='\n')
    print('Number of pets are as folows:')
    for key, value in report.items():#iterating through the dictionary
        print(key, ' : ', value)
    print('Total number of pets:',Total)
    
    
def comparison():
    youngest= pets_list[0]
    eldest=pets_list[0]
    for a in pets_list:
        if (a.pet_age < youngest.pet_age):
            youngest=a
        elif (a.pet_age > eldest.pet_age):
            eldest=a
            
    print('\nDetails of the Eldest Pet:\n')
    eldest.print_details()
    print('\nDetails of the Youngest Pet:\n')
    youngest.print_details()
    
    
    
def Add_pet():
    #Calculating the average of age before new pet is added 
    length=len(pets_list)
    sum=0
    for i in pets_list: 
        if int(i.pet_age) !=0:
            sum+=int(i.pet_age)
    avg=sum/len(pets_list)
    
    #Adding new pet
    print("-----------------WELCOME!---------------------")
    a=input('How many pets do you want to enter?: ')
    while True:
        if numinput(a):
            break
        else:
            print('Please specify a number')
            a=input('How many pets do you want to enter?: ')
    a=int(a)
    for i in range(a):    
        id = input("Enter the Pet Id: ")
        #error handling
        while True:
            if idinput(id):
                print('ID already exists')
                id = input("Enter the Pet Id: ")
            else:
                break          
        name = input("Enter the Pet Name: ")
        type = input("Enter the Pet Type: ")
        age = input("Enter the Pet age: ")
        #error handling
        while True:
            if numinput(age):
                int(age)
                break
            else:
                print('Age must be integer')
                age = input("Enter the Pet age: ")
                int(age)
        owner = input("Enter the Pet Owner: ")
        new_data = Pet_details(id, name, type, age, owner)
        pets_list.append(new_data)
        writer = open('PET.TXT', 'a')
        a=('\n',id,', ', name,', ', type,', ', age,', ', owner)
        writer.writelines(a)
        writer.close()
        print("Successfully added to the list.....")
    length2= len(pets_list)
    increment= length2-length
    sum2=0
   
     #calculating average age of pets after addition
    for i in pets_list: 
          if int(i.pet_age) !=0:
              sum2+=int(i.pet_age)
    total=len(pets_list)
    avg2=sum2/total
    difference=avg-avg2
    
    
    print('---------------SUMMARY REPORT------------------')
    print('Number of pets increased by:')
    print(increment)
    print('Difference in the average age of pets is:')

    print(difference)
        
def pet_search():
    found=False
    petname=input('Enter the pet name:')
    for a in pets_list:
        if a.pet_name==petname:
            a.print_details()
            found=True
    if found == False:
            print('Sorry!',petname,'is not looked after by the vet')
            response1=input('Do you want to try again?')
            if response1=='y':
                pet_search()

                
def owners_list():
  owner = set()
  for x in pets_list:
    owner.add(x.pet_owner)
  dictt = {}
  for x in owner:
    number= 0
    for obj in pets_list:
      if (x == obj.pet_owner):
        number+=1
    dictt.update({x: number})

  print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
  print("Lists of owners and their number of pets are as follows:")
  print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
  for x, y in dictt.items():
   print(" Owner's Name:",'\n',x,"Number of pets owned:",'\n',y)
            
            
            
def sorting_age():
  for i in range(0,len(pets_list)):
    for j in range(i + 1, len(pets_list)):
      if (pets_list[i].pet_age > pets_list[j].pet_age):
        c = Pet_details(0, "", "", 0, "")  #this is an empty object
        c = pets_list[i]
        pets_list[i] = pets_list[j]
        pets_list[j] = c
  print('\n')
  for I in pets_list:
      I.print_details()
  print("Sorting done successfully.....")
                      
                 
def create_graph():
 xaxis = set()
 for i in pets_list:
      xaxis.add(i.pet_type)
      
  
 owners_dict = {}
 for x in xaxis:
   number = 0
   for data in pets_list:
     if (x == data.pet_type):
       number+= 1
   owners_dict.update({x: number})

 ####---------------------------------
 types = list(owners_dict.keys())
 pets = list(owners_dict.values())
 # creating the bar plot
 plt.bar(types, pets, color='purple', width=0.4)

 plt.xlabel("Pet Type")
 plt.ylabel("Numbers of pets")                          
        
 plt.title("Composition of pets looked after by a vet")
 plt.show()
  

def write():
    print('WELCOME!')
    try:
        with open('PET.TXT', mode='w') as writer: 
            while True:
                id=input('Enter pet ID: ')   
                name=input('Enter pet name: ')
                type=input('Enter pet type: ') 
                age=input('Enter pet age: ')
                owner=input('Enter pet owner: ')
                a=(id,', ', name,', ', type,', ', age,', ', owner,'\n')
                writer.writelines(a)
                nextrecord=input('Do you want to insert another record? ')
                if nextrecord=='n':
                    break
        
                    print('Records Successfully added to the file.....') 
    except:
        print('file error')


         #------------------------main body--------------------------#

pets_list= [] 
read('pet_data.pet.txt')    
while(True):
    menu()      
    a=(input('Please choose an option 1-9:'))
    #error handling
    while True:
        if numinput(a):
            break
        else:
            print('Invalid option')
            a=(input('Please choose an option 1-9:'))
                 
    a=int(a)
    if a==1:
      displayall()
    elif a==2:
     comparison()
    elif a==3:
      Add_pet()
    elif a==4:
      pet_search()
    elif a==5:
      owners_list()
    elif a==6:
      sorting_age()
    elif a==7:
      create_graph()
    elif a==8:
      write()
    elif a==9:
       print('Thank you for using this system')
       break       
    else:
       print('invalid option')
menu()
    
