<script lang="ts" setup>
import { ref, defineProps } from 'vue';
import { subscRibeToTickets } from '@/api/ticket';
import { VBtn } from 'vuetify/components';

const props = defineProps(["ticket_id"])

// const follow_but_text = ref("Follow")
const subs = () => {
	console.log("subscriibattu!")
	subscRibeToTickets(props.ticket_id)
}
</script>

<template>
	<div class="modal-header-interactions">
		<VBtn icon="mdi-thumb-up" color="primary"></VBtn> <br>
		<VBtn color="primary" @click="subs">Follow</VBtn>
	</div>
</template>
