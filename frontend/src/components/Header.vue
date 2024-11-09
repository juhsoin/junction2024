<script lang="ts" setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { VAppBar, VToolbarTitle, VSpacer, VBtn, VIcon } from 'vuetify/components';

const router = useRouter();

const title = ref('Fingrid Service Hub');
const handleNavigation = (route: string) => {
  router.push(route);
};
</script>

<template>
  <VAppBar app color="primary">
    <VToolbarTitle>{{ title }}</VToolbarTitle>
    <VSpacer />
    <div class="button-grid">
        <VBtn icon @click="handleNavigation('/')">
            Home
        </VBtn>
        <VBtn icon @click="handleNavigation('/apis')">
            APIs
        </VBtn>
        <VBtn icon @click="handleNavigation('/tickets')">
            Tickets
        </VBtn>
    </div>
  </VAppBar>
</template>

<style scoped>
/* Add any custom styling here */
    .button-grid {
        padding-right: 15px;
    }
    .v-btn {
        margin: 30px;
    }
</style>