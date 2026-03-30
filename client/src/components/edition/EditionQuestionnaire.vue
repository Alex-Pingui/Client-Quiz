<script>
import EditionQuestions from "./EditionQuestions.vue";

export default {
  components: {EditionQuestions},
  props: {
    questionnaire: Object
  },
  data(){
    return {
      nomQuestionnaire: "",
      showQuestions: false
    };
  },
  methods:{
    supprimerQuestionnaire(){
      this.$emit("supprimerQuestionnaire", {uri: this.questionnaire.uri});
    },
    modifierQuestionnaire(){
      this.$emit("modifierQuestionnaire", {uri: this.questionnaire.uri, nomQuestionnaire: this.nomQuestionnaire});
    },
    getQuestions() {
      if (this.showQuestions) {
        this.showQuestions = !this.showQuestions;
        return;
      }

      let response=fetch(`${this.questionnaire.uri}/questions`, {headers: {"Content-Type": "application/json"}, method: "GET"});
      response.then(
          result => result.json()
      ).then(
          result => {
            this.questionnaire.questions = result["questions"];
            this.showQuestions = true;
          }
      ).catch(error => console.log(error));
    },
    ajouterQuestion(args){
      this.$emit("ajouterQuestion", args);
    },
    supprimerQuestion(args){
      this.$emit("supprimerQuestion", args);
    }
  }
};
</script>

<template>
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
