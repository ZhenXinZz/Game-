from sources import tools, demarrer
from sources.state import bureau 

def main():
    game= tools.Game()
    state = bureau.MainMenu() #初始化主菜单界面
    game.run(state)

if __name__ == '__main__':
    main()

