<script>
import CreationQuestions from "./CreationQuestions.vue";

export default {
    name: 'AfficherQuestions',
    components: { CreationQuestions },
    props: {
        questions: Array,
        questionnaireUri: String
    },
    emits: ['supprimerQuestion', 'ajouterQuestion']
}
</script>

<template>
    <div>
        <h4>Questions</h4>

        <ul v-if="
            Array.isArray(questions) &&
            questions.length
        ">
            <li v-for="question in questions">
                {{ question.enonce }}
                <button class="btn btn-danger btn-sm" type="button" @click="($emit('supprimerQuestion', question))">
                    Supprimer
                </button>
            </li>
        </ul>

        <p v-else>Aucune question pour l’instant.</p>

        <CreationQuestions :questionnaire-uri="questionnaireUri" @add="(question) => $emit('ajouterQuestion', question)" />
    </div>
</template>