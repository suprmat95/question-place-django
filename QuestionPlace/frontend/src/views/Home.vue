<template>
    <div class="home-view">
        <div class="container">
            <div class="mt-2">
                <div v-for = "question in questions"
                :key = "question.pk">
                    <p class="mb-0"> Domanda aggiunta da
                        <span class="author-name">{{ question.author }}</span>
                    </p>
                    <h2> {{ question.content }}</h2>
                    <p>Risposte: {{question.answers_count}}</p>
                    <hr>
                </div>
            </div>
        homepage
        </div>
    </div>
</template>

<script>
    import {apiService} from "../common/api.service";

    export default {
        name: "Home",

        data() {
            return {
                questions: []
            }
        },
        methods: {
            getQuestions() {
                let endpoint = "api/questions/";
                apiService(endpoint)
                    .then(data => {
                        this.questions.push(...data.results)
                    })
            }
        },

        created() {
            this.getQuestions()
        }

    };
</script>
<style>
    .author-name{
        font-weight: bold;
        color: #DC3545;
    }
</style>