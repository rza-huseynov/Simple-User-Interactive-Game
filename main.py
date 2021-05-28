numlist = [0, 1, 2]

def display_list () :
    print('Here is the current list: \n')
    print(numlist)

def position_choice () :
    
    choice = 'WRONG'
    within_range = False
    
    while (not choice.isdigit() or not within_range) :
        
        choice = input('Please enter a number in range (0-2): ')
        
        if (not choice.isdigit()) :
            print('Sorry, the input must be a digit\n')
        else :
            if (int(choice) not in range(0, 3)) :
                print('Sorry, the input must be in range (0 - 2)\n')
            else :
                within_range = True
    
    return int(choice)

def value_choice (index) :
    
    choice = input('Please enter the desired new value: ')
    numlist[index] = choice
    
    display_list()

def gameon_choice() :
    
    Y_or_N = False
    last_choice = 'WRONG'
    
    while (not Y_or_N) :
        
        choice = input('Would you like to continue the game?\nPlease press Y or N: ')
        
        if (choice not in ['Y', 'N']) :
            print('Sorry, I could not understand you, try again please\n')
        else :
            Y_or_N = True
            last_choice = choice
            
    return (last_choice == 'Y')

#gameplay

gameon = True

while (gameon) :
    
    #Display the current list
    display_list()
    
    #Choosing an index
    index = position_choice()
    
    #Choosing a new value
    value_choice(index)
    
    #Game on or not
    gameon = gameon_choice()
