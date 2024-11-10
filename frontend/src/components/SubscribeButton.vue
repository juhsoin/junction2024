<script lang="ts" setup>
import { ref, defineProps, onMounted, defineEmits } from 'vue';
import { subscRibeToTickets, unsubscRibeToTickets } from '@/api/ticket';
import { VBtn } from 'vuetify/components';

const props = defineProps(["ticket_id", "followed"])
const emit = defineEmits(["deleted"])

const subs = () => {
	console.log("subscriibattu!")
	subscRibeToTickets(props.ticket_id)
}

onMounted(() => {
console.log(props.followed)
})

const unsub = () => {
	console.log("unsubscriibattu!")
	unsubscRibeToTickets(props.ticket_id)
	emit("deleted")
}
</script>

<template>
	<div class="modal-header-interactions">
		<VBtn icon="mdi-thumb-up" color="primary"></VBtn> <br>
		<VBtn v-if="!props.followed" color="primary" @click="subs">Follow</VBtn>
		<VBtn v-else color="primary" @click="unsub">Unfollow</VBtn>
	</div>
</template>

<style scoped>
	.v-btn {
		margin-top: 10px;
	}
</style>