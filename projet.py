import numpy as np
from utils import *

noms = np.array(["mohammed", "nizar", "simo", "mourad"])
epreuves = np.array(["E1", "E2", "E3"])

notes = np.array([
    [14.5, 16.0, 13.0],
    [11.0, 10.5, 12.5],
    [17.0, 18.5, 16.5],
    [9.0, 11.0, 10.0]
])


stats = stats_globales(notes)
print("Rapport :", stats)

moy_epreuves = stats_par_epreuve(notes)
print("Moyennes par epreuve :", moy_epreuves)

# Analyse par étudiant
moy_etudiants = stats_par_etudiant(notes)
print("Moyennes par etudiant :", moy_etudiants)

nom_top, moy_top = top_etudiant(noms, notes)
print(f"Best eudiant : {nom_top} ({moy_top:.2f})")


epreuve, moy = epreuve_difficile(epreuves, notes)
print(f"epreuve la plus difficile : {epreuve} ({moy:.2f})")


admis, notes_admis = filtrer_admis(noms, notes)
print("Etudiants admis :", admis)
print("Notes admis :\n", notes_admis)


notes_enrichies = enrichir_tableau(notes)
print("Notes avec moyenne :\n", notes_enrichies)
