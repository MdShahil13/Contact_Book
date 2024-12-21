contect = {}

while True:
    print("Contect Book Me Aapka Swagat Haii! ")
    print("1. Create the contect")
    print("2. Delete the contect")
    print("3. Update the contect")
    print("4. Search the contect")
    print("5. Count the contect")
    print("6. View the contect")
    print("7. Exit")

    choice = input("Enter Your choice :  ")

    if choice=='1':
        name = input("Enter a Name : ")
        if name in contect:
            print(f"Contect name {name} is already exists !")
        else:
            mobile = int(input("Enter a Mobile Number : "))
            email = input("Enter a Email-id : ")
            contect[name] = {'mobile': mobile, 'email':email,}
            print(f'Contect name {name} has been created...')

    elif choice=='2':
        name = input("Enter a name Which You delete in Contect Book : ")
        if name in contect:
            print(f"Contect name {name} has been Deleted...")
            del contect[name]
        else:
            print(f"Contect Name {name} has not Found...")
    elif choice=='3':
        name= input("Enter a name for update : ")
        if name in contect:
            name = input("Enter a Updated Name : ")
            try:
                mobile = int(input("Enter a updated Mobile Number : "))
            except:
                print("Invalid Number It is should Be Only Digit...")
            email = input("Enter a updated Email-id : ")
            contect[name] = { 'name': name ,'mobile': mobile, 'email':email,}
        else:
            print(f"Contect Name {name} is Not found")

    elif choice=='4':
        name = input("Enter a name to search it is present or not in Contect Book !: ")
        if name in contect:
            print(f'Contect name {name} is a Present in Contect Book...')
        else :
            print(f"Contect Name {name} is not present in Contect Book...")
    elif choice=='5':
        count = 0
        for i in contect:
            count += 1
        print(f"There Are {count} Contects In Contects Book...")
    elif choice=='6':
        name = input("Enter a name to see his/her Details: ")
        if name in contect:
            print(f"Name : {name}")
            print(f"Mobile Number : {mobile}")
            print(f"Email-id: {email}")
        else:
            print(f"Contect Name {name} is not found")
    elif choice=='7':
        print("Thank You...!")
    else:
        print("Invalid Choice...")












