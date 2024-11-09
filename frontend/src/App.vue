<script setup lang="ts">
import { RouterView } from 'vue-router'
import Footer from './components/Footer.vue'
import Header from './components/Header.vue';
import { VApp, VMain } from 'vuetify/components';
</script>

<template>
	<VApp>
		<Header />
		<VMain>
			<RouterView />
		</VMain>
		<Footer />
	</VApp>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,100..1000;1,9..40,100..1000&family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap');

:root {
	--brand-primary-red: #D5121E;
	--brand-secondary-blue-gray:  #3E5660;
	--brand-light-blue-gray:  #6D838F;
	--brand-lighter-blue-gray: #D5DDE3;
	--brand-lightest-blue-gray: #E9EEF2;
	--brand-dark-green: #277158;
	--brand-green:  #4d9d88;
	--brand-pink: #e5b2bb;
	--brand-violet: #A15885;
	--brand-yellow: #f8f43f;
	--brand-light-blue: #a5d0e2;
}

.v-application {
	font-family: Inter !important;
}
</style>
