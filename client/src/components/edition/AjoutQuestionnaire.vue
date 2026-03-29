<script>
export default {
  data() {
    return {
      nomQuestionnaire: ""
    };
  },
  methods: {
    submit() {
      if (!this.nomQuestionnaire) return;
      this.$emit("ajouterQuestionnaire", {
        nomQuestionnaire: this.nomQuestionnaire
      });
      this.nomQuestionnaire = "";
    }
  },
  emits: ["ajouterQuestionnaire"]
};
</script>

<template>
  <div class="input-group mt-2">
    <input
      v-model="nomQuestionnaire"
      placeholder="Nom du questionnaire"
      type="text"
      class="form-control"
    />
    <button @click="submit" class="btn btn-primary">Ajouter</button>
  </div>
</template>
