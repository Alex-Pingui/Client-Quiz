<script>
const API_URL = "http://localhost:5000/quiz/api/v1.0";
import CreationQuestion from './components/CreationQuestion.vue';

export default {
  data() {
    return {
      title: "Quiz",
      questionnaires: [],
      newItem: "",
      newQuestion: {
        enonce: "",
        reponse: "",
        proposition_a: "",
        proposition_b: ""
      }
    }
  },
  async mounted() {
    await this.fetchData();
  },
  methods: {
    async fetchData() {
      try {
        const response = await fetch(`${API_URL}/questionnaires`, {
          method: "GET",
          headers: { "Content-Type": "application/json" }
        });
        if (!response.ok) throw new Error(`Erreur HTTP : ${response.status}`);
        const data = await response.json();
        this.questionnaires = await Promise.all(
          data.questionnaires.map(async (questionnaire) => {
            const questionResult = await fetch(`${API_URL}/questionnaires/${questionnaire.id}/questions`);
            const questionData = await questionResult.json();
            console.log(`Questions pour le questionnaire ${questionnaire.id} :`, questionData);
            return { ...questionnaire, questions: questionData.questions };
          })
        );
      } catch (error) {
        console.error("Erreur lors du chargement :", error.message);
      }
    },
    async addItem() {
      if (!this.newItem.trim()) return;
      try {
        const response = await fetch(API_URL, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ name: this.newItem })
        });
        if (!response.ok) throw new Error(`Erreur HTTP : ${response.status}`);
        this.newItem = "";
        await this.fetchData();
      } catch (error) {
        console.error("Erreur lors de l'ajout :", error.message);
      }
    },
    async addQuestion(questionnaireId, enonce, reponse, proposition_a = null, proposition_b = null) {
      try {
        const body = { enonce, reponse };
        if (proposition_a && proposition_b) {
          body.proposition_a = proposition_a;
          body.proposition_b = proposition_b;
        }
        const response = await fetch(`${API_URL}/questionnaires/${questionnaireId}/questions`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(body)
        });
        if (!response.ok) throw new Error(`Erreur HTTP : ${response.status}`);
        const data = await response.json();
        return data.question;
      } catch (error) {
        console.error("Erreur lors de l'ajout de la question :", error.message);
      }
    },
    async submitQuestion(questionnaireId) {
      if (!this.newQuestion.enonce.trim() || !this.newQuestion.reponse.trim()) return;
      await this.addQuestion(
        questionnaireId,
        this.newQuestion.enonce,
        this.newQuestion.reponse,
        this.newQuestion.proposition_a || null,
        this.newQuestion.proposition_b || null
      );
      this.newQuestion = { enonce: "", reponse: "", proposition_a: "", proposition_b: "" };
      await this.fetchData();
    }
  },
  components: { CreationQuestion }
}
</script>

<template>
  <div class="container">
    <h2>{{ title }}</h2>
    <ol>
      <li v-for="questionnaire in questionnaires" :key="questionnaire.id">
        {{ questionnaire.name }}
        <div>
          <CreationQuestion v-for="question in questionnaire.questions" :key="question.num_question"
            :question="question" @getAll="fetchData" @remove="fetchData" @modify="fetchData" />
        </div>

      </li>
    </ol>
  </div>
  <div class="input-group">
    <input v-model="newItem" @keyup.enter="addItem" placeholder="Ajouter un questionnaire" type="text"
      class="form-control">
    <span class="input-group-btn">
      <button @click="addItem" class="btn btn-default" type="button">Ajouter</button>
    </span>
  </div>
</template>
