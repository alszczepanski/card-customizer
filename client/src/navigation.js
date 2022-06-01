import { createRouter, createWebHistory } from 'vue-router'
import { BusinessCards, CreateBusinessCard, HomePage, LoginPage } from "./pages";

export const routes = [
    {
        path: "/login",
        component: LoginPage,
        meta: {
            layout: "anonymous",
        },
    },
    {
        path: "/",
        component: HomePage,
        meta: {
            layout: "authorized",
        },
    },
    {
        path: "/your-cards",
        component: BusinessCards,
        meta: {
            layout: "authorized",
        },
    },
    {
        path: "/creator",
        component: CreateBusinessCard,
        meta: {
            layout: "authorized",
        },
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
