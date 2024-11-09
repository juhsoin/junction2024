<script lang="ts" setup>
import { defineProps, defineEmits } from 'vue';
import { VCard, VCardTitle, VCardText } from 'vuetify/components';

const props = defineProps<{
    id: string;
    title: string;
    description: string;
    status: string;
}>();

const emit = defineEmits<{
  (e: 'ticket-action', ticket: { id: number; title: string; description: string }): void;
}>();

</script>

<template>
   <VCard class="api-card">
            <VCardTitle>{{ title }}</VCardTitle>
            <VCardSubtitle>{{ status }}</VCardSubtitle>
            <VCardText>{{ description }}</VCardText>
        </VCard>
</template>

<style scoped>
.ticket-row {
    width: 1000px;
}
</style>