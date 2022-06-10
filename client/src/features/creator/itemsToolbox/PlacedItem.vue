<template>
    <div>
        <div class="input-group input-group-sm flex-nowrap">
            <span class="input-group-text" id="addon-wrapping">Wysokość</span>
            <input v-model="height" type="text" class="form-control" placeholder="Wysokość" aria-label="Wysokość" aria-describedby="addon-wrapping">
        </div>
        <div class="input-group input-group-sm  flex-nowrap">
            <span class="input-group-text" id="addon-wrapping">Szerokość</span>
            <input v-model="width" type="text" class="form-control" placeholder="Szerokość" aria-label="Szerokość" aria-describedby="addon-wrapping">
        </div>
        <div v-if="props.item.type === 'text'" class="input-group input-group-sm flex-nowrap">
            <span class="input-group-text" id="addon-wrapping">Tekst</span>
            <textarea v-model="value" class="form-control" id="textArea" rows="3"></textarea>
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
    
    const height = ref(props.item.height);
    const width = ref(props.item.width);
    const value = ref(props.item.value);

    const handleSubmit = () => {
         props.onChange({ height: parseInt(height.value), width: parseInt(width.value), value: value.value });
    }
</script> 
