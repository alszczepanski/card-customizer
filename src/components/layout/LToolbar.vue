<script>
import styles from './LToolbar.module.css';
export default {
    data() {
        return {
            styles,
        };
    },
};
</script>

<template>
    <div :class="styles.toolbar">
        <slot />
    </div>
</template>
