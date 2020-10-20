<template lang="html">
    <div class="single-answe">
        <p class="text-muted">
            <strong>{{answer.author}}</strong> ha risposto il {{answer.created_at}}
        </p>
        <p>{{answer.body}}</p>
    </div>
</template>

<script>
    export default {
        name: "AnswerComponent",
        props: {
            answer: {
                type: Object,
                required: true
            }
        }
    }
</script>

<style scoped>

</style>