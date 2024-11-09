<script lang="ts" setup>
import { VFooter, VContainer, VRow, VCol, VDivider } from 'vuetify/components';

const currentYear = new Date().getFullYear();
</script>

<template>
  <VFooter app color="primary" class="footer">
      <VContainer class="text-center">
        <span>&copy; {{ new Date().getFullYear() }} Fingrid Service Hub</span>
      </VContainer>
    </VFooter>
</template>

<style scoped>
/* Add any custom styling here */
.v-footer {
}
</style>