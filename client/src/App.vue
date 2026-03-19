<script>
const API_URL = "http://localhost:5000/quiz/api/v1.0";
import CreationQuestion from './components/CreationQuestion.vue';

export default {
  data() {
    return {
      title: "Quiz",
      questionnaires: [],
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
    }
  },
  components: { CreationQuestion }
}
</script>

<template>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"
    integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
  <div class="container">
    <h2>{{ title }}</h2>
    <ol>
      <li v-for="questionnaire in questionnaires">
        {{ questionnaire.name }}
        <div>
          <ol>
          <li v-for="question in questionnaire.questions" :key="question.id" :question="question"
            @getAll="fetchData" @remove="fetchData" @modify="fetchData">
            {{ question.enonce }}
          </li>
          </ol>
        </div>
      </li>
    </ol>
    <div class="input-group">
      <input v-model="newItem" @keyup.enter="addItem" placeholder="Ajouter un questionnaire" type="text"
        class="form-control">
      <span class="input-group-btn">
        <button @click="addItem" class="btn btn-default" type="button">Ajouter</button>
      </span>
    </div>
  </div>
</template>
