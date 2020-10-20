<template lang="html">
    <div class="single-question mt-2">
        <div class="container">
            <h1>{{ question.content }}</h1>
            <p class="mb-0"> Domanda aggiunta da:
                <span class="author-name">{{ question.author }}</span>
            </p>
            <p>{{ question.created_at }}</p>
            <hr>
            <template v-if="userHasAnswered">
                <p class="answer-added">Hai risposto a questa domanda.</p>
            </template>
            <template v-else-if="showForm">
                <form class="card" @submit.prevent="onSubmit">
                    <div class="card-header px-3">
                        Aggiungi una risposta alla domanda
                    </div>
                    <div class="card-block">
                        <textarea
                                v-model="newAnswerBody"
                                class="form-control"
                                placeholder="Aggiungi una risposta alla domanda"
                                rows="5"
                                ></textarea>
                    </div>
                    <div class="card-footer px-3">
                        <button type="submit" class="btn btn-sm btn-success">Aggiungi risposta</button>
                    </div>
                </form>
                <p class="error mt-2">{{error}}</p>
            </template>
            <template v-else>
                <button
                        class="btn btn-sm btn-success"
                        @click="showForm=true"
                        >Rispondi alla Domanda</button>
            </template>
            <hr>
            <AnswerComponent
                v-for="(answer, index) in answers"
                :answer="answer"
                :key="index"/>
            <div class="my-4">
                <p v-show="loadingAnswers">...loading...</p>
                <button
                    v-show="next"
                    @click="getQuestionAnswers"
                    class="btn btn-sm btn-outline-succes"> Carica Ancora

                </button>
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
                answers: [],
                userHasAnswered: false,
                showForm: false,
                newAnswerBody: null,
                error: null,
                next: null
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
                    this.userHasAnswered = data.user_has_answered;
                    this.setPageTitle(data.content)
                })
            },
            getQuestionAnswers() {
                let endpoint = `/api/questions/${this.slug}/answers/`
                if (this.next) {
                    endpoint = this.next;
                }
                this.loadingAnswers = true;
                apiService(endpoint)
                .then(data => {
                    this.answers.push(...data.results);
                    this.loadingAnswers = false;
                    if (data.next) {
                        this.next = data.next;
                    } else {
                        this.next = null;
                    }
                })

            },
            onSubmit() {
                if(this.newAnswerBody){
                    let endpoint = `/api/questions/${this.slug}/answer/`;
                    apiService(endpoint, "POST", {body: this.newAnswerBody})
                        .then(data => {
                            this.answers.unshift(data);
                        })
                    this.newAnswerBody = null;
                    this.showForm = false;
                    this.userHasAnswered = true;
                    if(this.error) {
                        this.error = null
                    }
                }
                else {
                    this.error = "Il campo non puo essere vuoto."
                }
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
.error {
    color: red;
    font-weight: bold;
}
.answer-added {
    color: green;
    font-weight: bold;
}
</style>