<script>
import BilanQuiz from "./BilanQuiz.vue";

export default {
  components: {BilanQuiz},
  props: {
    questions: Array
  },
  data(){
    return {
      quizValide: false,
      scoreQuiz: 0,
      scoreMax: 0,
      reponsesSelectionnees: {},
      questionsBilan: []
    }
  },
  methods: {
    verifierReponses(){
      this.quizValide = true;
      this.scoreMax=this.questions.length;
      for(let question of this.questions){
        let reponseEntree=this.reponsesSelectionnees[question.uri];
        let estCorrect=question.reponse===reponseEntree;
        this.scoreQuiz+=estCorrect?1:0;
        this.questionsBilan.push({
          "enonce": question.enonce,
          "reponse": reponseEntree,
          "reponse_correct": question.reponse,
          "correct": estCorrect
        });
      }
    },
    resetQuestionnaire(){
      this.quizValide=false;
      this.scoreQuiz=0;
      this.reponsesSelectionnees={};
      this.questionsBilan=[];
    }
  },

};
</script>

<template>
  <h2>Questions</h2>
  <ul>
    <li v-for="question in questions">
      <h3>{{question.enonce}}</h3>
      <input type="text" v-if="question.proposition_a==null" v-model="reponsesSelectionnees[question.uri]">
      <ul v-else>
        <li><input :name="question.enonce" type="radio" :value="question.proposition_a" v-model="reponsesSelectionnees[question.uri]">{{question.proposition_a}}</li>
        <li><input :name="question.enonce" type="radio" :value="question.proposition_b" v-model="reponsesSelectionnees[question.uri]">{{question.proposition_b}}</li>
      </ul>
    </li>
  </ul>
  <button v-if="!quizValide" @click="verifierReponses">Valider</button>
  <button v-if="quizValide" @click="resetQuestionnaire">Refaire le questionnaire</button>
  <BilanQuiz v-if="quizValide" :scoreObtenu="scoreQuiz" :scoreMax="scoreMax" :questions="questionsBilan"/>
</template>

<style scoped>

</style>