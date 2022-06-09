import { createRouter, createWebHistory } from "vue-router";
import useAuthStore from "./stores/authStore";
import {
  BusinessCards,
  CreateBusinessCard,
  HomePage,
  LoginPage,
  RegisterPage
} from "./pages";

export const routes = [
  {
    path: "/login",
    component: LoginPage,
    meta: {
      layout: "anonymous",
    },
  },
  {
    path: "/register",
    component: RegisterPage,
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

router.beforeEach(async (to) => {
    console.log(to.path)
  const authRequired = !["/login", "/register"].includes(to.path);
  const auth = useAuthStore();

  if (authRequired && !auth.user) {
    return "/login";
  }
});

export default router;
