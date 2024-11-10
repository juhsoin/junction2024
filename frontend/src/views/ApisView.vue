<script setup lang="ts">
import ApiGrid from '@/components/ApiGrid.vue';

const apiInfo = [
	{
		id: '1',
		title: 'Wind Speed API',
		description: 'Supplies information about the wind speeds at various power plants',
		status: 'Active',
		updateSummary: 'Next release will modify the payload data format for user requests.',
		version: '2.4.2',
		nextRelease: '2.5.0',
	},
	{
		id: '2',
		title: 'Electricity Price API',
		description: 'Supplies information about the latest electricity prices in Finland',
		status: 'Active',
		updateSummary: 'Next release will modify the update interval for the price fetching.',
		version: '1.3.4',
		nextRelease: '1.4.0',
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
