<script setup lang="ts">
import TicketGrid from '@/components/TicketGrid.vue';
import { VContainer } from 'vuetify/components';
import { fetchTickets, type ITicketResponse, type ITicket } from '../api/ticket';



// plaeholder for demo purposes

import { onMounted, ref } from 'vue';

const ticketInfo = ref<ITicketResponse | null>(null);

onMounted(async () => {
	ticketInfo.value = await fetchTickets();
});

</script>

<template>
<VContainer>
	<h1>Your Tickets</h1>
	<TicketGrid :tickets="ticketInfo">
	</TicketGrid>
	
</VContainer>
</template>
