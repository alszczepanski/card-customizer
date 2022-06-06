<script setup>
import { useRouter } from "vue-router";

import useAuthStore from "@/stores/authStore";
import styles from './UserInfo.module.css';

const router = useRouter();

const { user, logout } = useAuthStore();
const handlelogout = () => {
    logout();
    router.replace("/login");
}
</script>

<template>
  <div :class="styles.container">
    <div>
        Zalogowano jako: {{ user.username }}
    </div>
    <button class="btn btn-light" @click="handlelogout">Wyloguj się</button>
  </div>
</template>
