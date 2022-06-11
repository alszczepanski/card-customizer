import { createRouter, createWebHistory } from "vue-router";

import useAuthStore from "@/stores/authStore";
import { restoreUser } from "@/services/auth";

import {
  BusinessCards,
  CreateBusinessCard,
  HomePage,
  LoginPage,
  RegisterPage,
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

router.beforeEach(async (to, from) => {
  const authRequired = !["/login", "/register"].includes(to.path);
  const auth = useAuthStore();

  return await restoreUser()
    .then(({ data }) => auth.setUser(data))
    .then(() => {
      if (!authRequired) return from.path;
    })
    .catch(() => {
      if (authRequired) {
        return "/login";
      }
    });
});

export default router;
