import os
#create new file
def create_file(filename):
    try:
        with open(filename,'x') as f:
            print(f"FileName{filename}:Created Sucessfully")    
            

    except FileExistsError:
        print(f"FileName{filename} already Exists")

    except Exception as E:
        print('An Error Occured !')

# view all files 
def view_all_files():
    files = os.listdir()
    if not files:
        print("No file Found")
    else:
        print("Files in directory !")
        for file in files:
            print(file) 


#delete the files
def delete_file(filename):
    try:
        os.remove(filename)
        print(f'{filename} file has been deleted sucessfully !')
    except FileNotFoundError:
        print("File Not Found")
    
    except Exception as e:
        print("An error occured !")

def read_file(filename):
    try:
        with open('sample.txt','r') as f:
            content = f.read()
            print(f"Content of '{filename}':\n{content}")
    except FileNotFoundError:
        print(f"{filename}doesn't exits!")
    except Exception as e:
        print("An error occured!")

# edit a file
def edit_file(filename):

    try:
        with open('sample.txt','a') as f:
            content =input('Enter data to add =')
            f.write(content +"\n")
            print(f'Content added to {filename}  Sucessfully !')
    except FileNotFoundError:
        print(f"{filename}doesn't exits!")

    except Exception as e:
         print("An error occured!")


# main Funtion for options
def main():
    while True:
        print('File Management App')
        print('1:Create file ')
        print('2:View All files ')
        print('3:Deletefile ')
        print('4:Read file ')
        print('5:Edit file ')
        print('6:Exit file ')
        

        choice =input("Enter Your Choice(1-6)= ")

        if choice == '1':
            filename =input('Enter the file name to create =')
            create_file(filename)
        
        elif choice =='2':
            view_all_files()

        elif choice =='3':
            filename =input('Enter filename you want to delete =')
            delete_file(filename)

        elif choice =='4':
            filename = input('Enter file name to read =')
            read_file(filename)

        elif choice =='5':
            filename = input('Enter the file name to edit =')
            edit_file(filename)
        
        elif choice =='6':
            print("Closing the app...")
            break
        else:
            print("Invalid Syntax")

if __name__=="__main__":
    main()

