<script lang="ts" setup>
import { defineProps, defineEmits } from 'vue';
import { VCard, VCardTitle, VCardText, VCardActions, VBtn } from 'vuetify/components';
import TicketModal from './TicketModal.vue';
import type { ITicket } from '@/api/ticket';

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
</script>

<template>
   <VCard class="ticket-card">
    <VCardTitle>
      {{ ticket.title }}
    </VCardTitle>
    <VCardText color="secondary">
      {{ ticket.description }}
    </VCardText>
    <VDialog scrollable>
        <template v-slot:activator="{ props: activatorProps }">
            <VCardActions>
                <VBtn v-bind="activatorProps" color="primary" @click="handleActionClick">Show details</VBtn>
            </VCardActions>
        </template>
        <template v-slot:default="{ isActive }">
          <TicketModal :ticket="ticket", class="ticket-modal"></TicketModal>
        </template>
    </VDialog>
  </VCard>
</template>

<style scoped>
.ticket-card {
  border: 1px solid #eee;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.ticket-modal {
  align-self: center;
}

</style>