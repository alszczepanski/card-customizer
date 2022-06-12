<template>
    <div :class="styles.toolsPanel">
        <h1>Narzędzia</h1>
        <div v-if="!uploadedPhoto" class="mb-3">
            <label for="photoInput" class="form-label">Dodaj zdjęcie</label>
            <input class="form-control form-control-sm" id="photoInput" type="file" @change="addfile" />
        </div>
        <div v-if="uploadedPhoto">
            <h6>Przeciągnij zdjęcie wizytówki</h6>
            <DraggableNode :item="{ type: 'photo', src: uploadedPhoto }" />
        </div>
        <h6>Przeciągnij tekst wizytówki</h6>
        <DraggableNode :item="{ type: 'text' }" />
        <div :class="styles.colorPicker">
            <label for="colorInput" class="form-label">Ustaw kolor wizytówki</label>
            <input type="color" class="form-control form-control-color" id="colorInput" value="#ffffff"
                @change="handleSetColor" />
        </div>
        <button @click="handleSaveCard" class="btn btn-light">Zapisz wizytówkę</button>
    </div>
</template>

<script setup>
import { ref } from "vue";
import { fileAsBase64 } from "@/utils";
import { DraggableNode } from "./draggable"
import useCardCreator from "./store/useCardCreator";

import styles from "./ToolsPanel.module.css";

const { setCardColor, color, dropzoneBlocks } = useCardCreator();

const uploadedPhoto = ref();

const handleSetColor = (event) => setCardColor(event.target.value);
const addfile = (event) =>
    fileAsBase64(
        event.target.files[0],
        (base64) => (uploadedPhoto.value = base64)
    );

const handleSaveCard = () => console.log(JSON.stringify({ color, placedItems: dropzoneBlocks }))
</script>