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
    }
  }
}
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
             v-bind:value="nomQuestionnaire"
      >
      <span class="input-group-btn">
      <button class="btn btn-default"
              type="button">Modifier
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