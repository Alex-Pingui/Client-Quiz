<script>
export default {
  props: {
    questionnaire: Object
  },
  methods: {
    getQuestions(){
      this.$emit("getQuestions", {uri:this.questionnaire.uri})
    }
  }
}
</script>

<template>
  <li>
    <span>
      {{questionnaire.name}}
      <button
          class="btn btn-default"
          @click="getQuestions"
      >
        Questions
      </button>
    </span>
  </li>
</template>

<style scoped>

</style>