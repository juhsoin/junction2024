<script lang="ts" setup>
import { ref } from 'vue';
import router from '../router/index'
import { VAppBar, VToolbarTitle, VSpacer, VBtn, VIcon } from 'vuetify/components';

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
            Services
        </VBtn>
        <VBtn icon @click="handleNavigation('/tickets')">
            Tickets
        </VBtn>
    </div>
    <div class="user-view">
        <v-icon>mdi-account-circle-outline</v-icon>
        Customer Account
    </div>
  </VAppBar>
</template>

<style scoped>
/* Add any custom styling here */
    .button-grid {
        padding-right: 30px;
    }
    .v-btn {
        margin: 40px;
    }
    .user-view {
        padding-right: 30px;
    }
</style>