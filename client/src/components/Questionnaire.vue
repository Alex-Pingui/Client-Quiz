<script>
import CreationQuestion from "./CreationQuestions.vue";

export default {
  components: { CreationQuestion },
  props: {
    questionnaire: Object
  },
  data() {
    return {
      nomQuestionnaire: "",
      showQuestions: false
    };
  },
  methods: {
    fetchQuestions() {
      if (this.showQuestions) {
        this.showQuestions = false;
        return;
      }
      fetch(this.questionnaire.uri + "/questions", {
        headers: { "Content-Type": "application/json" },
        method: "GET"
      }
      )
        .then(result => result.json())
        .then(result => {
          this.questionnaire.questions = result["questions"];
          this.showQuestions = !this.showQuestions;
          console.log(this.questionnaire);
        })
        .catch(error => console.log(error));
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
  <li>
    <span>
      {{ questionnaire.name }}
      <button class="btn btn-default" type="button" @click="fetchQuestions">
        Questions
      </button>
    </span>

    <div class="input-group">
      <input placeholder="Modifier le nom du questionnaire" type="text" class="form-control"
        v-model="nomQuestionnaire" />
      <span class="input-group-btn">
        <button class="btn btn-default" type="button" @click="modifierQuestionnaire">
          Modifier
        </button>
      </span>
    </div>

    <input type="button" class="btn btn-danger" value="Supprimer" @click="supprimerQuestionnaire" />


  </li>
</template>
