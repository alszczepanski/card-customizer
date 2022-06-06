<script>
import LContent from "./LContent.vue";
import LToolbar from "./LToolbar.vue";
import LNavigation from "./LNavigation.vue";
import styles from "./AuthorizedLayout.module.css";
import UserInfo from "./UserInfo.vue";

export default {
  components: { LContent, LToolbar, LNavigation, UserInfo },
  data: () => {
    return {
      styles,
    };
  },
};
</script>

<template>
  <div :class="styles.layout">
    <LToolbar><h1>Kreator wizytówek</h1> <UserInfo /></LToolbar>
    <div :class="styles.mainContent">
      <LNavigation :class="styles.sider">Sider</LNavigation>
      <LContent :class="styles.content">
        <slot />
      </LContent>
    </div>
  </div>
</template>
