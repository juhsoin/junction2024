import { ref, computed } from "vue"
import { defineStore } from "pinia"
import { type IFilter } from "@/filters/filter"

export const useCounterStore = defineStore("counter", () => {
	const count = ref(0)
	const doubleCount = computed(() => count.value * 2)
	function increment() {
		count.value++
	}
	return { count, doubleCount, increment }
})

export const useFilterStore = defineStore("filter", {
	state: () => {
		return {
			filter: {} as IFilter
		}
	},
	getters: {
		getFilter(state) {
			return state.filter
		}
	},
})
