<script lang="ts" setup>
import { defineProps, defineEmits } from 'vue';
import { VCard, VCardTitle, VCardText, VCardActions, VBtn, VCardSubtitle } from 'vuetify/components';
import TicketModal from './TicketModal.vue';
import type { ITicket } from '@/api/ticket';
import { EStates } from '@/filters/filter';

// Define the props
const props = defineProps<{
  ticket: ITicket;
}>();

// Emit an action event when the button is clicked
const emit = defineEmits<{
  (e: 'action-clicked'): void;
}>();

// Handle action button click
const handleActionClick = () => {
  emit('action-clicked');
};

const stateHighlight = (ticket: ITicket) => {
  return parseInt(ticket.status) === 6  ? 'warning-state' :
   parseInt(ticket.status) === 5 ? 'confirmed-state' : '';
}
</script>

<template>
   <VCard class="ticket-card">
    <VCardTitle>
      {{ ticket.title }}
    </VCardTitle>
    <VCardText :class="stateHighlight(ticket)">{{ EStates[parseInt(ticket.status)] }}</VCardText>
    <VCardText color="secondary" class="description-paragraph">
      {{ ticket.description.slice(0, 30) + (ticket.description.length > 30 ? '...' : '')}}
    </VCardText>
    <VDialog scrollable>
        <template v-slot:activator="{ props: activatorProps }">
            <VCardActions>
                <VBtn variant="plain" v-bind="activatorProps" color="primary" @click="handleActionClick">Show details</VBtn>
            </VCardActions>
        </template>
        <template v-slot:default="{ isActive }">
          <TicketModal :ticket="ticket" class="ticket-modal"></TicketModal>
        </template>
    </VDialog>
  </VCard>
</template>

<style scoped>
.ticket-card {
  border: 1px solid #eee;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  max-height: 250px;
  max-width: 280px;
}

.description-paragraph {
  max-height: 10px;
}

.ticket-modal {
  align-self: center;
}

.warning-state {
  color: var(--brand-violet);
  text-decoration: line-through;
}

.confirmed-state {
  color: var(--brand-green);
}

</style>