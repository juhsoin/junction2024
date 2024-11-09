<script setup lang="ts">
import ApiGrid from '@/components/ApiGrid.vue';

const apiInfo = [
	{
		id: '1',
		title: 'Wind service',
		description: 'Tuuli?',
		status: 'Status',
	},
	{
		id: '1',
		title: 'Wind service',
		description: 'Tuuli?',
		status: 'Status',
	},
]

// import TheWelcome from '../components/TheWelcome.vue'
</script>

<template>
	<VContainer>
		<h1>Active Fingrid Services</h1>
		<ApiGrid :api-list="apiInfo" :short-form="false" />
	</VContainer>
</template>
