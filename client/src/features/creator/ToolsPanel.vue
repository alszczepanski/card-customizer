<template>
    <div :class="styles.toolsPanel">
        <h1>Tools Panel</h1>
        <DraggableNode :item="{ type: 'photo' }" />
        <DraggableNode :item="{ type: 'text' }" />

        <label for="colorInput" class="form-label">Kolor wizytówki</label>
        <input type="color" class="form-control form-control-color" id="colorInput" value="#ffffff"
            @change="handleSetColor" />
    </div>
</template>


<script setup>
import { DraggableNode } from "./draggable"
import useCardCreator from "./store/useCardCreator";

import styles from "./ToolsPanel.module.css";

const { setCardColor } = useCardCreator();

const handleSetColor = (event) => setCardColor(event.target.value);
</script>