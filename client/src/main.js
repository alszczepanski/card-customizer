import { createApp } from "vue";
import { createPinia } from "pinia";

import "element-plus/dist/index.css";

import App from "./App.vue";
import router from "./navigation";

createApp(App).use(router).use(createPinia()).mount("#app");
