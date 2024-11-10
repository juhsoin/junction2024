<script setup lang="ts">
import ApiGrid from "@/components/ApiGrid.vue"
import { fetchApis, type IApi } from "../api/apis"
import { ref, onMounted } from "vue"


const apis = ref<IApi[]>([])
const loading = ref(true)

onMounted(() => {
	fetchApis().then((response) => {
		apis.value = response
		console.log(response)
		loading.value = false
	})
})
</script>

<template>
	<VContainer>
		<h1>Active Fingrid Services</h1>
		<div v-if="loading">Loading...</div>
		<ApiGrid v-else :api-list="apis" :short-form="false" />
	</VContainer>
</template>
