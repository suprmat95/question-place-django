import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue"
import Question from "./views/Question.vue";
import QuestionEditor from "./views/QuestionEditor";
import AnswerEditor from "./views/AnswerEditor";

Vue.use(Router);

export default new Router({
    mode: "history",
    routes: [
        {
            path: "/",
            name: "home",
            component: Home
        },
        {
            path: "/question/:slug",
            name: "question",
            component: Question,
            props: true
        },
        {
            path: "/answer/:id",
            name: "answer-editor",
            component: AnswerEditor,
            props: true
        },
        {
            path: "/ask/:slug?",
            name: "question-editor",
            component: QuestionEditor,
            props: true
        },

    ]
});