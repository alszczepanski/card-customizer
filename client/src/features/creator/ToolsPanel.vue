<template>
    <div :class="styles.toolsPanel">
        <h1>Tools Panel</h1>
        <div :class="styles.draggable" draggable="true" @dragstart="onDragStart">To be dragged
        </div>
    </div>
</template>


<script setup>
import styles from "./ToolsPanel.module.css";
const onDragStart = (event) => {
    const { clientWidth: width, clientHeight: height } = event.currentTarget
    event.dataTransfer.dropEffect = "move"
    event.dataTransfer.setData("currentTarget", JSON.stringify({ width, height}))
}
</script>