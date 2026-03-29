<script>
import AjoutQuestion from "./AjoutQuestion.vue";
import EditionQuestion from "./EditionQuestion.vue";

export default {
  components: {EditionQuestion, AjoutQuestion },
  props: {
    questions: Array,
    questionnaireUri: String
  },
  methods: {
    ajouterQuestion(args){
      this.$emit("ajouterQuestion", args);
    },
    supprimerQuestion(args){
      this.$emit("supprimerQuestion", args);
    }
  },
  emits: ["supprimerQuestion", "ajouterQuestion"]
};
</script>

<template>
  <div>
    <h4>Questions</h4>

    <ul v-if="questions.length>0">
      <EditionQuestion v-for="question in questions"
                       :question="question"
                       :questionnaireUri="questionnaireUri"
                       @supprimerQuestion="supprimerQuestion"
      />
    </ul>
    <p v-else>Aucune question pour l’instant.</p>

    <AjoutQuestion @ajouterQuestion="ajouterQuestion"
                   :questionnaireUri="questionnaireUri"
    />
  </div>
</template>
