import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";
import bootstrap from "bootstrap/dist/js/bootstrap.bundle";

import "bootstrap/dist/css/bootstrap.css";

createApp(App).use(store).use(router, axios, bootstrap).mount("#app");
