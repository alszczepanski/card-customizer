<script>
import styles from './LContent.module.css';
export default {
    data() {
        return {
            styles,
        };
    },
};
</script>

<template>
    <div :class="styles.content">
        <slot />
    </div>
</template>
