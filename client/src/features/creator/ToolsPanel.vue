<template>
    <div :class="styles.toolsPanel">
        <h1>Tools Panel</h1>
<DraggableNode type="photo" />
        <DraggableNode type="text" />
    </div>
</template>


<script setup>
import { DraggableNode } from "./draggable"
import styles from "./ToolsPanel.module.css";
</script>