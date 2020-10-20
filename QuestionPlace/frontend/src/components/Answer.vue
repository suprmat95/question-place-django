<template lang="html">
    <div class="single-answer">
        <p class="text-muted">
            <strong>{{answer.author}}</strong> ha risposto il {{answer.created_at}}
        </p>
        <p>{{answer.body}}</p>
        <div v-if="isAnswerAuthor()" class="answer-owner">
            <button
                    class="btn btn-sm btn-outline-secondary mr-1">Modifica</button>
            <button class="btn btn-sm btn-outline-danger">Cancella</button>

        </div>
    </div>

</template>

<script>
    export default {
        name: "AnswerComponent",
        props: {
            answer: {
                type: Object,
                required: true
            },
            requestUser: {
                type: String,
                required: true
            }
        },
        methods: {
            isAnswerAuthor() {
                return this.answer.author === this.requestUser;
            }
        }
    }
</script>

<style scoped>

</style>