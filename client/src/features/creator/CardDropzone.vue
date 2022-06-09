<template>
    <div :class="styles.container">
        <div :class="styles.card">
            <div :class="styles.column" v-for="col of cols" :key="col">
                <DropzoneBlock v-for="row of rows" :key="row" :id="'block-row' + row + '-col' + col" />
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from "vue";
import styles from "./CardDropzone.module.css";
import DropzoneBlock from "./DropzoneBlock.vue";
const cols = ref([...Array(10).keys()]);
const rows = ref([...Array(10).keys()]);
</script> 