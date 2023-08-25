###########################################################################
##############                                         ####################
##############         SELAGSA MOFFO SERGEO            ####################
##############                                         ####################
###########################################################################
import os

# Crée l'arborescence de répertoires
os.makedirs("data/cleaned")
os.makedirs("data/raw")
os.makedirs("docs")
os.makedirs("models")
os.makedirs("notebooks")
os.makedirs("reports")
os.makedirs("src")

# Crée le fichier LICENSE
with open("LICENSE", "w") as f:
    f.write("MIT License\n")

# Crée le fichier Makefile
with open("Makefile", "w") as f:
    f.write("# Makefile\n")

# Crée le fichier main.ipynb dans le répertoire notebooks
with open("notebooks/main.ipynb", "w") as f:
    f.write("# Notebook principal\n")

# Crée le fichier README.md
with open("README.md", "w") as f:
    f.write("# Evaluation Cours de DevOps\n\n## Programme de création d'une Arborescence # ├── data               #  repertoire contenant des données (brutes, propres)")
# │   ├── cleaned  s\n\n
# │   └── raw s\n\n
# ├── docs               #  repertoire contenant toute documentation utile s\n\n
# ├── LICENSE s\n\n
# ├── Makefile           #  fichier permettant d'automatiser des taches s\n\n
# ├── models             #  repertoire contenant tous les modèles construits s\n\n
# ├── notebooks          #  repertoire contenant tous les notebooks rédigés s\n\n
# │   └── main.ipynb s\n\n
# ├── README.md
# ├── reports            #  repertoire contenant tous les rapports générés
# ├── requirements.txt   #  fichier contenant la liste des dépendances du projets
# └── src                #  repertoire contenant tout code python utile
#     └── utils.py

# Crée le fichier requirements.txt
with open("requirements.txt", "w") as f:
    f.write("# Liste des dépendances\n")

# Crée le fichier utils.py dans le répertoire src
with open("src/utils.py", "w") as f:
    f.write("# Fonctions utilitaires\n")