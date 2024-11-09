<script setup lang="ts">

import TicketGrid from '@/components/TicketGrid.vue';

import { VContainer } from 'vuetify/components';
import { fetchTickets, type ITicket } from '../api/ticket';

import { onMounted, ref, toValue } from 'vue';


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
	<h1>Your Tickets</h1>
	<div v-if="loading">Loading...</div>
	<TicketGrid v-else :tickets="tickets">
	</TicketGrid>
	
</VContainer>
</template>
