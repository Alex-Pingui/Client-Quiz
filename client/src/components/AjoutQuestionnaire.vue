<script>
export default {
  data(){
    return {
      nomQuestionnaire: ""
    };
  },
  methods:{
    ajouterQuestionnaire(){
      this.$emit('ajouterQuestionnaire',{nomQuestionnaire: this.nomQuestionnaire});
    }
  }
};
</script>

<template>
  <div class="input-group">
    <input placeholder="Entrer le nom du questionnaire"
           type="text"
           class="form-control"
           v-model="nomQuestionnaire"
    >
    <span class="input-group-btn">
      <button class="btn btn-default"
              type="button"
              @click="ajouterQuestionnaire"
      >
        Ajouter
      </button>
    </span>
  </div>
</template>

<style scoped>
</style>