<template lang="html">
    <div class="single-question mt-2">
        <div class="container">
            <h1>{{ question.content }}</h1>
            <p class="mb-0"> Domanda aggiunta da:
                <span class="author-name">{{ question.author }}</span>
            </p>
            <p>{{ question.created_at }}</p>
            <hr>
            <AnswerComponent
                v-for="(answer, index) in answers"
                :answer="answer"
                :key="index"/>
            <div class="my-4">
                <p v-show="loadingAnswers">...loading...</p>
            </div>
        </div>
    </div>
</template>

<script>
    import {apiService} from "../common/api.service";
    import AnswerComponent from "../components/Answer";
    export default {
        name: "Question",

        props: {
            slug: {
                type: String,
                required: true
            }
        },
        components: {
            AnswerComponent
        },
        data() {
            return {
                question: {},
                loadingAnswers: false,
                answers: []
            }
        },

        methods: {
            setPageTitle(title) {
                document.title = title;
            },
            getQuestionData() {
                let endpoint = `/api/questions/${this.slug}/`
                apiService(endpoint)
                .then(data =>{
                    this.question = data;
                    this.setPageTitle(data.content)
                })
            },
            getQuestionAnswers() {
                let endpoint = `/api/questions/${this.slug}/answers/`
                this.loadingAnswers = true;
                apiService(endpoint)
                .then(data => {
                    this.answers = data.results;
                    this.loadingAnswers = false;
                })

            }
        },
        created() {
            this.getQuestionData();
            this.getQuestionAnswers();
        }
    }
</script>

<style scoped>
.single-question {
    text-align: left;
}
</style>