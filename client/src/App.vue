<script>
import Questionnaire from "./components/Questionnaire.vue";
import AjoutQuestionnaire from "./components/AjoutQuestionnaire.vue";

export default {
  components: {AjoutQuestionnaire, Questionnaire},
  data(){
    return {
      title: "Quiz",
      questionnaires: []
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
    <Questionnaire :questionnaire="questionnaire"
                   v-for="questionnaire in questionnaires"
                   @supprimerQuestionnaire="supprimerQuestionnaire"
                   @modifierQuestionnaire="modifierQuestionnaire"
    />
  </ul>
  <h2>Ajouter un questionnaire</h2>
  <AjoutQuestionnaire @ajouterQuestionnaire="ajouterQuestionnaire"/>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
