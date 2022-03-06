from sources import tools, demarrer
from sources.state import bureau,transition,niveau

def main():
    
    
    state_dict={
        'bureau':bureau.MainMenu(),
        'transition':transition.Transition(),
        'niveau':niveau.Niveau()
    }
    
    game= tools.Game(state_dict,'bureau')
    game.run()

if __name__ == '__main__':
    main()

