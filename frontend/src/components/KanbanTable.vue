<script lang="ts" setup>
import { defineProps, defineEmits } from 'vue';
import { VContainer, VDivider } from 'vuetify/components';
import TicketCard from './TicketCard.vue';
import type { ITicket } from '@/api/ticket';
import { EStates } from '@/filters/filter';

const props = defineProps<{
  tickets: ITicket[];
}>();

// Emit an action event when the button is clicked
const emit = defineEmits<{
  (e: 'action-clicked'): void;
}>();

const filteredTickets = (scope: number) => {
    return props.tickets.filter((ticket) => Math.min(parseInt(ticket.status), 5) === scope )
}

const columns = [
  {
    title: 'Requested',
    status: 1,
  },
  {
    title: 'Clarification needed',
    status: 2,
  },

  {
    title: 'Approved',
    status: 3,
  },

  {
    title: 'In progress',
    status: 4,
  },

  {
    title: 'Resolved',
    status: 5,
  },
]

</script>

<template>
    <VContainer class="kanban-table">
      <VRow class="kanban-row">
      <VCol
        v-for="column in columns"
        :key="column.status"
        cols="auto"
        style="min-width: 250px;"
        class="kanban-column"
      > 
        <h3 class="column-title">{{ column.title }}</h3>
        <VDivider></VDivider>
        <TicketCard
          v-for="ticket in filteredTickets(column.status)"
          class="kanban-card"
          :ticket="ticket"
		  :followed="false"
        />
      </VCol>
    </VRow>
    </VContainer>
  </template>

<style scoped>

.kanban-row {
  width: 1700px !important;
}

.column-title {
  color: var(--brand-primary-red)
}

.kanban-column {
  background-color: var(--brand-lightest-blue-gray);
  border: 1px solid var(--brand-light-blue-gray);
  margin-left: 10px;
  padding: 15px;
  border-radius: 8px;
  min-height: 400px;
  min-width: 300px;
  min-height: 750px;
}

.kanban-card {
  margin-top: 5px;
}
</style>
