<script lang="ts" setup>
import { defineProps, defineEmits } from 'vue';
import { VContainer, VDivider } from 'vuetify/components';
import TicketCard from './TicketCard.vue';


interface ticketCardInfo {
    id: string;
    title: string;
    description: string;
    scope: string;
}

const props = defineProps<{
  tickets: ticketCardInfo[];
}>();

// Emit an action event when the button is clicked
const emit = defineEmits<{
  (e: 'action-clicked'): void;
}>();

const filteredTickets = (scope: string) => {
    return props.tickets.filter((ticket) => ticket.scope === scope )
}

const columns = [
  {
    title: 'Requested',
    status: 'NEW',
  },
  {
    title: 'In Progress',
    status: 'In progress',
  },

  {
    title: 'Valitated',
    status: 'Started',
  },

  {
    title: 'Resolved',
    status: 'Started',
  },

  {
    title: 'Clarification',
    status: 'Started',
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
        <TicketCard
          v-for="ticket in filteredTickets(column.status)"
          :key="ticket.id"
          :title="ticket.title"
          :description="ticket.description"
        />
      </VCol>
      
    </VRow>
    </VContainer>
  </template>

<style scoped>

.kanban-row {
  width: 2500px !important;
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
}
</style>