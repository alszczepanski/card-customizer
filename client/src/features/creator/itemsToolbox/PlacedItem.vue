<template>
    <div :class="styles.container">
        <div class="form-group">
            <label for="heightinput">Wysokość</label>
<input v-model="width" type="text" id="widthtinput" class="form-control form-control-sm" placeholder="Wysokość" aria-label="Wysokość" aria-describedby="addon-wrapping">
        </div>
        <div class="form-group">
            <label for="widthtinput">Szerokość</label>
            <input v-model="height" type="text" id="widthtinput" class="form-control form-control-sm"
                placeholder="Wysokość" aria-label="Wysokość" aria-describedby="addon-wrapping">
        </div>
        <div v-if="props.item.type === 'text'" class="form-group">
            <label for="textinput">Tekst</label>
            <textarea v-model="value" class="form-control form-control-sm" id="textinput" rows="3"></textarea>
        </div>
        <button type="button" class="btn btn-primary btn-sm" @click="handleSubmit">Zatwierdź zmiany</button>
    </div>
</template>

<script setup>
import { defineProps, ref } from "vue";

import styles from './PlacedItem.module.css'

const props = defineProps({
    item: Object,
    onChange: Function,
})

const height = ref(props.item.height);
const width = ref(props.item.width);
const value = ref(props.item.value);

const handleSubmit = () => {
    props.onChange({ height: parseInt(height.value), width: parseInt(width.value), value: value.value });
}
</script> 
