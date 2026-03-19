<script>
import Questionnaire from "./components/Questionnaire.vue";

export default {
  components: {Questionnaire},
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
            if(result.status === 200){
              this.questionnaires.splice(this.questionnaires.findIndex(questionnaire => questionnaire.id===questionnaireId), 1);
            }
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
}
</script>

<template>
  <h1>{{title}}</h1>
  <ul>
    <Questionnaire :questionnaire="questionnaire" v-for="questionnaire in questionnaires" @supprimerQuestionnaire="supprimerQuestionnaire"/>
  </ul>
</template>

<style scoped>
</style>
