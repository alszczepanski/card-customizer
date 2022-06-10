<template>
    <CreatorLayout>
        <div :class="styles.upper">
            <CardDropzone :class="styles.left" />
            <ToolsPanel :class="styles.right" />
        </div>
        <ItemsToolbox />
    </CreatorLayout>
</template>

<script setup>
    import CreatorLayout from './CreatorLayout.vue';
    import CardDropzone from './CardDropzone.vue';
    import ToolsPanel from './ToolsPanel.vue';
    import { ItemsToolbox } from './itemsToolbox';
    
    import styles from './CardCreator.module.css';
</script> 