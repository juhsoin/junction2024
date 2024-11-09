<script lang="ts" setup>
import { VCol, VRow, VContainer } from 'vuetify/components';
import {type ITicket, type ITicketResponse} from '../api/ticket';

const props = defineProps<{
  tickets: ITicketResponse | null;
}>();

const emit = defineEmits<{
  (e: 'ticket-action', ticket: { id: number; title: string; description: string }): void;
}>();

const tickets = props.tickets;

</script>

<template>
   <VContainer>
    <VRow :gutter="0" class="ticket-row">
      <VCol
        v-for="ticket in tickets"
        :key="ticket.id"
        cols="4"
        >
        <TicketCard
          ticket: ticket;
        />
      </VCol>
    </VRow>
   </VContainer>
</template>

<style scoped>
.ticket-row {
    width: 1000px;
}
</style>