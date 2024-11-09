<script setup lang="ts">
import TicketGrid from '@/components/TicketGrid.vue';
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
</script>

<template>
<VContainer>
	<h1>Your Tickets</h1>
	<TicketGrid :tickets="ticketInfo">
	</TicketGrid>
	
</VContainer>
</template>
