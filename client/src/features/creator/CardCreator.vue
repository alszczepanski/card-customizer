<template>
    <CreatorLayout>
        <CardDropzone :class="styles.left" />
        <ToolsPanel :class="styles.right" />
    </CreatorLayout>
</template>

<script setup>
    import CreatorLayout from './CreatorLayout.vue';
    import CardDropzone from './CardDropzone.vue';
    import ToolsPanel from './ToolsPanel.vue';
    import styles from './CardCreator.module.css';
</script> 