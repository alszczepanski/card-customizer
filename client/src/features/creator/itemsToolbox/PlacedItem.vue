<template>
    <div v-if="props.item.type === 'text'">
        <div class="input-group input-group-sm flex-nowrap">
            <span class="input-group-text" id="addon-wrapping">Wysokość</span>
            <input v-model="height" type="text" class="form-control" placeholder="Wysokość" aria-label="Wysokość" aria-describedby="addon-wrapping">
        </div>
        <div class="input-group input-group-sm  flex-nowrap">
            <span class="input-group-text" id="addon-wrapping">Szerokość</span>
            <input v-model="width" type="text" class="form-control" placeholder="Szerokość" aria-label="Szerokość" aria-describedby="addon-wrapping">
        </div>
        <div class="input-group input-group-sm flex-nowrap">
            <span class="input-group-text" id="addon-wrapping">Tekst</span>
            <input v-model="value" type="text" class="form-control" placeholder="Tekst" aria-label="Tekst" aria-describedby="addon-wrapping">
        </div>
        <button @click="handleSubmit">Zatwierdź zmiany</button>
    </div>
</template>

<script setup>
    import { defineProps, ref } from "vue";
     const props = defineProps({
        item: Object,
        onChange: Function,
    })
    console.log(props.item);
    const height = ref(props.item.height);
    const width = ref(props.item.width);
    const value = ref(props.item.value);
    const handleSubmit = () => {
        props.onChange({ height: height.value, width: width.value, value: value.value });
    }
</script> 
