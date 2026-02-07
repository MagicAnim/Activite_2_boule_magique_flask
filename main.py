# On importe le framework Flask
from flask import Flask, render_template, request
from random import choice


reponses_possibles = [" Essaye plus tard ",
"Essaye encore ",
"Pas d'avis ",
"C'est ton destin ",
"Le sort en est jeté ",
"Une chance sur deux ",
"Repose ta question ",
"D'après moi oui ",
"C'est certain ",
"Oui absolument ",
"Tu peux compter dessus ",
"Sans aucun doute ",
"Très probable ",
"Oui ",
"C'est bien parti ",
"C'est non ",
"Peu probable ",
"Faut pas rêver ",
"N'y compte pas ",
"Impossible ",
]

# On crée l'application = instance de la classe Flask
app = Flask(__name__)

# On crée le premier route : à la racine de notre application "/"
# @app.route() : ce décorateur permet d'associer une URL à une fonction
# root -> page racine de l'app web
@app.route("/", methods=["GET", "POST"])
def index():
    # On crée une variable réponse
    reponse = 0
    # On vérifie si l'ulisateur accède à la page d'accueil ou valide le bouton
    if request.method == "POST":
            reponse = choice(reponses_possibles)
    return render_template("index.html", reponse = reponse)




#########################################
#         TOUJOURS A LA FIN             #
#########################################
# On lance l'application avec la méthode run()
# host = '0.0.0.0' = toutes les interfaces reseaux peuvent y accéder
# port 81 = le port sur lequel le serveur Flask écoute
app.run(host = '0.0.0.0', port = 81)
