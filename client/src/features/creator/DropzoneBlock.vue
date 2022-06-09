<template>
    <div :class="styles.block" @drop="handleDrop" @dragenter.prevent @dragover.prevent>
        <div v-if="placedItem" :class="styles.renderedItem"> {{ placedItem.width }} {{ placedItem.height }}</div>
    </div>
</template>


<script setup>
import { storeToRefs } from 'pinia';
import { defineProps, ref, watch } from 'vue';
import styles from './DropzoneBlock.module.css'
import useDropzone from './store/useDropzone';
const dropzoneStore = useDropzone();
const { onDrop, getItem } = dropzoneStore;
const { dropzoneBlocks } = storeToRefs(dropzoneStore)
const placedItem = ref();
watch(dropzoneBlocks, () => placedItem.value = getItem(props.id));
const props = defineProps({
    id: String
})
const handleDrop = (event) => {
    if (!placedItem.value) {
        onDrop(props.id, JSON.parse(event.dataTransfer.getData("currentTarget")));
    }
}
</script> 