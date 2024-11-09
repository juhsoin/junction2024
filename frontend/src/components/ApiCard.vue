<script lang="ts" setup>
import { defineProps, defineEmits } from 'vue';
import { VCard, VCardTitle, VCardText } from 'vuetify/components';

const props = defineProps<{
    id: string;
    title: string;
    description: string;
    status: string;
    shortForm: boolean;
}>();

const emit = defineEmits<{
  (e: 'ticket-action', ticket: { id: number; title: string; description: string }): void;
}>();

</script>

<template>
   <VCard v-if="shortForm" class="api-card">
        <VCardTitle>{{ title }}</VCardTitle>
        <VCardSubtitle>{{ status }}</VCardSubtitle>
        <VCardText>{{ description }}</VCardText>
    </VCard>

    <VCard v-else class="api-card">
        <VCardTitle>{{ title }}</VCardTitle>
        <VCardSubtitle>{{ status }}</VCardSubtitle>
        <VCardText>Current Version: 1.2.3</VCardText>
        <VCardText>Next release: 1.3.0</VCardText>
        <VCardText>Next change description</VCardText>
        <VCardText>{{ description }}</VCardText>
    </VCard>
</template>

<style scoped>
.ticket-row {
    width: 1000px;
}
</style>