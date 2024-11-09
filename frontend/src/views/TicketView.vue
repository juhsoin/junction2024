<script setup lang="ts">
import { fetchTickets, type ITicket } from '@/api/ticket';
import AddNewTicket from '@/components/AddNewTicket.vue';
import KanbanTable from '@/components/KanbanTable.vue';
import { useFilterStore } from '@/stores/filterStore';
import { onMounted, ref } from 'vue';
import { VSelect, VContainer } from 'vuetify/components';

const store = useFilterStore();

const filter = ref<string | null>(null);
const tickets = ref<ITicket[]>([]);
const loading = ref(true);
const items = ['category 1', 'category 2', 'my tickets']
const key = ref('test')

onMounted(() => {
	fetchTickets().then((response) => {
		tickets.value = response;
		loading.value = false;
	});
});

const toggleFilter = async (value: string) => {
	store.$state.filter.categories = value;
	tickets.value = await fetchTickets();
}
</script>

<template>
    <VContainer :key="key">
		<h1 class="title-text">Tickets workflow view</h1>
		<VSelect
			:items="items"
			v-model="filter"
			@update:model-value="(value: string) => toggleFilter(value)"
			chips
			closable-chips
		></VSelect>
		<AddNewTicket class="add-ticket-dialog"/>
		<div v-if="loading">Loading...</div>
        <KanbanTable v-else :tickets="tickets"></KanbanTable>
    </VContainer>
</template>

<style scoped>
:deep(.v-field__input input) {
	display: none;
}
</style>