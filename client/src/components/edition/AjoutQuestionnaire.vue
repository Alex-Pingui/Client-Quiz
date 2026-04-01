<script>
export default {
  data(){
    return {
      nomQuestionnaire: ""
    };
  },
  methods:{
    ajouterQuestionnaire(){
      if(this.nomQuestionnaire.length===0){
        alert("Veuillez renseigner un nom de questionnaire pour pouvoir ajouter un nouveau questionnaire");
        return;
      }

      this.$emit('ajouterQuestionnaire',{nomQuestionnaire: this.nomQuestionnaire});
      this.nomQuestionnaire="";
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
