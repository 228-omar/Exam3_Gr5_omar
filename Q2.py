import datetime
import locale
locale.setlocale(locale.LC_TIME,'')



def afficher_jours_examens(p_horaire_examen: dict) -> list:
    """
    Cette fonction sert à extraire les jours de la semaines où il y a des examens
    :param p_horaire_examen: dictionnaire contenant les dates d'examens
    :return: une liste de jours de la semaine
    """
    for  value in p_horaire_examen.items():
            jours = []
            date_examen = datetime.datetime.strptime(horaire_examen[value], "%Y-%m-%d")
            j = date_examen.strftime("%A")
            jours.append(j)
            print(f"Les examens sont {jours} ")
            print(jours)
    return jours



if __name__ == '__main__':


    horaire_examen = {
        "math" : "10/12/2025",
        "anglais" : "12/12/2025",
        "français" : "15/12/2025"
    }
    print("Les examens sont :", ", ".join(afficher_jours_examens(horaire_examen)))
