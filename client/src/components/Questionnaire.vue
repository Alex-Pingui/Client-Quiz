<script>
export default {
  props: {
    questionnaire: Object
  }
}
</script>

<template>
  <li>
    <span>
      {{questionnaire.name}}
      <button class="btn btn-default">Questions</button>
    </span>
    <div class="input-group">
      <input placeholder="Modifier le nom du questionnaire"
             type="text"
             class="form-control">
      <span class="input-group-btn">
      <button class="btn btn-default"
              type="button">Modifier
      </button>
    </span>
    </div>
    <input type="button"
           class="btn btn-danger"
           value="Supprimer">
  </li>
</template>

<style scoped>

</style>