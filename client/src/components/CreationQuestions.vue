<script>
export default {
  props: {
    uri: String
  },
  data() {
    return {
      newQuestion: {
        enonce: "",
        reponse: "",
        proposition_a: "",
        proposition_b: ""
      }
    };
  },
  methods: {
    submitQuestion() {
      this.$emit("add", {
        question: { ...this.newQuestion }
      });
      this.newQuestion = { enonce: "", reponse: "", proposition_a: "", proposition_b: "" };
    },
    supprimerQuestionnaire(args) {
      let questionnaireUri = args.uri;
      let response = fetch(questionnaireUri, { headers: { "Content-Type": "application/json" }, method: "DELETE" });
      response.then(
        result => result.json()
      ).then(
        result => {
          this.questionnaires = this.questionnaires.filter(questionnaire => questionnaire.uri !== questionnaireUri);
        }
      ).catch(error => console.log(error));
    }
  },
  emits: ["add", "delete"]
};
</script>

<template>
  <div class="text">
    <div class="input-group mt-2">
      <input v-model="newQuestion.enonce" placeholder="Énoncé" type="text" class="form-control">
      <input v-model="newQuestion.reponse" placeholder="Réponse" type="text" class="form-control">
      <input v-model="newQuestion.proposition_a" placeholder="Proposition A (optionnel)" type="text"
        class="form-control">
      <input v-model="newQuestion.proposition_b" placeholder="Proposition B (optionnel)" type="text"
        class="form-control">
      <button @click="submitQuestion" class="btn btn-primary">Ajouter question</button>
    </div>
  </div>
</template>
