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
    getQuestionnaireId() {
      // Extrait l'ID depuis l'URI : /quiz/api/v1.0/questionnaires/123 → 123
      if (this.questionnaire.id) return this.questionnaire.id;
      const match = this.questionnaire.uri.match(/questionnaires\/(\d+)/);
      return match ? parseInt(match[1]) : null;
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
        <!-- DEBUG : affiche l'ID disponible -->
        <p>DEBUG ID questionnaire : {{ questionnaire.id }} | {{ questionnaire.uri }}</p>

        <AfficherQuestions :key="showQuestionsLocal + (questionnaire.questions?.length || 0)"
          :questions="questionnaire.questions" :questionnaire-id="getQuestionnaireId()"
          @supprimerQuestion="(question) => $emit('supprimerQuestion', { uri: question.uri })"
          @ajouterQuestion="(data) => $emit('ajouterQuestion', data)" />
      </div>

      <button class="btn btn-danger" @click="$emit('supprimerQuestionnaire', { uri: questionnaire.uri })">
        Supprimer
      </button>
    </li>
  </ul>
</template>
