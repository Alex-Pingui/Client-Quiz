<script>
export default {
    data() {
        return {
            showQuestions: false
        };
    },
    props: {
        questions: Array
    },
    methods: {
        getURIQuestionnaire() {
            return this.questionnaire.uri;
        },
    }
}
</script>

<template>
    <div v-if="showQuestions" class="mt-3">
        <h4>Questions</h4>

        <ul v-if="
            Array.isArray(questions) &&
            questions.length
        ">
            <li v-for="question in questions">
                {{ question.enonce }}
                <button class="btn btn-danger btn-sm" type="button" @click="supprimerQuestion(question)">
                    Supprimer
                </button>
            </li>
        </ul>

        <p v-else>Aucune question pour l’instant.</p>

        <CreationQuestion :questionnaire-id="questionnaire.id" @add="addQuestion" />
    </div>
</template>