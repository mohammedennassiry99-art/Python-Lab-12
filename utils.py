import numpy as np

def stats_globales(notes):
    return {
        "moyenne": np.mean(notes),
        "min": np.min(notes),
        "max": np.max(notes),
        "ecart_type": np.std(notes)
    }

def stats_par_epreuve(notes):
    return np.mean(notes, axis=0)

def stats_par_etudiant(notes):
    return np.mean(notes, axis=1)

def top_etudiant(noms, notes):
    moyennes = stats_par_etudiant(notes)
    idx = np.argmax(moyennes)
    return noms[idx], moyennes[idx]

def epreuve_difficile(epreuves, notes):
    moyennes = stats_par_epreuve(notes)
    idx = np.argmin(moyennes)
    return epreuves[idx], moyennes[idx]

def filtrer_admis(noms, notes, seuil=12):
    moyennes = stats_par_etudiant(notes)
    masque = moyennes >= seuil
    return noms[masque], notes[masque]

def enrichir_tableau(notes):
    moy_etudiants = stats_par_etudiant(notes)
    col_moy = moy_etudiants.reshape(-1, 1)
    return np.hstack((notes, col_moy))
