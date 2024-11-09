<script setup lang="ts">
import { fetchTickets, type ITicket } from '@/api/ticket';
import AddNewTicket from '@/components/AddNewTicket.vue';
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
    <VContainer>
		<h1 class="title-text">Tickets workflow view</h1>
		<AddNewTicket class="add-ticket-dialog"/>
		<div v-if="loading">Loading...</div>
        <KanbanTable v-else :tickets="tickets"></KanbanTable>
    </VContainer>
</template>

<style scoped>
</style>