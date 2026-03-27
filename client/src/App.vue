<script>
import EditionQuestionnaire from "./components/edition/EditionQuestionnaire.vue";
import AjoutQuestionnaire from "./components/edition/AjoutQuestionnaire.vue";
import RepondreQuestionnaire from "./components/repondre/RepondreQuestionnaire.vue";
import RepondreQuestions from "./components/repondre/RepondreQuestions.vue";

export default {
  components: {RepondreQuestions, RepondreQuestionnaire, AjoutQuestionnaire, EditionQuestionnaire},
  data(){
    return {
      title: "Quiz",
      questionnaires: [],
      questions: []
    };
  },
  methods: {
    supprimerQuestionnaire(args){
      let questionnaireUri=args.uri;
      let response=fetch(questionnaireUri, {headers: {"Content-Type": "application/json"}, method: "DELETE"});
      response.then(
          result => {
            if(result.status === 200) this.questionnaires.splice(this.questionnaires.findIndex(questionnaire => questionnaire.uri===questionnaireUri), 1);
          }
      ).catch(error => console.log(error));
    },
    modifierQuestionnaire(args){
      let questionnaireUri=args.uri;
      let nomQuestionnaire=args.nomQuestionnaire;
      let sent={"name":nomQuestionnaire};
      let response=fetch(questionnaireUri, {headers: {"Content-Type": "application/json"}, method: "PUT", body: JSON.stringify(sent)});
      response.then(
          result => result.json()
      ).then(
          result => {
            let resultQuestionnaire=result["questionnaire"];
            this.questionnaires.find(questionnaire => questionnaire.uri===resultQuestionnaire.uri).name=resultQuestionnaire.name;
          }
      ).catch(error => console.log(error));
    },
    ajouterQuestionnaire(args){
      let nomQuestionnaire=args.nomQuestionnaire;
      let sent={"name":nomQuestionnaire};
      let response=fetch("http://localhost:5000/quiz/api/v1.0/questionnaires", {headers: {"Content-Type": "application/json"}, method: "POST", body: JSON.stringify(sent)});
      response.then(
          result => result.json()
      ).then(
          result => {
            this.questionnaires.push(result["questionnaire"]);
          }
      ).catch(error => console.log(error));
    },
    getQuestions(args){
      let response=fetch(`${args.uri}/questions`, {headers: {"Content-Type": "application/json"}, method: "GET"});
      response.then(
          result => result.json()
      ).then(
          result => this.questions=result["questions"]
      ).catch(error => console.log(error));
    }
  },
  mounted() {
    let questionnaires=fetch("http://localhost:5000/quiz/api/v1.0/questionnaires", {headers: {"Content-Type": "application/json"}, method: "GET"});
    questionnaires.then(
        result => result.json()
    ).then(
        result => {
          this.questionnaires = result["questionnaires"];
        }
    ).catch(error => console.log(error));
  }
};
</script>

<template>
  <h1>{{title}}</h1>
  <h2>Questionnaires</h2>
  <ul>
    <RepondreQuestionnaire :questionnaire="questionnaire"
                           v-for="questionnaire in questionnaires"
                           @getQuestions="getQuestions"
    />
  </ul>
  <RepondreQuestions v-if="questions.length>0" :questions="questions"/>
</template>

<style scoped>
</style>
