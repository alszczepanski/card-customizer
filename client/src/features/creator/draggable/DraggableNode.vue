<template>
    <img v-if="props.item.type === 'photo'" :class="styles.img" :style="{
        width: (props.item?.width || 125) + 'px',
        height: (props.item?.height || 125) + 'px',
    }" src="./61.jpg" draggable="true" @dragstart="onDragStart($event, { type: 'photo' })" />
    <div v-if="props.item.type === 'text'" :class="styles.text" :style="{
        width: (props.item?.width || 75) + 'px',
        height: (props.item?.height || 35) + 'px',
    }" draggable="true" @dragstart="onDragStart($event, { type: 'text', value: props.item.value || 'TEXT' })">
        {{ props.item.value || "TEXT" }}
    </div>
</template>

<script setup>
import { defineProps } from 'vue';
import styles from './Draggable.module.css'

const props = defineProps({
    item: Object,
    dropzoneBlockId: String,
});

const onDragStart = (event, itemProperties) => {
    event.dataTransfer.dropEffect = "move";
    event.dataTransfer.setData(
        "currentTarget",
        JSON.stringify({
            width: props.item?.width || event.currentTarget.clientWidth,
            height: props.item?.height || event.currentTarget.clientHeight,
            ...itemProperties,
            previousBlockId: props.dropzoneBlockId,
        })
    );
};

</script>
