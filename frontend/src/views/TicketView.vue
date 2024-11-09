<script setup lang="ts">
import { fetchTickets, type ITicket } from '@/api/ticket';
import KanbanTable from '@/components/KanbanTable.vue';
import { onMounted, ref } from 'vue';
import { VContainer } from 'vuetify/components';

const tickets = ref<ITicket[]>([]);
const loading = ref(true);

onMounted(() => {
	fetchTickets().then((response) => {
		tickets.value = response;
		loading.value = false;
	});
});

</script>

<template>
    <VContainer class="kanban-table">
        <h1>Tickets workflow view</h1>
		<div v-if="loading">Loading...</div>
        <KanbanTable v-else :tickets="tickets"></KanbanTable>
    </VContainer>
</template>

<style scoped>
</style>