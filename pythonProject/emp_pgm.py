emp_info = {}
while True:
    print("1. Create the employee information")
    print("2. Update the employee details")
    print("3. Delete the employee")
    print("4. Display")
    print("5. Exit")

    ch = int(input("Enter your choice: [1-4]:"))
    if ch == 1:
        name = input("Enter name:")
        emp_id = input("Enter employee id:")
        ph = input("Enter phone:")
        tech = input("Enter technologies (csv)")
        emp_info[emp_id] = {"name": name, "phone": ph, "tech": tech.split(',')}
    elif ch == 2:
        emp_id = input("Whose details you wanna update? Enter id:")
        for key, value in emp_info[emp_id].items():
            new = input("{}({})".format(key, value))
            emp_info[emp_id][key] = value if new == '' else new
    elif ch == 3:
        emp_id = input("Whose details you wanna delete? Enter id:")
        # emp_info.pop(emp_id)
        del emp_info[emp_id]
    elif ch == 4:
        print(emp_info)
    else:
        break
