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
		title: 'Wind service',
		description: 'Tuuli?',
		status: 'Status',
	},
	{
		id: '1',
		title: 'Wind service',
		description: 'Tuuli?',
		status: 'Status',
	},
]

const handleNavigation = (route: string) => {
	router.push(route);
};
</script>

<template>
	<VContainer>
		<h1>Your Tickets</h1>
		<div v-if="loading">Loading...</div>
		<TicketGrid v-else @deleted="refresh" :followed="true" :tickets="tickets">
		</TicketGrid>
		<VBtn variant="plain" color="primary" @click="handleNavigation('/tickets')">Show All</VBtn>
	</VContainer>
	<VContainer>
		<h1>Your Fingrid Services</h1>
		<ApiGrid :api-list="apiInfo" :short-form="true" />
		<VBtn variant="plain" color="primary" @click="handleNavigation('/apis')">Show All</VBtn>
	</VContainer>
</template>
