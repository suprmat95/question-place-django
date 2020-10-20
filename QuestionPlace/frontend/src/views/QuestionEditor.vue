<template lang="html">
    <div class="container mt-2">
        <div class="row">
            <div class="col-12">
                <h1 class="mb-3">Aggiungi una domanda</h1>
                <form @submit.prevent="onSubmit">
                    <textarea v-model="questionBody"
                              class="form-control"
                              placeholder="Cosa vuoi chiedere?"
                              rows="3"></textarea>
                    <br>
                    <button
                        class="btn btn-success"
                        type="submit"
                    >Pubblica Domanda
                    </button>
                </form>
                <p class="muted error mt-2">{{error}}</p>
            </div>
        </div>
    </div>
    
</template>

<script>
    import {apiService} from "../common/api.service";

    export default {
        name: "QuestionEditor",

        data() {
            return {
                questionBody: null,
                error: null
            }
        },

        methods:{
            onSubmit() {
                if(!this.questionBody){
                    this.error = "Il campo non puo essere vuoto."
                }
                else if (this.questionBody.length> 240){
                    this.error = "Non superare i 240 caratteri."
                }
                else {
                    let endpoint = "/api/questions/";
                    let method = "POST";
                    apiService(endpoint, method, {content: this.questionBody})
                        .then(question_data => {
                            this.$router.push({
                                name: "question",
                                params: { slug: question_data.slug }
                            });
                        });
                }
            }
        },
        created() {
            document.title = "Editor - QuestionPlace"
        }
    }
</script>

<style scoped>

</style>