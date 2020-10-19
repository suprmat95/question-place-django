import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue"
import Esempio from "./views/Esempio";
import About from "./views/About";

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
            path: "/about",
            name: "about",
            component: About
        },
        {
            path: "/esempio",
            name: "esempio",
            component: Esempio
        }
    ]
});