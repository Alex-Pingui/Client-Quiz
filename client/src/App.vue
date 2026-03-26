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
    ajouterQuestion(args) {
      const questionnaireId = args.id;
      const q = args.question;

      const sent = {
        enonce: q.enonce.trim(),
        reponse: q.reponse.trim()
      };
      if (q.proposition_a?.trim()) sent.proposition_a = q.proposition_a.trim();
      if (q.proposition_b?.trim()) sent.proposition_b = q.proposition_b.trim();

      fetch(`http://localhost:5000/quiz/api/v1.0/questionnaires/${questionnaireId}/questions`, {
        headers: { "Content-Type": "application/json" },
        method: "POST",
        body: JSON.stringify(sent)
      })
        .then(result => result.json())
        .then(result => {
          const newQuestion = result.question;

          const questionnaire = this.getQuestionnaireById(questionnaireId);

          if (questionnaire) {
            if (!questionnaire.questions) questionnaire.questions = [];
            questionnaire.questions.push(newQuestion);
          }
        })
        .catch(console.error);
    },
    supprimerQuestion(args) {
      let questionUri = args.uri;
      if (questionUri.startsWith('/quiz')) {
        questionUri = 'http://localhost:5000' + questionUri;
      }

      fetch(questionUri, { method: "DELETE", headers: { "Content-Type": "application/json" } })
        .then(result => {
          if (result.ok) {
            this.questionnaires.forEach(questionnaire => {
              if (questionnaire.questions) {
                const index = questionnaire.questions.findIndex(q => q.uri === args.uri);
                if (index !== -1) questionnaire.questions.splice(index, 1);
              }
            });
          }
        })
        .catch(console.error);
    },
    getQuestionnaireById(id) {
      return this.questionnaires.find(q => {
        const uriMatch = q.uri ? q.uri.match(/questionnaires\/(\d+)/) : null;
        const uriId = uriMatch ? parseInt(uriMatch[1]) : null;
        return uriId === id;
      })
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
