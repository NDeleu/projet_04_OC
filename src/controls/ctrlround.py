
"""
Lancer un nouveau round + vérifier et créer le nom du nouveau round + l'ajouter à la liste tournoi.round
!!!
a rework pour ne pas devoir utiliser un compter check round, mais en considérant la liste préalablement établie
ds tournoi (tournoi.round) : exemple : round{}.format(len(self.tournoi)      ???
Ou check directement ac le nom du précédent round ???
!!!

def round_start(self):
    if "round{}".format(self.check_round) not in self.round_match:
        self.round_match["round{}".format(self.check_round)] = []
        if "round{}".format(self.check_round) == "round1":
            self.first_round()
        else:
            self.other_round()
    else:
        if self.check_match < int(len(self.liste_joueur) / 2):
            print(
                "Vous n'avez pas fini le round en cours, veuillez saisir le résultat de tous les matchs du round en cours")
        else:
            self.check_round += 1
            self.check_match = 0
            self.round_start()
"""


"""
Lancer les matchs du premier round (ac ses règles spécifiques)
!!!
Parait bon, à recheck => changer la forme du for ac [for ... i in ...]
!!!

def first_round(self):
    sorted_by_classement = sorted(self.liste_joueur, key=lambda x: x.classement)
    for y in range(int(len(sorted_by_classement) / 2)):
        self.round_match["round{}".format(self.check_round)].append(
            (sorted_by_classement[y], sorted_by_classement[y + (int(len(sorted_by_classement) / 2))]))
"""


"""
Lancer les matchs des autres rounds (ac ses règles spécifiques)
!!!
L'idée est correct, mais préférer for à while, maybe implanter un système de pts aux joueurs, ou recalculer en fonction
des pts dans matchs (si pas trop long !), enfin fr passer la boucle for à [for ... i in ...]
!!!

def other_round(self):
    y = 0
    i = 1
    sorted_by_roundpoint = sorted(self.liste_joueur, key=lambda x: x.round_point)  # self.resultat joueur ?
    while int(len(self.round_match["round{}".format(self.check_round)]) < int(len(self.liste_joueur) / 2)):
        if (sorted_by_roundpoint[y], sorted_by_roundpoint[y + 1]) or (
                sorted_by_roundpoint[y + 1], sorted_by_roundpoint[y]) not in self.round_match:
            self.round_match["round{}".format(self.check_round)].append(
                (sorted_by_roundpoint[y], sorted_by_roundpoint[y + i]))
            del (sorted_by_roundpoint[y + i])
            del (sorted_by_roundpoint[y])
            i = 1
        else:
            i += 1
"""

