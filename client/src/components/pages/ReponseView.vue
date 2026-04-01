<script>
import RepondreQuestionnaire from "../repondre/RepondreQuestionnaire.vue";
import RepondreQuestions from "../repondre/RepondreQuestions.vue";

export default {
    components: { RepondreQuestionnaire, RepondreQuestions },
    data() {
        return { questionnaires: [], questions: [] };
    },
    methods: {
        getQuestions(args) {
            let response = fetch(`${args.uri}/questions`, { headers: { "Content-Type": "application/json" }, method: "GET" });
            response.then(
                result => result.json()
            ).then(
                result => this.questions = result["questions"]
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
    <h2>Questionnaires</h2>
    <ul>
        <RepondreQuestionnaire v-for="q in questionnaires" :questionnaire="q" @getQuestions="getQuestions" />
    </ul>
    <RepondreQuestions v-if="questions.length > 0" :questions="questions" />
</template>
