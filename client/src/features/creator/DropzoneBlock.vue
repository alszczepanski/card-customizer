<template>
    <div :class="styles.block" @drop="handleDrop" @dragenter.prevent @dragover.prevent>
      <DraggableNode v-if="placedItem" :type="placedItem.type" />
    </div>
</template>


<script setup>
import { storeToRefs } from 'pinia';
import { defineProps, ref, watch } from 'vue';
import useDropzone from './store/useDropzone';
import { DraggableNode } from './draggable';
import styles from './DropzoneBlock.module.css'

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