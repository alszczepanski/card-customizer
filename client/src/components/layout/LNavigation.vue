<script>
import { ref, watch } from "vue";
import { useRoute } from "vue-router";

import { NavLink } from "../link";

import styles from "./LNavigation.module.css";

export default {
  components: { NavLink },
  data() {
    return {
      styles,
    };
  },
  setup() {
    const activeRoute = ref("");
    const route = useRoute();
    watch(
      route,
      ({ path }) => {
        activeRoute.value = path;
      },
      { immediate: true, deep: true }
    );
    return { activeRoute };
  },
};
</script>

<template>
  <div>
    <ul class="nav flex-column">
      <NavLink to="/" text="Strona startowa" :active="activeRoute === '/'" />
      <NavLink to="/your-cards" text="Twoje wizytówki" :active="activeRoute === '/your-cards'" />
       <NavLink to="/creator" text="Stwórz wizytówkę" :active="activeRoute === '/creator'" />
    </ul>
  </div>
</template>
