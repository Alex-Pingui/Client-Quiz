<script>
export default {
  props: {
    questionnaire: Object
  },
  data(){
    return {
      nomQuestionnaire: ""
    };
  },
  methods:{
    supprimerQuestionnaire(){
      this.$emit("supprimerQuestionnaire", {id: this.questionnaire.id});
    },
    modifierQuestionnaire(){
      this.$emit("modifierQuestionnaire", {id: this.questionnaire.id, nomQuestionnaire: this.nomQuestionnaire});
    }
  }
};
</script>

<template>
  <li>
    <span>
      {{questionnaire.name}}
      <button class="btn btn-default">Questions</button>
    </span>
    <div class="input-group">
      <input placeholder="Modifier le nom du questionnaire"
             type="text"
             class="form-control"
             v-model="nomQuestionnaire"
      >
      <span class="input-group-btn">
      <button class="btn btn-default"
              type="button"
              @click="modifierQuestionnaire"
      >
        Modifier
      </button>
    </span>
    </div>
    <input type="button"
           class="btn btn-danger"
           value="Supprimer"
           @click="supprimerQuestionnaire"
    >
  </li>
</template>

<style scoped>

</style>