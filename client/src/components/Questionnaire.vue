<script>
import CreationQuestion from "./CreationQuestion.vue";

export default {
  components: { CreationQuestion },
  props: {
    questionnaire: Object
  },
  data() {
    return {
      nomQuestionnaire: "",
      showQuestions: false
    };
  },
  methods: {
    supprimerQuestionnaire() {
      this.$emit("supprimerQuestionnaire", { uri: this.questionnaire.uri });
    },
    modifierQuestionnaire() {
      this.$emit("modifierQuestionnaire", {
        uri: this.questionnaire.uri,
        nomQuestionnaire: this.nomQuestionnaire
      });
    },
    addQuestion(args) {
      this.$emit("ajouterQuestion", args);
    },
    supprimerQuestion(question) {
      this.$emit("supprimerQuestion", { uri: question.uri });
    }
  },
  emits: [
    "supprimerQuestionnaire",
    "modifierQuestionnaire",
    "ajouterQuestion",
    "supprimerQuestion"
  ]
};
</script>

<template>
  <li>
    <span>
      {{ questionnaire.name }}
      <button
        class="btn btn-default"
        type="button"
        @click="showQuestions = !showQuestions"
      >
        Questions
      </button>
    </span>

    <div class="input-group">
      <input
        placeholder="Modifier le nom du questionnaire"
        type="text"
        class="form-control"
        v-model="nomQuestionnaire"
      />
      <span class="input-group-btn">
        <button
          class="btn btn-default"
          type="button"
          @click="modifierQuestionnaire"
        >
          Modifier
        </button>
      </span>
    </div>

    <input
      type="button"
      class="btn btn-danger"
      value="Supprimer"
      @click="supprimerQuestionnaire"
    />

    <div v-if="showQuestions" class="mt-3">
      <h4>Questions</h4>

      <ul
        v-if="
          Array.isArray(questionnaire.questions) &&
          questionnaire.questions.length
        "
      >
        <li
          v-for="(question, index) in questionnaire.questions"
          :key="question?.id ?? index"
          v-if="question"
        >
          {{ question.enonce }}
          <button
            class="btn btn-danger btn-sm"
            type="button"
            @click="supprimerQuestion(question)"
          >
            Supprimer
          </button>
        </li>
      </ul>

      <p v-else>Aucune question pour l’instant.</p>

      <CreationQuestion
        :questionnaire-id="questionnaire.id"
        @add="addQuestion"
      />
    </div>
  </li>
</template>
