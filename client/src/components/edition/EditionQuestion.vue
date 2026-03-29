<script>
export default {
  props: {
    question: Object,
    questionnaireUri: String
  },
  methods: {
    supprimerQuestion(){
      this.$emit('supprimerQuestion', {uri: this.question.uri, questionnaireUri: this.questionnaireUri});
    }
  },
  emits: ["supprimerQuestion"]
};
</script>

<template>
  <div class="question-item">
    <p><strong>{{ question.enonce }}</strong></p>
    <p>Réponse : {{ question.reponse }}</p>
    <p v-if="question.proposition_a">A. {{ question.proposition_a }}</p>
    <p v-if="question.proposition_b">B. {{ question.proposition_b }}</p>
    <button class="btn btn-danger btn-sm" @click="supprimerQuestion">
      Supprimer
    </button>
  </div>
</template>
