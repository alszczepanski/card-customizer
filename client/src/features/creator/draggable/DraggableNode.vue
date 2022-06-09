<template>
    <img v-if="props.type === 'photo'" :class="styles.img" src="./61.jpg" draggable="true" @dragstart="onDragStart($event, { type: 'photo' })" />
    <div v-if="props.type === 'text'" draggable="true" @dragstart="onDragStart($event, { type: 'text', value: 'TEXT' })">TEXT</div>
</template>

<script setup>
import { defineProps } from 'vue';
import styles from './Draggable.module.css'

const props = defineProps({
    type: String,
    dropzoneBlockId: String,
});

const onDragStart = (event, itemProperties) => {
    const { clientWidth: width, clientHeight: height } = event.currentTarget
    event.dataTransfer.dropEffect = "move"
    event.dataTransfer.setData("currentTarget", JSON.stringify({ width, height, ...itemProperties, previousBlockId: props.dropzoneBlockId }))
}

</script>