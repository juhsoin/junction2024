<script lang="ts" setup>
import { VRow, VContainer } from 'vuetify/components';
import ApiCard from './ApiCard.vue';
import { IApi } from "../api/apis"

const props = defineProps<{
  apiList: IApi[];
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
            :next-release="api.next_release"
            :update-summary="api.update_summary"
            :version="api.version"
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
