<script lang="ts" setup>
import { defineProps, defineEmits } from 'vue';
import { VCard, VCardTitle, VCardText, VCardActions, VBtn } from 'vuetify/components';

// Define the props
const props = defineProps<{
  title: string;
  description: string;
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
      {{ title }}
    </VCardTitle>
    <VCardText>
      {{ description }}
    </VCardText>
    <VCardActions>
      <VBtn color="primary" @click="handleActionClick">Take Action</VBtn>
    </VCardActions>
  </VCard>
</template>

<style scoped>
.ticket-card {
  border: 1px solid #eee;
  width: 300px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
</style>