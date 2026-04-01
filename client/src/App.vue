<script>
export default {
  data(){
    return {
      title: "Quiz"
    };
  },
};
</script>

<template>
  <h1>{{title}}</h1>
  <nav>
    <RouterLink :to="{ name: 'home' }">Accueil</RouterLink>
    <RouterLink to="edition">Édition</RouterLink>
    <RouterLink to="reponse">Répondre</RouterLink>
  </nav>
  <RouterView />
</template>

<style scoped>
</style>
