<template>
    <div :class="styles.toolsPanel">
        <h1>Narzędzia</h1>

        <h6>Przeciągnij zdjęcie wizytówki</h6>
        <DraggableNode :item="{ type: 'photo' }" />

        <h6>Przeciągnij tekst wizytówki</h6>
        <DraggableNode :item="{ type: 'text' }" />

        <div :class="styles.colorPicker">
            <label for="colorInput" class="form-label">Ustaw kolor wizytówki</label>
            <input type="color" class="form-control form-control-color" id="colorInput" value="#ffffff"
                @change="handleSetColor" />
        </div>
    </div>
</template>


<script setup>
import { DraggableNode } from "./draggable"
import useCardCreator from "./store/useCardCreator";

import styles from "./ToolsPanel.module.css";

const { setCardColor } = useCardCreator();

const handleSetColor = (event) => setCardColor(event.target.value);
</script>