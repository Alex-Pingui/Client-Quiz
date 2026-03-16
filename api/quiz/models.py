from .app import db

def add_questionnaire(nom):
    questionnaire=Questionnaire(nom)
    db.session.add(questionnaire)
    db.session.commit()
    return questionnaire

def get_questionnaires():
    return Questionnaire.all()

def get_questionnaire(id_questionnaire):
    for questionnaire in Questionnaire.all():
        if questionnaire.id_questionnaire == id_questionnaire:
            return questionnaire
    return None

def remove_questionnaire(id_questionnaire):
    questionnaire=db.session.query(Questionnaire).filter_by(id_questionnaire=id_questionnaire).first()
    db.session.delete(questionnaire)
    db.session.commit()

def update_questionnaire(questionnaire, nom):
    questionnaire.nom = nom
    db.session.commit()
    return questionnaire

class Questionnaire(db.Model):
    __tablename__ = "QUESTIONNAIRE"

    id_questionnaire=db.Column(db.Integer, primary_key=True)
    nom=db.Column(db.String)

    def __init__(self, nom):
        self.id_questionnaire = len(Questionnaire.all())+1
        self.nom = nom

    @classmethod
    def all(cls):
        return db.session.query(Questionnaire).all()

    def to_json(self):
        return {"id":self.id_questionnaire, "name":self.nom}

    def add_question(self, enonce, reponse, proposition_a=None, proposition_b=None):
        if proposition_a is None and proposition_b is None:
            question = QuestionOuverte(self.id_questionnaire, len(self.get_questions())+1, enonce, reponse)
        else:
            question = QuestionFermee(self.id_questionnaire, len(self.get_questions())+1, enonce, proposition_a, proposition_b, reponse)
        db.session.add(question)
        db.session.commit()
        return question

    def update_question(self, num_question, enonce, reponse, proposition_a, proposition_b):
        question=self.get_question(num_question)
        question.enonce=enonce
        question.reponse=reponse
        if proposition_a is not None and proposition_b is not None:
            question.proposition_a=proposition_a
            question.proposition_b=proposition_b
        db.session.commit()
        return question

    def delete_question(self, num_question):
        question=db.session.query(Question).filter_by(id_questionnaire=self.id_questionnaire, num_question=num_question).first()
        db.session.delete(question)
        db.session.commit()

    def get_questions(self):
        return db.session.query(Question).filter_by(id_questionnaire=self.id_questionnaire).all()

    def get_question(self, num_question):
        return db.session.query(Question).filter_by(id_questionnaire=self.id_questionnaire, num_question=num_question).first()

class Question(db.Model):
    __tablename__ = "QUESTION"

    id_questionnaire=db.Column(db.Integer, db.ForeignKey("QUESTIONNAIRE.id_questionnaire"), primary_key=True)
    num_question=db.Column(db.Integer, primary_key=True)
    enonce=db.Column(db.String(30))
    type=db.Column(db.String(20)) # Permet de différencier les lignes de la bd (QUESTIONOUVERTE ou QUESTIONFERMEE)

    reponse=db.Column(db.String(50))
    proposition_a=db.Column(db.String(50))
    proposition_b=db.Column(db.String(50))

    __mapper_args__={
        "polymorphic_identity":"QUESTION",
        "polymorphic_on": type, # Lecture de la colonne type en bd pour savoir à quelle classe correspond chaque ligne
    }

    @classmethod
    def all(cls):
        return cls.query.all()

    def to_json(self):
        return {"num_question":self.num_question, "enonce":self.enonce}

class QuestionOuverte(Question):
    __mapper_args__ = {
        "polymorphic_identity":"QUESTIONOUVERTE", # polymorphic_identity dans les enfants: Valeur enregistré dans la colonne type en bd
    }

    def __init__(self, id_questionnaire, num_question, enonce, reponse):
        super().__init__(id_questionnaire=id_questionnaire, num_question=num_question, enonce=enonce, reponse=reponse)

    def to_json(self):
        return {"num_question": self.num_question, "enonce": self.enonce, "reponse": self.reponse}

class QuestionFermee(Question):
    __mapper_args__ = {
        "polymorphic_identity": "QUESTIONFERMEE",
    }

    def __init__(self, id_questionnaire, num_question, enonce, proposition_a, proposition_b, reponse):
        super().__init__(id_questionnaire=id_questionnaire, num_question=num_question, enonce=enonce, reponse=reponse, proposition_a=proposition_a, proposition_b=proposition_b)

    def to_json(self):
        return {"num_question": self.num_question, "enonce": self.enonce, "propositionA": self.proposition_a, "propositionB": self.proposition_b, "reponse": self.reponse}