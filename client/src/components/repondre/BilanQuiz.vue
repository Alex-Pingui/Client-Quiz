<script>
import BilanQuestion from "./BilanQuestion.vue";

export default {
  components: {BilanQuestion},
  props:{
    scoreObtenu: Number,
    scoreMax: Number,
    questions: Array
  }
}
</script>

<template>
  <h2>Bilan du quiz</h2>
  <p>Score obtenu: {{scoreObtenu}} / {{scoreMax}}</p>
  <h3>Détails</h3>
  <ul>
    <BilanQuestion v-for="question in questions" :question="question"/>
  </ul>
</template>

<style scoped>

</style>