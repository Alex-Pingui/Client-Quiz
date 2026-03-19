<script>
export default {
  props: {
    question: {
      type: Object,
      required: true
    }
  },
  methods: {
    ajouter() {
      this.$emit('add', { id: this.question.id });
    },
    supprimer() {
      this.$emit('remove', { id: this.question.id });
    },
    modifier() {
      this.$emit('modify', { id: this.question.id });
    }
  },
  emits: ["add", "remove", "modify"]
}
</script>

<template>
    <div class="text">
        <label>
            {{ question.enonce }}
        </label>
        <!-- <input type="button" class="btn btn-warning" value="Modifier" @click="modifier">
        <input type="button" class="btn btn-danger" value="Supprimer" @click="supprimer"> -->
    </div>
</template>