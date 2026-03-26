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
        enonce: q.enonce.trim(),      // Trim pour éviter les espaces
        reponse: q.reponse.trim()
      };

      // ✅ NE PAS envoyer les props vides
      if (q.proposition_a && q.proposition_a.trim()) {
        sent.proposition_a = q.proposition_a.trim();
      }
      if (q.proposition_b && q.proposition_b.trim()) {
        sent.proposition_b = q.proposition_b.trim();
      }

      console.log("📤 Données nettoyées :", sent);

      // ✅ DEBUG : affiche EXACTEMENT ce qui est envoyé
      console.log("📤 Données envoyées à l'API :", JSON.stringify(sent, null, 2));

      fetch(
        `http://localhost:5000/quiz/api/v1.0/questionnaires/${questionnaireId}/questions`,
        {
          headers: { "Content-Type": "application/json" },
          method: "POST",
          body: JSON.stringify(sent)
        }
      )
        .then(result => {
          console.log("📥 Status HTTP :", result.status, result.statusText);
          return result.json();
        })
        .then(result => {
          console.log("API retourne :", result);

          let newQuestion = result.question || result;

          // ✅ CORRECTION : ton API n'a pas "error" ni "id", mais "uri" !
          if (newQuestion.error) {
            console.error("❌ Erreur API :", newQuestion);
            return;
          }

          const questionnaire = this.questionnaires.find(qq => qq.id == questionnaireId);
          if (questionnaire) {
            if (!questionnaire.questions) questionnaire.questions = [];
            questionnaire.questions.push(newQuestion);
          }
        })
        .catch(error => console.error("Erreur fetch :", error));
    },
    supprimerQuestion(args) {
      let questionUri = args.uri;

      // ✅ CORRECTION : Si l'URI est relatif, ajouter le domaine
      if (questionUri.startsWith('/quiz')) {
        questionUri = 'http://localhost:5000' + questionUri;
      }

      console.log("🗑️ Supprimant :", questionUri);

      fetch(questionUri, {
        headers: { "Content-Type": "application/json" },
        method: "DELETE"
      })
        .then(result => {
          console.log("📥 DELETE status :", result.status);
          if (result.ok) {  // 200 ou 204
            this.questionnaires.forEach(questionnaire => {
              if (!questionnaire.questions) return;
              const index = questionnaire.questions.findIndex(
                question => question.uri === args.uri  // Utilise l'ancien uri relatif
              );
              if (index !== -1) {
                questionnaire.questions.splice(index, 1);
              }
            });
          } else {
            console.error(`❌ Échec suppression ${result.status} :`, questionUri);
          }
        })
        .catch(error => console.error("Erreur DELETE :", error));
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
