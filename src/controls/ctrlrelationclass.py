from src.controls.ctrlplayermethods import CtrlPlayerMethods
from src.controls.ctrltournamentmethods import CtrlTournamentMethods
from src.controls.ctrltournamentrunning import CtrlTournamentRunning
from src.controls.ctrlmanagermain import CtrlManagerMain
from src.controls.ctrlviewmain import CtrlViewMain
from src.controls.ctrlmainmenu import CtrlMainMenu
from src.controls.ctrltournamentmenu import CtrlTournamentMenu


class CtrlRelationClass:
    def __init__(self):
        self.view_main = CtrlViewMain()
        self.manager_main = CtrlManagerMain()
        self.tournament_methods = CtrlTournamentMethods(self.view_main, self.manager_main)
        self.tournament_running = CtrlTournamentRunning
        self.player_methods = CtrlPlayerMethods(self.view_main, self.manager_main)
        self.main_menu = CtrlMainMenu(self.view_main)
        self.tournament_menu = CtrlTournamentMenu()


class LeaveApplication(Exception):
    def __init__(self):
        self.view_main = CtrlViewMain()
        self.main_menu = CtrlMainMenu(self.view_main)

    def __str__(self):
        return self.main_menu.show_navigate_main_menu.show_leave_app()

    def __repr__(self):
        return self.__str__()


class LeaveTournament(Exception):
    def __init__(self, tournament_name):
        self.tournament_menu = CtrlTournamentMenu()
        self.tournament_name = tournament_name

    def __str__(self):
        return self.tournament_menu.quit_tournament(self.tournament_name)

    def __repr__(self):
        return self.__str__()
