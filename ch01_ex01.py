import random
import textwrap

def print_bold(msg, end='\n'):
    """Print a string in 'bold' font"""
    txt = '\033[1m' + msg + '\033[0m'
    print( txt, end=end)

def print_dotted_line(width=72):
    """Print a dotted (rather 'dashed') line"""
    print('-'*width)

def show_theme_message(width=72):
    print_dotted_line()
    print_bold('Attack of the Orcs v0.0.1:')

    msg= (
       "The war between humans and their arch enemies, Orcs, was in the "
       "offing.  Sir Foo, one of the brave knights guarding the southern "
       "plains began a long journey towards the east through an unknown "
       "dense forest.  On his way, he spotted a small isolated settlement."
       " Tired and hoping to replenish his food stock, he decided to take "
       "a detour.  As he approached the village, he saw five huts.  There "
       "was no one to be seen around.  Hesitantly, he decided to enter..")
    print (textwrap.fill(msg,width=width))

def show_game_mission():
    print_bold('Mission:')
    print("\tChoose a hut where Sir Foo can rest...")
    print_bold('TIP:')
    print("Be careful as there are enemies lurking around!")    
    print_dotted_line()


def occupy_huts():
    huts = []
    occupants = ['enemy','friend','unoccupied']
    # Randomly append 'enemy or 'friend' or None to the huts list
    while len(huts) < 5:
        computer_choice = random.choice(occupants)
        huts.append(computer_choice)
    return huts


def process_user_choice():
    """Prompt user to select a hut"""
    msg = '\033[1m' + 'Choose a hut number to enter (1-5): ' + '\033[0m'
    user_choice = input("\n" + msg)
    msg=""
    return int(user_choice)

        
def reveal_occupants(idx, huts):
    """Print the occupants of the hut""" 
    msg=""
    print("Revealing the occupants...")
    for i in range(len(huts)):
        occupant_info = "<%d:%s>"%(i+1, huts[i])
        if i + 1 == idx:
            occupant_info = '\033[1m' + occupant_info + '\033[0m'
        msg += occupant_info + " "
    print ( "\t" + msg)
    print_dotted_line ()

def reset_health_meter(health_meter):
    """Reset the values of health_meter dict to the original ones"""
    health_meter['player'] = 40
    health_meter['enemy'] = 30

def show_health(health_meter, bold=False):
    """Show the remaining hit points of the player and the enemy"""
    msg = "Health: Sir Foo: %d, Enemy: %d" \
          % (health_meter['player'], health_meter['enemy'])

    if bold:
        print_bold(msg)
    else:
        print(msg)

def attack(health_meter):
    hit_list = 4 * ['player'] + 6 * ['enemy']
    injured_unit = random.choice(hit_list)
    hit_points = health_meter[injured_unit]
    injury = random.randint(10,15)
    health_meter[injured_unit] = max(hit_points - injury, 0)
    print("ATTACK! ", end='')
    show_health(health_meter)

def play_game(health_meter):
    huts = occupy_huts()
    idx = process_user_choice()
    reveal_occupants(idx, huts)

    # print_bold('Entering hut %d... ' % idx, end=" ")

    # Determine and announce the winner
    if huts[idx-1] != 'enemy':
        print_bold( 'Congratulations! YOU WIN!!!:' )
    else:
        print_bold('ENEMY SIGHTED! ', end='')
        show_health(health_meter, bold=True)
        contine_attack = True

        while contine_attack:
            contine_attack = input("......continue attack? (y/n): ")
            if contine_attack == 'n':
                print_bold("RUNNING AWAY with following health status...")
                show_health(health_meter, bold=True)
                print_bold("GAME OVER!")
                break
            
            attack(health_meter)

            if health_meter['enemy'] <= 0:
                print_bold('GOOD JOB! Enemy defeated! YOU WIN!!!')
                break

            if health_meter['player'] <= 0:
                print_bold("YOU LOSE  :(  Better luck next time")
                break

    print_dotted_line()

def run_application():
    health_meter = {}
    reset_health_meter(health_meter)

    show_theme_message()
    show_game_mission()

    keep_playing = 'y'
    while keep_playing == 'y':
        reset_health_meter(health_meter)
        play_game(health_meter)
        keep_playing = input("Play again? Yes(y)/No(n):")

if __name__ == '__main__':
    run_application()