<script>
export default {
    props: {
        question: Object,
        required: true
    },
    methods: {
        getAll() {
            this.$emit('getAll');
        },
        supprimer() {
            this.$emit('remove',{id: this.question.id });
        },
        modifier() {
            this.$emit('modify', this.question.id);
        }
    },
    emits: ["remove", "modify"]
}
</script>

<template>
    <div></div>
</template>