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
  mounted() {
    let questionnaires=fetch("http://localhost:5000/quiz/api/v1.0/questionnaires", {headers: {"Content-Type": "application/json"}, method: "GET"});
    questionnaires.then(
        result => result.json()
    ).then(
        result => {
          this.questionnaires = result["questionnaires"];
          console.log(this.questionnaires);
        }
    ).catch(error => console.log(error));
  }
}
</script>

<template>
  <h1>{{title}}</h1>
  <ul>
    <Questionnaire :questionnaire="questionnaire" v-for="questionnaire in questionnaires"/>
  </ul>
</template>

<style scoped>
</style>
