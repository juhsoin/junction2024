<script setup lang="ts">
import ApiGrid from '@/components/ApiGrid.vue';
import TicketGrid from '@/components/TicketGrid.vue';
import router from '../router/index'

import { VContainer } from 'vuetify/components';



// plaeholder for demo purposes
const ticketInfo = [
	{
		id: '1',
		title: 'First ticket',
		description: 'First Description'
	},
	{
		id: '2',
		title: 'First ticket',
		description: 'First Description'
	},
	{
		id: '3',
		title: 'First ticket',
		description: 'First Description'
	},
	{
		id: '4',
		title: 'First ticket',
		description: 'First Description'
	},
]

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
		<TicketGrid :tickets="ticketInfo">
		</TicketGrid>
		<VBtn variant="plain" color="primary" @click="handleNavigation('/tickets')">Show All</VBtn>
	</VContainer>
	<VContainer>
		<h1>Your Fingrid Services</h1>
		<ApiGrid :api-list="apiInfo" :short-form="true" />
		<VBtn variant="plain" color="primary" @click="handleNavigation('/apis')">Show All</VBtn>
	</VContainer>
</template>
