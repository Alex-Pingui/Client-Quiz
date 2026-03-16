from flask import jsonify, make_response, abort, request

from .app import app
from .models import get_questionnaires, get_questionnaire, add_questionnaire, remove_questionnaire, update_questionnaire

@app.route("/quiz/api/v1.0/questionnaires", methods=["GET"])
def get_questionnaires_view():
    return jsonify({"questionnaires": [questionnaire.to_json() for questionnaire in get_questionnaires()]}), 200

@app.route("/quiz/api/v1.0/questionnaires/<int:id_questionnaire>", methods=["GET"])
def get_questionnaire_view(id_questionnaire):
    questionnaire=get_questionnaire(id_questionnaire)

    if questionnaire is None:
        abort(404)

    return jsonify({"questionnaire": questionnaire.to_json()}), 200

@app.route("/quiz/api/v1.0/questionnaires", methods=["POST"])
def create_questionnaire_view():
    if not request.json or not "name" in request.json:
        abort(400)

    return jsonify({"questionnaire": add_questionnaire(request.json["name"]).to_json()}), 201

@app.route("/quiz/api/v1.0/questionnaires/<int:id_questionnaire>", methods=["PUT"])
def update_questionnaire_view(id_questionnaire):
    updated_questionnaire=get_questionnaire(id_questionnaire)

    if updated_questionnaire is None:
        abort(404)

    if not request.json:
        abort(400)

    if "name" in request.json and not isinstance(request.json["name"], str):
        abort(400)

    return jsonify({"questionnaire":update_questionnaire(updated_questionnaire, request.json["name"]).to_json()}), 200

@app.route("/quiz/api/v1.0/questionnaires/<int:id_questionnaire>", methods=["DELETE"])
def delete_questionnaire_view(id_questionnaire):
    deleted_questionnaire=get_questionnaire(id_questionnaire)

    if deleted_questionnaire is None:
        abort(404)

    remove_questionnaire(id_questionnaire)
    return jsonify({"status":"deleted"}), 200

@app.route("/quiz/api/v1.0/questionnaires/<int:id_questionnaire>/questions", methods=["GET"])
def get_questions_view(id_questionnaire):
    selected_questionnaire=get_questionnaire(id_questionnaire)

    if selected_questionnaire is None:
        abort(404)

    return jsonify({"questions":[question.to_json() for question in selected_questionnaire.get_questions()]}), 200

@app.route("/quiz/api/v1.0/questionnaires/<int:id_questionnaire>/questions/<int:num_question>", methods=["GET"])
def get_question_view(id_questionnaire, num_question):
    selected_questionnaire=get_questionnaire(id_questionnaire)

    if selected_questionnaire is None:
        abort(404)

    question=selected_questionnaire.get_question(num_question)
    if not question:
        abort(404)

    return jsonify({"question":question.to_json()}), 200

@app.route("/quiz/api/v1.0/questionnaires/<int:id_questionnaire>/questions", methods=["POST"])
def add_question_view(id_questionnaire):
    selected_questionnaire=get_questionnaire(id_questionnaire)

    if selected_questionnaire is None:
        abort(404)

    if not request.json:
        abort(400)

    if "enonce" in request.json and not isinstance(request.json["enonce"], str):
        abort(400)

    if "reponse" in request.json and not isinstance(request.json["reponse"], str):
        abort(400)

    if "proposition_a" in request.json and not isinstance(request.json["proposition_a"], str):
        abort(400)

    if "proposition_b" in request.json and not isinstance(request.json["proposition_b"], str):
        abort(400)

    question=selected_questionnaire.add_question(request.json["enonce"], request.json["reponse"], request.json.get("proposition_a", None), request.json.get("proposition_b", None))
    return jsonify({"question":question.to_json()}), 201

@app.route("/quiz/api/v1.0/questionnaires/<int:id_questionnaire>/questions/<int:num_question>", methods=["PUT"])
def update_question_view(id_questionnaire, num_question):
    selected_questionnaire=get_questionnaire(id_questionnaire)

    if selected_questionnaire is None:
        abort(404)

    question=selected_questionnaire.get_question(num_question)

    if not question:
        abort(404)

    if "enonce" in request.json and not isinstance(request.json["enonce"], str):
        abort(400)

    if "reponse" in request.json and not isinstance(request.json["reponse"], str):
        abort(400)

    if "proposition_a" in request.json and not isinstance(request.json["proposition_a"], str):
        abort(400)

    if "proposition_b" in request.json and not isinstance(request.json["proposition_b"], str):
        abort(400)

    question=selected_questionnaire.update_question(num_question, request.json.get("enonce", question.enonce), request.json.get("reponse", question.reponse), request.json.get("proposition_a", question.proposition_a), request.json.get("proposition_b", question.proposition_b))
    return jsonify({"question":question.to_json()}), 200

@app.route("/quiz/api/v1.0/questionnaires/<int:id_questionnaire>/questions/<int:num_question>", methods=["DELETE"])
def delete_question_view(id_questionnaire, num_question):
    selected_questionnaire=get_questionnaire(id_questionnaire)

    if selected_questionnaire is None:
        abort(404)

    deleted_question=selected_questionnaire.get_question(num_question)

    if deleted_question is None:
        abort(404)

    selected_questionnaire.delete_question(num_question)
    return {"status":"deleted"}, 200

@app.errorhandler(404)
def not_found(e):
    return make_response(jsonify({"error": "Not found"}), 404)

@app.errorhandler(400)
def bad_request(e):
    return make_response(jsonify({"error": "Bad request"}), 400)
