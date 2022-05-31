<script>

import LContent from './LContent.vue';
import LToolbar from './LToolbar.vue';
import LNavigation from './LNavigation.vue';
import styles from './AuthorizedLayout.module.css';

export default {
    components: { LContent, LToolbar, LNavigation },
    data() {
        return {
            styles,
        };
    },
};
</script>

<template>
    <div :class="styles.layout">
        <LToolbar><h1>Kreator wizytówek</h1></LToolbar>
        <div :class="styles.mainContent">
            <LNavigation :class="styles.sider">Sider</LNavigation>
            <LContent :class="styles.content">
                <slot />
            </LContent>
        </div>
    </div>
</template>
