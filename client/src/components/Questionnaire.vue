<script>
import CreationQuestions from "./CreationQuestions.vue";
import AfficherQuestions from "./AfficherQuestions.vue";

export default {
  components: { CreationQuestions, AfficherQuestions },
  props: {
    questionnaire: Object,
  },
  data() {
    return { showQuestionsLocal: false };
  },
  methods: {
    fetchQuestions() {
      if (this.showQuestionsLocal) {
        this.showQuestionsLocal = false;
        return;
      }
      fetch(this.questionnaire.uri + "/questions")
        .then(res => res.json())
        .then(res => {
          this.questionnaire.questions = res.questions || [];
          this.showQuestionsLocal = true;
        });
    },
    supprimerQuestionnaire() {
      this.$emit("supprimerQuestionnaire", { uri: this.questionnaire.uri });
    },
    modifierQuestionnaire() {
      this.$emit("modifierQuestionnaire", {
        uri: this.questionnaire.uri,
        nomQuestionnaire: this.nomQuestionnaire
      });
    },
    supprimerQuestion(question) {
      this.$emit("supprimerQuestion", { uri: question.uri });
    },
    ajouterQuestion(data) {
      fetch(data.uri + "/questions", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data.question)
      })
        .then(res => res.json())
        .then(newQuestion => {
          // On ajoute la nouvelle question à la liste locale pour l'affichage immédiat
          this.questionnaire.questions.push(newQuestion);
        });
    }
  },
  emits: [
    "supprimerQuestionnaire",
    "modifierQuestionnaire",
    "ajouterQuestion",
    "supprimerQuestion"
  ]
};
</script>

<template>
  <ul>
    <li>
      <span>
        {{ questionnaire.name }}
        <button class="btn btn-default" @click="fetchQuestions">Questions</button>
      </span>

      <div v-if="showQuestionsLocal">
        <AfficherQuestions 
          :questions="questionnaire.questions" 
          :questionnaire-id="questionnaire.id"
          @supprimer-question="(question) => $emit('supprimerQuestion', question)"
          @ajouter-question="(data) => $emit('ajouterQuestion', data)"
        />
      </div>

      <button class="btn btn-danger" @click="$emit('supprimerQuestionnaire', { uri: questionnaire.uri })">
        Supprimer
      </button>
    </li>
  </ul>
</template>

