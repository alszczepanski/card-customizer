<script>
import LContent from './LContent.vue';
import styles from './AnonymousLayout.module.css';

export default {
    components: { LContent },
    data() {
        return {
            styles,
        };
    },
};
</script>

<template>


    <LContent :class="styles.content">
        <slot />
    </LContent>


</template>
