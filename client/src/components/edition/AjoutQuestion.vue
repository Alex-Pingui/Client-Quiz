<script>
export default {
  props: {
    questionnaireUri: String
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
    ajouterQuestion() {
      this.$emit("ajouterQuestion", {newQuestion: this.newQuestion, questionnaireUri: this.questionnaireUri});
      this.newQuestion = { enonce: "", reponse: "", proposition_a: "", proposition_b: "" };
    }
  },
  emits: ["ajouterQuestion"]
};
</script>

<template>
  <div class="card p-3 mt-3">
    <h5>Ajouter une question</h5>
    <div class="input-group mb-2">
      <input v-model="newQuestion.enonce" placeholder="Énoncé" type="text" class="form-control">
      <input v-model="newQuestion.reponse" placeholder="Réponse" type="text" class="form-control">
    </div>
    <div class="input-group mb-2">
      <input v-model="newQuestion.proposition_a" placeholder="Proposition A (question fermée)" type="text" class="form-control">
      <input v-model="newQuestion.proposition_b" placeholder="Proposition B (question fermée)" type="text" class="form-control">
      <button @click="ajouterQuestion" class="btn btn-primary">Ajouter</button>
    </div>
  </div>
</template>
