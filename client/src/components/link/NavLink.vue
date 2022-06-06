<script>
export default {
  props: {
    to: String,
    text: String,
    active: Boolean,
  },
};
</script>

<template>
  <li class="nav-item">
    <router-link
      class="nav-link"
      :class="active ? 'active': 'text-secondary'"
      :to="to"
      >{{ text }}</router-link
    >
  </li>
</template>
