<script setup>
import { useRouter } from "vue-router";
import { setItem } from "@/services/localstorage";
import useAuthStore from "@/stores/authStore";
import styles from './UserInfo.module.css';

const router = useRouter();

const { user, setUser } = useAuthStore();
const handlelogout = () => {
    setItem('cards-auth-token', null)
    setUser(null);
    router.replace("/login");
}
</script>

<template>
  <div :class="styles.container">
    <div>
        Zalogowano jako: {{ user?.username }}
    </div>
    <button class="btn btn-light" @click="handlelogout">Wyloguj się</button>
  </div>
</template>
