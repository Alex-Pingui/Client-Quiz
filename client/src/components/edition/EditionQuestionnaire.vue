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
      this.$emit("supprimerQuestionnaire", {uri: this.questionnaire.uri});
    },
    modifierQuestionnaire(){
      this.$emit("modifierQuestionnaire", {uri: this.questionnaire.uri, nomQuestionnaire: this.nomQuestionnaire});
    }
  }
};
</script>

<template>
  <ul>
    <li>
      <span>
        {{ questionnaire.name }}
        <button class="btn btn-default" @click="getQuestions">Questions</button>
      </span>

      <div v-if="showQuestions">
        <EditionQuestions :questions="questionnaire.questions"
                          :questionnaireUri="questionnaire.uri"
                          @supprimerQuestion="supprimerQuestion"
                          @ajouterQuestion="ajouterQuestion"
        />
      </div>

      <div class="input-group">
        <h4>Modifier le questionnaire</h4>
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
