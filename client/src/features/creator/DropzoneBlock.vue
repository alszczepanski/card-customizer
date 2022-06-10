<template>
    <div :class="styles.block" @drop="handleDrop" @dragenter.prevent @dragover.prevent>
       <DraggableNode v-if="placedItem" :item="placedItem" :dropzone-block-id="props.id" />
    </div>
</template>


<script setup>
import { storeToRefs } from 'pinia';
import { defineProps, ref, watch } from 'vue';

import useCardCreator from './store/useCardCreator';
import { DraggableNode } from './draggable';

import styles from './DropzoneBlock.module.css'

const dropzoneStore = useCardCreator();
const { setItem, getItem } = dropzoneStore;
const { dropzoneBlocks } = storeToRefs(dropzoneStore);

const placedItem = ref();

watch(dropzoneBlocks, () => placedItem.value = getItem(props.id));
const props = defineProps({
    id: String
})

const handleDrop = (event) => {
    if (!placedItem.value) {
        setItem(props.id, JSON.parse(event.dataTransfer.getData("currentTarget")));
    }
}
</script> 