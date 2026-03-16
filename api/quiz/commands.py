from .app import app, db
from .models import add_questionnaire

@app.cli.command()
def syncdb():
    db.drop_all()
    db.create_all()

    qz1=add_questionnaire("REST")
    qz2=add_questionnaire("Calcul")
    qz3=add_questionnaire("Java")

    qz1.add_question("C'est quoi?", "Des bonnes pratiques")
    qz2.add_question("1+1", "2")
    qz3.add_question("Quel est le meilleur langage", "Java", "Java", "C")
    qz3.add_question("Qu'est ce qu'un attribut final", "Constante", "Constante", "Constructeur")

    print("Database initialized")
