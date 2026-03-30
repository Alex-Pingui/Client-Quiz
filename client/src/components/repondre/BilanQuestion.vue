<script>
export default {
  props: {
    question: Object
  }
}
</script>

<template>
  <li>
    <h3>{{question['enonce']}}</h3>
    <p :class="question['correct']?'bonne-reponse':'mauvaise-reponse'">Réponse entrée: {{question['reponse']}}</p>
    <p v-if="question['correct']" class="bonne-reponse">Bonne réponse</p>
    <p v-else class="mauvaise-reponse">Mauvaise réponse</p>
  </li>
</template>

<style scoped>
.bonne-reponse{
  color: #3A7734;
}

.mauvaise-reponse{
  color: #9C1A1C;
}
</style>