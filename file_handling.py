from os import remove

loop = "yes"
file_created = 0

while loop == "yes":

    

    if file_created == 0 :

        file_name = input("Create a new file or open an exisiting one :")

    else :
        pass



    procces = int(input("""
    
    ->Enter the 1 for appending data into the file

    ->Enter the 2 for writing data over the old versions and delete them

    ->Enter the 3 for reading the file

    ->Enter the 4 for removing the file

    ->Enter the 5 for closing the file 

    ->Enter the 6 to switch the file
    :"""))

    #append the file
    if procces == 1 :
        
        f = open(file_name+".txt","a")
        
        loop_2 = 'yes'

        while loop_2 == 'yes' :

            text = input("Enter the text that you want to save into the file :")

            new_line=input("Would you like to pass a new line ?(yes/no):").lower()

            if new_line == 'yes':
                f.write(text+"\n")
            
            else:
                f.write(text)

            loop_2 = input("Would you like to continue ?(yes/no):").lower()


    #writing the file
    elif procces == 2:
        
        f=open(file_name+".txt","w")

        loop_3 = 'yes'

        while loop_3 == 'yes' :

            text = input("Enter the text that you want to save into the file :")

            new_line=input("Would you like to pass a new line ?(yes/no):").lower()

            if new_line == 'yes':
                f.write(text+"\n")
            
            else:
                f.write(text)

            loop_3 = input("Would you like to continue ?(yes/no):").lower()

        



    #reading the file
    elif procces == 3:

        f = open(file_name+".txt","r")
        
        read_type =int(input("""

        ->Press 1 to read whole file 

        ->Press 2 to read limitied line set
        
        """)) 

        if read_type == 1 :

            print(f.read())


        elif read_type == 2:
            
            line_set = int(input("How many line set would you like to display ? :"))

            a=0

            while a<line_set:

                try :

                    print(f.readline())

                except:

                    print("There is none left to show...")
                    break
            
                a += 1
            #bring the cursor on initial position
            f.seek(0)

    #remove the file
    elif procces == 4:
        
        remove("alp_notes.txt")
        print("File was removed...")

    #close the file
    elif procces == 5:
        
        try :
            f.close()
            print("File was closed...")

        except :
            print("File doesn't exist .")


    #switch the file
    elif procces == 6:

        change_file = input("Would you like to switch the file you are working on ?(yes/no):").lower()

        if change_file == 'yes' :
             file_name = input("Create a new file or open an exisiting one :")

        else :
            pass


    if file_created == 0:
        file_created += 1
    loop = input("Would you like to continue to procces the file ?(yes/no):").lower()

print("Program is being closed...")
    

