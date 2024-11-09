<script lang="ts" setup>
import { VCol, VRow, VContainer } from 'vuetify/components';
import { type ITicket } from '../api/ticket';
import TicketCard from './TicketCard.vue';

const props = defineProps<{
	tickets: ITicket[];
	followed?: boolean;
}>();

const emit = defineEmits<{
	(e: 'ticket-action', ticket: { id: number; title: string; description: string }): void;
	(e: 'deleted'): void;
}>();

</script>

<template>
	<VContainer>
		<VRow :gutter="0" class="ticket-row">
			<VCol v-for="ticket in tickets" :key="ticket.id" cols="4">
				<TicketCard @deleted="$emit('deleted')" :followed="props.followed" :ticket="ticket" />
			</VCol>
		</VRow>
	</VContainer>
</template>

<style scoped>
.ticket-row {
	width: 1000px;
}
</style>
