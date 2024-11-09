<script setup lang="ts">

import TicketGrid from '@/components/TicketGrid.vue';

import { VContainer } from 'vuetify/components';
import { fetchTickets, type ITicketResponse, type ITicket } from '../api/ticket';



// plaeholder for demo purposes

import { onMounted, ref, toValue } from 'vue';


const ticket = ref<ITicketResponse>([]);
const loading = ref(true);


onMounted(async () => {
	ticket.value = await fetchTickets();
	console.log(ticket.value);
	loading.value = false;
});

</script>

<template>
<VContainer>
	<h1>Your Tickets</h1>
	<TicketGrid :tickets="ticket">
	</TicketGrid>
	
</VContainer>
</template>
