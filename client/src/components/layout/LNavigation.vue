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
        watch(route, ({ path }) => {
            activeRoute.value = path;
        }, { immediate: true, deep: true })
        return { activeRoute }
    },
};
</script>

<template>
    <div :class="styles.navigation">
        <el-row>
            <el-col>
                <el-menu @open="handleOpen" @close="handleClose">
                    <el-menu-item index="1">
                        <NavLink to="/" text="Strona startowa" :active="activeRoute === '/'" />
                    </el-menu-item>
                    <el-menu-item index="2">
                        <NavLink to="/your-cards" text="Twoje wizytówki" :active="activeRoute === '/your-cards'" />
                    </el-menu-item>
                    <el-menu-item index="3">
                        <NavLink to="/creator" text="Stwórz wizytówkę" :active="activeRoute === '/creator'" />
                    </el-menu-item>
                </el-menu>
            </el-col>
        </el-row>
    </div>
</template>
