<script setup lang="ts">
import { fetchTickets, type ITicket } from '@/api/ticket';
import AddNewTicket from '@/components/AddNewTicket.vue';
import KanbanTable from '@/components/KanbanTable.vue';
import { useFilterStore } from '@/stores/filterStore';
import { onMounted, ref } from 'vue';
import { VSelect, VContainer, VCheckbox } from 'vuetify/components';
import { get_user_id } from "../stores/userState"

const store = useFilterStore();

const filter = ref<string | null>(null);
const tickets = ref<ITicket[]>([]);
const loading = ref(true);
const items = [
"Käyttöpaikkaprosessi"       ,
"Tuoteprosessi"              ,
"Mittaustietoprosessi"       ,
"Asiakastietoprosessi"       ,
"Sopimusprosessi"            ,
"Sanomahallinta"             ,
"Yleinen hallinta"           ,
"Tietosuoja"                 ,
"Kytkentä/katkaisuprosessi"  ,
"Laskutustiedot"             ,
"Valtuutusprosessi"          ,
"Tietoturva"                 ,
"Roolitus"                   ,
"Mittaustiedonhallinta"      ,
"Raportointi"                ,
"Toimeksiantoprosessi"       ,
"Loppuasiakaskäyttöliittymä" ,
"Laskennat"                  ,
"Osapuolitiedot"             ,
"Kuormanohjausprosessi"      
]
const key = ref('test')

onMounted(() => {
	fetchTickets().then((response) => {
		tickets.value = response;
		loading.value = false;
	});
});

const toggleFilter = async (value: string) => {
	store.$state.filter.categories = value;
	tickets.value = await fetchTickets();
}

const toggle = (value) => {
	if (value) {
		store.$state.filter.user_id = get_user_id();
	} else {
		store.$state.filter.user_id = "";
	}
	fetchTickets().then((res) => {
		tickets.value = res
	})
}
</script>

<template>
    <VContainer :key="key">
		<h1 class="title-text">Tickets workflow view</h1>
		<VSelect
			:items="items"
			v-model="filter"
			@update:model-value="(value: string) => toggleFilter(value)"
			chips
			closable-chips
		></VSelect>
		<AddNewTicket :categories="items" class="add-ticket-dialog"/>
		<VCheckbox label="Show only my tickets" @update:model-value="(value) => toggle(value)"></VCheckbox>
		<div v-if="loading">Loading...</div>
        <KanbanTable v-else :tickets="tickets"></KanbanTable>
    </VContainer>
</template>

<style scoped>
:deep(.v-field__input input) {
	display: none;
}
</style>
