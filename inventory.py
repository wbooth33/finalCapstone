'''
I have left the comments as the ones provided as I didnt want to add more unnecessary lines.
If you wish me to add more comments please let me know and I will.
'''

#========The beginning of the class==========
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
    def get_cost(self):
        with open("inventory.txt", "r") as f:
            data = f.readlines()[1:]
            for line in data:
                shoe_data = line.strip().split(",")
                if shoe_data[1] == self.code:
                    return int(shoe_data[3])
        '''
        Read from the inventory.txt file.
        Add the code to return the cost of the shoe in this method.
        '''

    def get_quantity(self):
        with open("inventory.txt", "r") as f:
            data = f.readlines()[1:]
            for line in data:
                shoe_data = line.strip().split(",")
                if shoe_data[1] == self.code:
                    return int(shoe_data[4])
        '''
        Read from the inventory.txt file.
        Add the code to return the quantity of the shoes.
        '''

    def __str__(self):
        return f"Country: {self.country}\nCode: {self.code}\nProduct: {self.product}\nCost: £{self.cost}\nQuantity: {self.quantity}"
    '''
    Add a code to returns a string representation of a class.
    '''

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    try:
        with open("inventory.txt", "r") as f:
            data = f.readlines()[1:]
            for line in data:
                shoe_data = line.strip().split(",")
                shoe = Shoe(shoe_data[0], shoe_data[1], shoe_data[2], int(shoe_data[3]), int(shoe_data[4]))
                shoe_list.append(shoe)
    except FileNotFoundError:
        print("Could not find inventory.txt.")

    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''

def capture_shoes(country, code, product, cost, quantity):
    new_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe)
    with open("inventory.txt", "a") as f:
        f.write(f"\n{country},{code},{product},{cost},{quantity}")
    print("Shoe added to inventory!")

    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

def view_all():
    for shoe in shoe_list:
        print("\n" + str(shoe))

    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

def re_stock():
    with open("inventory.txt", 'r') as f:
        lines = f.readlines()
        data = []
        for line in lines:
            try:
                item = line.strip().split(",")
                data.append([item[0], item[1], item[2], item[3], int(item[4])])
            except:
                pass
        min_quantity = min([item[4] for item in data])
        min_item = [item for item in data if item[4] == min_quantity][0]
        answer = input(f"Do you want to re-stock the {min_item[2]} shoes from {min_item[0]}? (yes/no)\n")
        if answer.lower() == 'yes':
            quantity = int(input("How many shoes do you want to add?\n"))
            for item in data:
                if item[2] == min_item[2] and item[0] == min_item[0]:
                    item[4] += quantity
    with open("inventory.txt", "w") as f:
        f.write('\n'.join([','.join([item[0], item[1], item[2], item[3], str(item[4])]) for item in data]))
        print("Inventory has been adjusted!")

    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

def search_shoe(shoe_list, code):
    for shoe in shoe_list:
        if shoe.code == code:
            print()
            return print(shoe)
    print("Shoe not found")
    return None

'''
    This function will search for a shoe from the list
    using the shoe code and return this object so that it will be printed.
'''

def value_per_item():
    with open("inventory.txt", "r") as f:
        lines = f.readlines()[1:]
        for line in lines:
            line_list = line.strip().split(",")
            value = int(line_list[3]) * int(line_list[4])
            print(f"The total value of all of the {line_list[2]} is £{value}.")

    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

def highest_qty():
    with open("inventory.txt", "r") as f:
        data = f.readlines()
        max_qty = 0
        max_product = ""
        for line in data:
            line_list = line.strip().split(",")
            qty = int(line_list[-1])
            if qty > max_qty:
                max_qty = qty
                max_product = line_list[2]
        print(f"{max_product} is for sale with a quantity of {max_qty}")


    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

#==========Main Menu=============
def menu():
    while True:
        print('''\nWelcome to the Shoe Zone!
        1 - Read the shoe directory
        2 - Add a shoe to the directory
        3 - View all shoe's in directory
        4 - Restock a shoe
        5 - Search for a shoe
        6 - Find the total cost of all quantity of a shoe
        7 - Find the shoe with the highest quantity
        8 - Exit
        ''')
        choice = input("What would you like to do?\n")

        #If choice is 1, call read_shoes_data() function.
        if choice == "1":
            read_shoes_data()
        
        #If choice is 2, call capture_shoes function.
        elif choice == "2":
            country = input("Enter the country of origin:\n")
            code = input("Enter the shoe code:\n")
            product = input("Enter the product name:\n")
            cost = int(input("Enter the cost of the shoe:\n"))
            quantity = int(input("Enter the quantity of the shoe:\n"))
            capture_shoes(country, code, product, cost, quantity)

        #If choice is 3, call view_all() function, call read_shoes_data() just incase it hasnt been called already.
        elif choice == "3":
            read_shoes_data()
            view_all()

        #If choice is 4, call re_stock() function.
        elif choice == "4":
            re_stock()

        #If choice is 5, call search_shoe() function, call read_shoes_data() just incase it hasnt been called already.
        elif choice == "5":
            code = input("Enter the code for the shoe you wish to find:\n")
            read_shoes_data()
            search_shoe(shoe_list, code)
        
        #If choice is 6, call value_per_item() function.
        elif choice == "6":
            value_per_item()

        #If choice is 7, call highest_qty() function.
        elif choice == "7":
            highest_qty()
        
        #If choice is 8, break.
        elif choice == "8":
            break

        else:
            print("Invalid choice!")

#Call menu() function to excute each function.
menu()
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
