# James Hooper and Spencer Burton

#**********************************Functions**************************************************************
def logo_screen() :
    """This is the first screen"""

    logo = \
"""
-----        _____ _                      __          __      _            
|    \      / ____| |                     \ \        / /     | |           
|     \    | |    | |__   ___  ___  ___  __\ \  /\  / /__  __| | __ _  ___ 
|      \   | |    | '_ \ / _ \/ _ \/ __|/ _ \ \/  \/ / _ \/ _` |/ _` |/ _ \\
|       \  | |____| | | |  __/  __/\__ \  __/\  /\  /  __/ (_| | (_| |  __/
----------  \_____|_| |_|\___|\___||___/\___| \/  \/ \___|\__,_|\__, |\___|
            Studios                                              __/ |     
                                                                |___/   
                                Presents                               
                           - The Oregon Trail -
"""
    
    names = "Jame Hooper and Spencer Burton"
    copy_right = "Copyright (c) 2020"

    print(str.format("{} {}\n {}", copy_right, names, logo))

    input("\nPress Enter to stop appreciating our art")

def menu(options) :
    value = ""
    success = False

    print("You may:")

    for i in range(len(options)) :
        print(str.format("  {}. {}", i + 1, options[i]))

    while not success :
        value = input("What do you choose: ")

        if value in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9") :
            int_value = int(value)

            if int_value in range(1, len(options) + 1) :
                success = True

    return int(value)


def start_screen() :

    oregon_trail = \
"""
_______________________________________________________________________________
  _______ _             ____                               _______        _ _ 
 |__   __| |           / __ \                             |__   __|      (_) |
    | |  | |__   ___  | |  | |_ __ ___  __ _  ___  _ __      | |_ __ __ _ _| |
    | |  | '_ \ / _ \ | |  | | '__/ _ \/ _` |/ _ \| '_ \     | | '__/ _` | | |
    | |  | | | |  __/ | |__| | | |  __/ (_| | (_) | | | |    | | | | (_| | | |
    |_|  |_| |_|\___|  \____/|_|  \___|\__, |\___/|_| |_|    |_|_|  \__,_|_|_|
                                        __/ |                                 
                                       |___/                                   
"""

    print(oregon_trail)

    finished = False

    while not finished :
        choice = menu(["Start Game", "Learn about the Trail", "End"])

        if choice == 1 :
            # Start game
            play_game()
            finished = True
        elif choice == 2 : # Tell about game
            learn()

            input("Press Enter to continue")
        else :
            finished = True

        # For spacing
        if not finished :
            print()

def learn() :
    """This is Used when the learn of trail is chosen"""
    print("""\nTry taking a journey by covered wagon across 2000 miles of plains, rivers, and mountains. Try! On the plains,
will you slosh your oxen through mucd and water-filled ruts or will you plod through dust six inches deep?\n""")
    input("Press Enter To Continue")
    print("""\nHow will you cross the rivers? If you have money, you might take a ferry (if there is a ferry).
Or, you can ford the river and hope you and your wagon aren't swallowed alive!\n""")
    input("Press Enter To Continue")
    print("""\nWhat about supplies? Well, if you're low on food you can hunt. You might get a buffalo... you might.
And there are bear in the mountains.\n""")
    input("Press Enter To Continue")
    print("""\nAt the Dalles, you can try navigating the Columbia River, but if running the rapids with a makeshift
raft makes you queasy, better take the Barlow Road.\n""")
    input("Press Enter To Continue")
    print("""\nIf for some reason you don't survive -- your wagon burns or thieves steal your oxen,
or you run out of provisisons, or you die of cholera -- don't give up! Try again... and again...\n""")
    input("Press Enter To Continue")
    print("\nThe software team responsible for creation of this product includes:\n - Spencer Burton\n - James Hooper\n")

def month_advice() :
    """Prints the text when you ask for advice"""
    print("""
You attend a public meeting held for “folks with the California - Oregon fever.” You are told:


If you leave too early, there won’t be any grass for your oxen to eat. If you leave too late,
you might not get to Oregon before winter comes. If you leave at just the right time,
there will be green grass and the weather will still be cool.""")
    input("Press Enter To Continue")


def play_game() :
    """The actual game function"""

    # Get profession and money that profession has
    prof_data = char_setup()
    profession = prof_data[0]
    money = prof_data[1]
    
    # Name Leader and other members
    name_data = name_members()
    leader = name_data[0]
    members = name_data[1]

    # Choose month
    month = ""
    
    while True :
        print("\nIt is 1848. Your jumping off place for Oregon is Independence,\n \
Missouri. You must decide which month to leave Independence.")
        choice = menu(["March", "April", "May", "June", "July", "Ask for advice"])

        if choice == 6 :
            month_advice()
        else :
            month = ("March", "April", "May", "June", "July")[choice - 1]
            break

    
    

def char_setup() :
    """Gets the profession and returns it and the amount of money they have"""

    print("\nMany kinds of people made the trip to Oregon.\n")

    description = """
Traveling to Oregon isn't easy! But if you're a banker, you'll have more
money for supplies and sevices than a carpenter or a farmer.

However, the harder you have to try, the more points you deserve! Therefore, the farmer
earns the greatest number of points and the banker earns the least.

 - Banker   : $1600.00
 - Carpeter : $800.00
 - Farmer   : $400.00\n"""

    profession = ""
    money = 0

    while True :

        choice = menu(("Be a banker from Boston", "Be a carpenter from Ohio", "Be a farmer from Illinois", "Find out the differences"))

        if choice == 1 :
            # Banker
            profession = "banker"
            money = 1600
            break
        elif choice == 2 :
            # Carpenter
            profession = "carpenter"
            money = 800
            break
        elif choice == 3 :
            # Farmer
            profession = "farmer"
            money = 400
            break
        elif choice == 4 :
            print(description)
            input("Press Enter To Continue")
            print()

    return (profession, money)

def name_members() :
    """Get the names of wagon leader and family members"""
    leader_name = get_name("\nWhat is the name of your wagon leader? ")

    # Ask how many family members
    num_family = get_number("\nHow many other family members? ", 1, 9)

    family_names = []

    # Get names of family members
    print()
    
    for i in range(num_family) :
        family_names.append(get_name(str.format("What is the name of member #{}? ", i + 1)))

    # Ask if they are sure, if not get number in range of the names and change it with get_name

    return (leader_name, family_names)

def get_name(question) :
    """Get name that is valid"""
    while True :
        name = input(question)

        if len(name) >= 2 and len(name) <= 16 :
            return name

def get_number(question, min, max) :
    """Gets number in range"""
    while True :
        number = int(input(question))

        # Check to make sure number only has digits not letters

        if number >= min and number <= max :
            return number
    
def shop(money,food,ammo,cloths,parts,oxen) :
    """Handles the shopping interface"""
    bill = 0
    items = ["Oxen","Food","Ammo","Cloths","Wagon Parts","Check Out"]
    spent_on_items = [0.00,0.00,0.00,0.00,0.00,bill]

    print("Before leaving Indipendance you should buy equipment and supplies.")
    print(str.format("You have ${} in cash, but you don't have to spend it all now", money))
    print("You can buy whatever you need at Matt's General Store.")
    input("Press Enter To Continue")

    while True :
        # Update bill in the list
        spent_on_items[len(spent_on_items) - 1] = bill

        print("Welcome to Matt's General Store")
        print("Here is a list of things you can buy")
        for i in range (len(items)):
            print(str.format(""))
    
#***********************************************************************************************************

# Display splash screen
logo_screen()

# Display start menu
start_screen()










