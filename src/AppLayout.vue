<template>
    <component :is="layout">
        <slot />
    </component>
</template>

<script>
import { useRoute } from "vue-router";
import { ref, watch } from "vue";

import { AuthorizedLayout, AnonymousLayout } from "./components/layout";

export default {
    name: "AppLayout",
    setup() {
        const layout = ref(AnonymousLayout);
        const route = useRoute();

        watch(
            () => route.meta,
            async (meta) => {
                try {
                    layout.value = meta.layout === 'authorized' ? AuthorizedLayout : AnonymousLayout
                } catch (e) {
                    layout.value = AnonymousLayout;
                }
            },
            { immediate: true }
        );
        return { layout };
    },
};
</script>
