<script setup lang="ts">
import ApiGrid from '@/components/ApiGrid.vue';
import TicketGrid from '@/components/TicketGrid.vue';
import router from '../router/index'

import { VContainer } from 'vuetify/components';
import { fetchUsersTickets, type ITicket } from '../api/ticket';

import { onMounted, ref } from 'vue';


const tickets = ref<ITicket[]>([]);
const loading = ref(true);


onMounted(() => {
	fetchUsersTickets().then((response) => {
		console.log(response)
		tickets.value = response
		loading.value = false;
	});
});

const refresh = () => {
	fetchUsersTickets().then((response) => {
		console.log(response)
		tickets.value = response
		loading.value = false;
	});
}

const apiInfo = [
	{
		id: '1',
		title: 'Wind Speed API',
		description: 'Supplies information about the wind speeds at various power plants.',
		status: 'Active',
		updateSummary: 'Next release will modify the data format for.',
		version: '2.4.2',
		nextRelease: '2.5.0',
	},
	{
		id: '2',
		title: 'Electricity Price API',
		description: 'Supplies information about the latest electricity prices in Finland.',
		status: 'Active',
		updateSummary: 'Next release will modify the update interval for the price fetching.',
		version: '1.3.4',
		nextRelease: '1.4.0',
	},
]

const handleNavigation = (route: string) => {
	router.push(route);
};
</script>

<template>
	<VContainer :key="tickets.toString()">
		<h1>Your Tickets</h1>
		<div v-if="loading">Loading...</div>
		<div v-if="!tickets.length && !loading" class='empty-state'> You are not following any tickets at the moment.</div>
		<TicketGrid v-else @deleted="refresh" :followed="true" :tickets="tickets">
		</TicketGrid>
		<VBtn variant="plain" color="primary" @click="handleNavigation('/tickets')">Show All Tickets</VBtn>
	</VContainer>
	<VContainer>
		<h1>Your Fingrid Services</h1>
		<ApiGrid :api-list="apiInfo" :short-form="true" />
		<VBtn variant="plain" color="primary" @click="handleNavigation('/apis')">Show All Services</VBtn>
	</VContainer>
</template>

<style scoped>
	.empty-state {
		margin-left: 10px;
		margin-top: 10px;
	}
</style>
