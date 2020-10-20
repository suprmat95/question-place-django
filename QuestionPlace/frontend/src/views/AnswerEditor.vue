<template>
    <div class="container mt-2">
        <div class="row">
            <div class="col-12">
                <h1 class="mb-3">Modifica la tua risposta</h1>
                <form @submit.prevent="onSubmit">
                    <textarea v-model="answerBody"
                              class="form-control"
                              rows="3"></textarea>
                    <br>
                    <button
                        class="btn btn-success"
                        type="submit"
                    >Pubblica Risposta
                    </button>
                </form>
                <p class="error mt-2">{{error}}</p>
            </div>
        </div>
    </div>

</template>

<script>
    import {apiService} from "../common/api.service";

    export default {
        name: "AnswerEditor",
        props: {
            id: {
                type: Number,
                required: true
            },
            answerEdit: {
                type: String,
                required: true
            },
            question_slug: {
                type: String,
                required: true
            }
        },
        async beforeRouteEnter(to, from, next) {
            let endpoint =`/api/answers/${to.params.id}/`;
            await apiService(endpoint)
                    .then(data =>{
                        to.params.answerEdit = data.body;
                        to.params.question_slug = data.question_slug;
                    })
            return next();
            },
        data() {
            return {
                answerBody: this.answerEdit,
                error: null
            }
        },
        methods: {
            onSubmit() {
                if (this.answerBody) {
                    let endpoint = `/api/answers/${this.id}/`;
                    apiService(endpoint, "PUT", {body: this.answerBody})
                        .then(()=> {
                            this.$router.push({
                                name: "question",
                                params: {slug: this.question_slug}
                            })
                        })

                } else {
                    this.error = "Il campo non puo essere vuoto";
                }
            }
        }
    //    methods: {
    //        async getAnswerData() {
    //            let endpoint =`/api/answers/${this.id}/`;
    //            await apiService(endpoint)
    //                .then(data =>{
    //                    this.answerBody = data.body;
    //                })
    //        }
    //    },
    //    created() {
    //        this.getAnswerData();
    //    }
    }
</script>

<style lang="css">

</style>