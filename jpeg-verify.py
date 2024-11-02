import os
import argparse
from PIL import Image

# Fonction principale pour vérifier les images JPEG non valides
def trouver_jpeg_non_valides(chemin_arborescence):
    jpeg_non_valides = []
    # Parcourir l'arborescence
    for dossier, sous_dossiers, fichiers in os.walk(chemin_arborescence):
        for fichier in fichiers:
            if fichier.lower().endswith(('.jpg', '.jpeg')):
                chemin_fichier = os.path.join(dossier, fichier)
                try:
                    # Essayer d'ouvrir le fichier avec PIL
                    with Image.open(chemin_fichier) as img:
                        img.verify()  # Vérifier si l'image est valide
                except Exception:
                    # Si une exception est levée, le fichier est non valide
                    jpeg_non_valides.append(chemin_fichier)

    # Afficher les fichiers non valides trouvés
    print("Fichiers JPEG non valides trouvés :")
    for fichier in jpeg_non_valides:
        print(fichier)

# Configuration de l'argument de ligne de commande
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lister les images JPEG non valides dans une arborescence.")
    parser.add_argument("-i", "--input", required=True, help="Chemin de l'arborescence à scanner")

    args = parser.parse_args()
    trouver_jpeg_non_valides(args.input)
