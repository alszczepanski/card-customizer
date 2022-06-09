<template>
    <div :class="styles.container">
        <div :class="styles.card">
            <div :class="styles.column" v-for="row of rows" :key="row">
                <DropzoneBlock v-for="col of cols" :key="col" />
            </div>
        </div>
    </div>
</template>

<script setup>
import styles from "./CardDropzone.module.css";
import DropzoneBlock from "./DropzoneBlock.vue";
const cols = [...Array(10).keys()];
const rows = [...Array(10).keys()];
</script> 