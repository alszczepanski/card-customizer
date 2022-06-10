<template>
    <div :class="styles.toolbox">TOOLBOX
        <div v-for="block of dropzoneBlocks" :key="block.id">
            <PlacedItem v-if="block.placedItem" :item="block.placedItem" :onChange="(item) => handleSubmit(item, block.id)" />
        </div>
    </div>
</template>

<script setup>
import { storeToRefs } from 'pinia';
import styles from './Toolbox.module.css'
import useCardCreator from '../store/useCardCreator';
import PlacedItem from './PlacedItem.vue';

const store = useCardCreator();
const { updateItem } = store;
const { dropzoneBlocks } = storeToRefs(store);

const handleSubmit = (item, blockId) => updateItem(blockId, item);
</script>
