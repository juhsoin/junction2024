<script lang="ts" setup>
import { defineProps, defineEmits } from 'vue';
import { VCard, VCardTitle, VCardText } from 'vuetify/components';
import { type IApi } from "../api/apis"

const props = defineProps<{
    id: string | undefined;
    title: string;
    description: string;
    status: string;
    updateSummary?: string;
    shortForm: boolean;
    version: string |undefined;
    nextRelease?: string;
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
        <VCardSubtitle>Status: {{ status }}</VCardSubtitle> 
        <VCardText>Description: {{ description }}</VCardText>
        <VCardText>Current Version: {{ version }}</VCardText>
        <VCardText>Next release: {{ nextRelease }} </VCardText>
        <VCardText>{{ updateSummary }}</VCardText>

    </VCard>
</template>

<style scoped>
.ticket-row {
    width: 1000px;
}
</style>
