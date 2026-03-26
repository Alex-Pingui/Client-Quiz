<script>
import Questionnaire from "./components/Questionnaire.vue";
import AjoutQuestionnaire from "./components/AjoutQuestionnaire.vue";

export default {
  components: { AjoutQuestionnaire, Questionnaire },
  data() {
    return {
      title: "Quiz",
      questionnaires: []
    };
  },
  methods: {
    supprimerQuestionnaire(args) {
      const questionnaireUri = args.uri;
      fetch(questionnaireUri, {
        headers: { "Content-Type": "application/json" },
        method: "DELETE"
      })
        .then(result => {
          if (result.status === 200) {
            const index = this.questionnaires.findIndex(
              q => q.uri === questionnaireUri
            );
            if (index !== -1) this.questionnaires.splice(index, 1);
          }
        })
        .catch(error => console.log(error));
    },

    modifierQuestionnaire(args) {
      const questionnaireUri = args.uri;
      const nomQuestionnaire = args.nomQuestionnaire;
      const sent = { name: nomQuestionnaire };

      fetch(questionnaireUri, {
        headers: { "Content-Type": "application/json" },
        method: "PUT",
        body: JSON.stringify(sent)
      })
        .then(result => result.json())
        .then(result => {
          const resultQuestionnaire = result["questionnaire"];
          const q = this.questionnaires.find(
            questionnaire => questionnaire.uri === resultQuestionnaire.uri
          );
          if (q) q.name = resultQuestionnaire.name;
        })
        .catch(error => console.log(error));
    },

    ajouterQuestionnaire(args) {
      const nomQuestionnaire = args.nomQuestionnaire;
      const sent = { name: nomQuestionnaire };

      fetch("http://localhost:5000/quiz/api/v1.0/questionnaires", {
        headers: { "Content-Type": "application/json" },
        method: "POST",
        body: JSON.stringify(sent)
      })
        .then(result => result.json())
        .then(result => {
          this.questionnaires.push(result["questionnaire"]);
        })
        .catch(error => console.log(error));
    },

    ajouterQuestion(args) {
      const questionnaireId = args.id;
      const q = args.question;

      const sent = {
        enonce: q.enonce,
        reponse: q.reponse,
        proposition_a: q.proposition_a || null,
        proposition_b: q.proposition_b || null
      };

      fetch(
        `http://localhost:5000/quiz/api/v1.0/questionnaires/${questionnaireId}/questions`,
        {
          headers: { "Content-Type": "application/json" },
          method: "POST",
          body: JSON.stringify(sent)
        }
      )
        .then((result) => result.json())
        .then((result) => {
          const questionnaire = this.questionnaires.find(
            (q) => q.id === questionnaireId
          );
          if (questionnaire) {
            if (!questionnaire.questions) questionnaire.questions = [];
            questionnaire.questions.push(result["question"]);
          }
        })
        .catch(console.log);
    },
    supprimerQuestion(args) {
      const questionUri = args.uri;

      fetch(questionUri, {
        headers: { "Content-Type": "application/json" },
        method: "DELETE"
      })
        .then(result => {
          if (result.status === 200) {
            this.questionnaires.forEach(questionnaire => {
              if (!questionnaire.questions) return;
              const index = questionnaire.questions.findIndex(
                question => question.uri === questionUri
              );
              if (index !== -1) questionnaire.questions.splice(index, 1);
            });
          } else {
            console.log(`Failed to delete question at ${questionUri}`);
          }
        })
        .catch(error => console.log(error));
    }
  },
  mounted() {
    fetch("http://localhost:5000/quiz/api/v1.0/questionnaires", {
      headers: { "Content-Type": "application/json" },
      method: "GET"
    })
      .then(result => result.json())
      .then(result => {
        this.questionnaires = result["questionnaires"];
      })
      .catch(error => console.log(error));
  }
};
</script>

<template>
  <h1>{{ title }}</h1>

  <h2>Questionnaires</h2>
  <ul>
    <Questionnaire v-for="questionnaire in questionnaires" :key="questionnaire.id" :questionnaire="questionnaire"
      @supprimerQuestionnaire="supprimerQuestionnaire" @modifierQuestionnaire="modifierQuestionnaire"
      @ajouterQuestion="ajouterQuestion" @supprimerQuestion="supprimerQuestion" />
  </ul>

  <h2>Ajouter un questionnaire</h2>
  <AjoutQuestionnaire @ajouterQuestionnaire="ajouterQuestionnaire" />
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
