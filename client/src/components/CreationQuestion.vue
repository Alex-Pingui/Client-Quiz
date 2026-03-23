<script>
export default {
  props: {
    question: {
      type: Object,
      required: true
    }
  },
  methods: {
    ajouter() {
      this.$emit('add', { id: this.question.id });
    },
    supprimer() {
      this.$emit('remove', { id: this.question.id });
    },
    modifier() {
      this.$emit('modify', { id: this.question.id });
    }
  },
  emits: ["add", "remove", "modify"]
}
</script>

<template>
  <div class="text">
    <label>
      {{ question.enonce }}
    </label>
    <div class="input-group mt-2">
      <input v-model="newQuestion.enonce" placeholder="Énoncé" type="text" class="form-control">
      <input v-model="newQuestion.reponse" placeholder="Réponse" type="text" class="form-control">
      <input v-model="newQuestion.proposition_a" placeholder="Proposition A (optionnel)" type="text"
        class="form-control">
      <input v-model="newQuestion.proposition_b" placeholder="Proposition B (optionnel)" type="text"
        class="form-control">
      <button @click="submitQuestion(questionnaire.id)" class="btn btn-primary">Ajouter question</button>
    </div>
    <!-- <input type="button" class="btn btn-warning" value="Modifier" @click="modifier">
        <input type="button" class="btn btn-danger" value="Supprimer" @click="supprimer"> -->
  </div>
</template>