<script>
export default {
  props:{
    scoreObtenu: Number,
    scoreMax: Number
  }
}
</script>

<template>
  <h2>Bilan du quiz</h2>
  <p>Score obtenu: {{scoreObtenu}} / {{scoreMax}}</p>
</template>

<style scoped>

</style>