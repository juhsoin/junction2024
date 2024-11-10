<template>
	<v-container>
		<!-- Button to open the ticket creation popup -->
		<v-btn color="primary" @click="toggleDialog">
			Add New Ticket
		</v-btn>

		<!-- Dialog for adding a new ticket -->
		<v-dialog v-model="dialogVisible" max-width="600px">
			<v-card>
				<v-card-title>
					<span class="text-h6">Create New Ticket</span>
				</v-card-title>

				<v-card-text>
					<!-- Ticket Header Field -->
					<v-text-field v-model="header" label="Ticket Header" outlined dense
						placeholder="Enter a brief title for the problem" />

					<!-- Ticket Description Field -->
					<v-textarea v-model="description" label="Problem Description" outlined autogrow
						placeholder="Describe the problem in detail" />


					<VSelect :items="props.categories" v-model="filter" chips closable-chips></VSelect>
				</v-card-text>

				<v-card-actions>
					<!-- Submit and Close Buttons -->
					<v-btn color="primary" @click="submitTicket">Submit Ticket</v-btn>
					<v-btn color="secondary" @click="toggleDialog">Cancel</v-btn>
				</v-card-actions>
			</v-card>
		</v-dialog>
	</v-container>
</template>

<script lang="ts" setup>
import { ref, defineProps } from 'vue';
import { createTicket } from '@/api/ticket';

const dialogVisible = ref(false);    // Controls visibility of the popup
const header = ref<string>('');      // Header field for the ticket
const description = ref<string>(''); // Problem description field

const props = defineProps(["categories"])
const filter = ref(props.categories[0])

// Toggles the visibility of the dialog
const toggleDialog = () => {
	dialogVisible.value = !dialogVisible.value;
};

const emit = defineEmits<{
	(e: 'submit-ticket', ticket: { header: string; description: string }): void;
}>();

// Function to submit the ticket
const submitTicket = () => {
	if (header.value.trim() && description.value.trim()) {
		const newTicket = {
			title: header.value,
			description: description.value,
			categories: filter.value,
		};
		// console.log(newTicket)
		createTicket(newTicket)
		emit('submit-ticket', newTicket); // Emit the new ticket data to the parent

		// Reset fields and close the dialog after submission
		header.value = '';
		description.value = '';
		dialogVisible.value = false;
	} else {
		alert('Please fill out both the header and description.');
	}
};
</script>

<style scoped>
.v-dialog {
	max-width: 600px;
}
</style>
