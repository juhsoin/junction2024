<script setup lang="ts">
import KanbanTable from '@/components/KanbanTable.vue';
import { VContainer } from 'vuetify/components';

// plaeholder for demo purposes
const ticketInfo = [
	{
		id: '1',
		title: 'First ticket',
		description: 'First Description',
        scope: "In progress",
	},
	{
		id: '2',
		title: 'First ticket',
		description: 'First Description',
        scope: "In progress",
	},
	{
		id: '3',
		title: 'First ticket',
		description: 'First Description',
        scope: "In progress",
	},
	{
		id: '4',
		title: 'First ticket',
		description: 'First Description',
        scope: "In progress",
	},
]
</script>

<template>
    <VContainer class="kanban-table">
        <h1>Tickets workflow view</h1>
        <KanbanTable :tickets="ticketInfo"></KanbanTable>
    </VContainer>
</template>

<style scoped>
</style>