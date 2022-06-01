<script>
import styles from './NavLink.module.css';

export default {
    props: {
        to: String,
        text: String,
        active: Boolean,
    },
    data() {
        return {
            styles,
        };
    },
};
</script>

<template>
    <router-link :class="[active ? styles.active : styles.link]" :to="to">{{text}}</router-link>
</template>
