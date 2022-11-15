"""Module Quoridor

Functions:
    * analyser_commande - Génère un interpréteur de commande.
    * formater_légende - Formater la représentation graphique du damier.
    * formater_damier - Formater la représentation graphique de la légende.
    * formater_jeu - Formater la représentation graphique d'un jeu.
    * formater_les_parties - Formater la liste des dernières parties.
    * récupérer_le_coup - Demander le prochain coup à jouer au joueur.
"""
import argparse


def analyser_commande():
    """Génère un interpréteur de commande.

    Returns:
        Namespace: Un objet Namespace tel que retourné par parser.parse_args().
                   Cette objet aura l'attribut «idul» représentant l'idul du joueur
                   et l'attribut «parties» qui est un booléen True/False.
    """
    parser = argparse.ArgumentParser()

    # Complétez le code ici
    # vous pourriez aussi avoir à ajouter des arguments dans ArgumentParser(...)

    return parser.parse_args()


def formater_légende(joueurs):
    """Formater la représentation graphique de la légende.

    Args:
        joueurs (list): Liste de dictionnaires représentant les joueurs.

    Returns:
        str: Chaîne de caractères représentant la légende.
    """
    
    if len(joueurs[0]['nom']) > len(joueurs[1]['nom']):
        c_1 = 1
        c_2 = len(joueurs[0]['nom']) - len(joueurs[1]['nom']) + 1
        
    elif len(joueurs[1]['nom']) > len(joueurs[0]['nom']):
        c_1 = len(joueurs[1]['nom']) - len(joueurs[0]['nom']) + 1
        c_2 = 1
        
    else:
        c_1, c_2 = 1, 1
    
    
    return (f"Légende:\n   1={joueurs[0]['nom']},{c_1*' '}murs={joueurs[0]['murs']*'|'}\n   2={joueurs[1]['nom']},{c_2*' '}murs={joueurs[1]['murs']*'|'}")

def formater_damier(joueurs, murs):
    """Formater la représentation graphique du damier.

    Args:
        joueurs (list): Liste de dictionnaires représentant les joueurs.
        murs (dict): Dictionnaire représentant l'emplacement des murs.

    Returns:
        str: Chaîne de caractères représentant le damier.
    """
    pass


def formater_jeu(état):
    """Formater la représentation graphique d'un jeu.

    Doit faire usage des fonctions formater_légende et formater_damier.

    Args:
        état (dict): Dictionnaire représentant l'état du jeu.

    Returns:
        str: Chaîne de caractères représentant le jeu.
    """
    pass


def formater_les_parties(parties):
    """Formater une liste de parties
    L'ordre rester exactement la même que ce qui est passé en paramètre.

    Args:
        parties (list): Liste des parties

    Returns:
        str: Représentation des parties
    """
    x = ''
    count = 1
    
    for partie in parties:
        
        if partie['gagnant'] == None:
            a = f"{count} : {partie['date']}, {partie['joueurs'][0]} vs {partie['joueurs'][1]}\n"
        
        else:
            a = f"{count} : {partie['date']}, {partie['joueurs'][0]} vs {partie['joueurs'][1]}, {partie['gagnant']}\n"
            
        x += a
        count += 1
        
    return x


def récupérer_le_coup():
    """Récupérer le coup

    Returns:
        tuple: Un tuple composé d'un type de coup et de la position.
               Le type de coup est une chaîne de caractères.
               La position est une liste de 2 entier [x, y].
    Examples:
        Quel type de coup voulez-vous jouer? ('D', 'MH', 'MV'):
        Donnez la position où appliquer ce coup (x,y): 2,6
    """
    
    type_coup = input("Quel type de coup voulez-vous jouer? ('D', 'MH', 'MV'):")
    while type_coup != 'D' and type_coup != 'MH' and type_coup != 'MV':
        type_coup = input("Quel type de coup voulez-vous jouer? ('D', 'MH', 'MV'):")

    position = input("Donnez la position où appliquer ce coup (x, y):")
    return f"{type_coup} : ({position})" 