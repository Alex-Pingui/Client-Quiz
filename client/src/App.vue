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
      //TODO: Utiliser l'URI plutot que l'id et utiliser cette URI dans le fetch
      let questionnaireId=args.id;
      let response=fetch(`http://localhost:5000/quiz/api/v1.0/questionnaires/${questionnaireId}`, {headers: {"Content-Type": "application/json"}, method: "DELETE"});
      response.then(
          result => {
            if(result.status === 200) this.questionnaires.splice(this.questionnaires.findIndex(questionnaire => questionnaire.id===questionnaireId), 1);
          }
      ).catch(error => console.log(error));
    },
    modifierQuestionnaire(args){
      let questionnaireId=args.id;
      let nomQuestionnaire=args.nomQuestionnaire;
      let sent={"name":nomQuestionnaire};
      let response=fetch(`http://localhost:5000/quiz/api/v1.0/questionnaires/${questionnaireId}`, {headers: {"Content-Type": "application/json"}, method: "PUT", body: JSON.stringify(sent)});
      response.then(
          result => {
            if(result.status === 200) this.questionnaires.find(questionnaire => questionnaire.id===questionnaireId).name=nomQuestionnaire;
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
  <div>
    <a href="https://vite.dev" target="_blank">
      <img src="/vite.svg" class="logo" alt="Vite logo" />
    </a>
    <a href="https://vuejs.org/" target="_blank">
      <img src="./assets/vue.svg" class="logo vue" alt="Vue logo" />
    </a>
  </div>
  <HelloWorld msg="Vite + Vue" />
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
