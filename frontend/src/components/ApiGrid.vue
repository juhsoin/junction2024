<script lang="ts" setup>
import { VRow, VContainer } from 'vuetify/components';
import ApiCard from './ApiCard.vue';

interface apiInfo {
    id: string;
    title: string;
    description: string;
    status: string;
}

const props = defineProps<{
  apiList: apiInfo[];
  shortForm: boolean;
}>();


const emit = defineEmits<{
  (e: 'ticket-action', ticket: { id: number; title: string; description: string }): void;
}>();

</script>

<template>
   <VContainer>
    <VRow :gutter="0" 
        class="api-row"
        v-for="api in apiList">
        <ApiCard 
            :title="api.title"
            :id="api.id"
            :description="api.description"
            :status="api.status"
            :short-form="shortForm"
        ></ApiCard>
    </VRow>
   </VContainer>
</template>

<style scoped>
.api-row {
    width: 1000px;
}

.api-card {
    margin-top: 5px;
    width: 1000px;
    background-color: var(--brand-lighter-blue-gray)
}
</style>