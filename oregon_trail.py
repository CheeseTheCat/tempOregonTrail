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

def play_game() :
    """The actual game function"""

    # Get profession and money that profession has
    prof_data = char_setup()
    profession = prof_data[0]
    money = prof_data[1]
    
    #Name Leader
    #name four others potato
    #and then confirm names

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

    
#***********************************************************************************************************

# Display splash screen
logo_screen()

# Display start menu
start_screen()










