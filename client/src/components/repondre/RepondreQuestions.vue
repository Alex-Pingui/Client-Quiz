<script>
import BilanQuiz from "./BilanQuiz.vue";

export default {
  components: {BilanQuiz},
  props: {
    questions: Array
  },
  data(){
    return {
      questionsQuiz: this.questions,
      quizValide: false,
      scoreQuiz: 0,
      scoreMax: this.questions.length,
      reponsesSelectionnee: {}
    }
  },
  methods: {
    verifierReponses(){
      this.quizValide = true;
      console.log(this.reponsesSelectionnee);
    }
  },

};
</script>

<template>
  <h2>Questions</h2>
  <ul>
    <li v-for="question in questions">
      <h3>{{question.enonce}}</h3>
      <input type="text" v-if="question.proposition_a==null" v-model="reponsesSelectionnee">
      <ul v-else>
        <li><input v-bind:name="question.enonce" type="radio" v-bind:value="reponsesSelectionnee[question.enonce]=question.proposition_a">{{question.proposition_a}}</li>
        <li><input v-bind:name="question.enonce" type="radio" v-bind:value="reponsesSelectionnee[question.enonce]=question.proposition_b">{{question.proposition_b}}</li>
      </ul>
    </li>
  </ul>
  <button @click="verifierReponses">Valider</button>
  <BilanQuiz v-if="quizValide" :scoreObtenu="scoreQuiz" :scoreMax="scoreMax"/>
</template>

<style scoped>

</style>