<script>
import EditionQuestionnaire from "../edition/EditionQuestionnaire.vue";
import AjoutQuestionnaire from "../edition/AjoutQuestionnaire.vue";

export default {
    components: { EditionQuestionnaire, AjoutQuestionnaire },
    data() {
        return { questionnaires: [] };
    },
    methods: {
        ajouterQuestionnaire(args) {
            let nomQuestionnaire = args.nomQuestionnaire;
            let sent = { "name": nomQuestionnaire.trim() };
            let response = fetch("http://localhost:5000/quiz/api/v1.0/questionnaires", { headers: { "Content-Type": "application/json" }, method: "POST", body: JSON.stringify(sent) });
            response.then(
                result => result.json()
            ).then(
                result => {
                    this.questionnaires.push(result["questionnaire"]);
                }
            ).catch(error => console.log(error));
        },
        modifierQuestionnaire(args) {
            let questionnaireUri = args.uri;
            let nomQuestionnaire = args.nomQuestionnaire;
            let sent = { "name": nomQuestionnaire.trim() };
            let response = fetch(questionnaireUri, { headers: { "Content-Type": "application/json" }, method: "PUT", body: JSON.stringify(sent) });
            response.then(
                result => result.json()
            ).then(
                result => {
                    let resultQuestionnaire = result["questionnaire"];
                    this.questionnaires.find(questionnaire => questionnaire.uri === resultQuestionnaire.uri).name = resultQuestionnaire.name;
                }
            ).catch(error => console.log(error));
        },
        supprimerQuestionnaire(args) {
            let questionnaireUri = args.uri;
            let response = fetch(questionnaireUri, { headers: { "Content-Type": "application/json" }, method: "DELETE" });
            response.then(
                result => {
                    if (result.ok) this.questionnaires.splice(this.questionnaires.findIndex(questionnaire => questionnaire.uri === questionnaireUri), 1);
                }
            ).catch(error => console.log(error));
        },
        ajouterQuestion(args) {
            let questionnaireUri = args.questionnaireUri;
            let question = args.newQuestion;

            let sent = {
                "enonce": question.enonce.trim(),
                "reponse": question.reponse.trim()
            };
            if (question.proposition_a.length > 0) sent["proposition_a"] = question.proposition_a.trim();
            if (question.proposition_b.length > 0) sent["proposition_b"] = question.proposition_b.trim();

            let response = fetch(`${questionnaireUri}/questions`, {
                headers: { "Content-Type": "application/json" },
                method: "POST",
                body: JSON.stringify(sent)
            });
            console.log(response);

            response.then(
                result => result.json()
            ).then(result => {
                let newQuestion = result["question"];
                let questionnaire = this.questionnaires.find(questionnaire => questionnaire.uri === questionnaireUri);

                if (!questionnaire.questions) questionnaire.questions = [];
                questionnaire.questions.push(newQuestion);
            }
            ).catch(console.error);
        },
        supprimerQuestion(args) {
            let questionUri = args.uri;
            let questionnaireUri = args.questionnaireUri;

            let response = fetch(questionUri, { method: "DELETE", headers: { "Content-Type": "application/json" } });
            response.then(
                result => {
                    if (result.ok) {
                        let questionnaire = this.questionnaires.find(questionnaire => questionnaire.uri === questionnaireUri);
                        if (questionnaire.questions) questionnaire.questions.splice(questionnaire.questions.findIndex(question => question.uri === questionUri), 1);
                    }
                }
            ).catch(error => console.log(error));
        }
    },
    mounted() {
        fetch("http://localhost:5000/quiz/api/v1.0/questionnaires", { headers: { "Content-Type": "application/json" }, method: "GET" })
            .then(r => r.json())
            .then(r => this.questionnaires = r["questionnaires"]);
    }
}
</script>

<template>
    <h2>Édition des questionnaires</h2>
    <ul>
        <EditionQuestionnaire v-for="q in questionnaires" :questionnaire="q"
            @supprimerQuestionnaire="supprimerQuestionnaire" @modifierQuestionnaire="modifierQuestionnaire"
            @ajouterQuestion="ajouterQuestion" @supprimerQuestion="supprimerQuestion" />
    </ul>
    <h2>Ajouter un questionnaire</h2>
    <AjoutQuestionnaire @ajouterQuestionnaire="ajouterQuestionnaire" />
</template>