import { API_URL, States } from "./common"

import { useFilterStore } from "../stores/filterStore"
import { get_user_id } from "../stores/userState"

export interface ITicket {
	id?: string
	title: string
	description: string
	status: string
	created_at?: string
	updated_at?: string
	root_id: string
	development_proposal?: string
	development_clarification?: string
	ball_park_estimate?: string
	impact_on_market?: number // 0 to 3
	priority?: number // 1 to 3
	argumentation_for_proposal?: string
	proposal_impact?: string
	next_steps?: string
	planned_release?: string
	categories?: string
	planned_release_version?: string
}

export interface ITicketComment {
	id: string
	title: string
	comment: string
	user_id: string
	created_at?: string
	updated_at?: string
	root_id: string
}

export const fetchTickets = async (): Promise<ITicket[]> => {
	const filterStore = useFilterStore()
	const filterValue = filterStore.$state.filter
	const response = await fetch(API_URL + "/tickets/all", {
		method: "POST",
		body: JSON.stringify(filterValue),
		headers: {
			"Access-Control-Allow-Origin": "*",
			"Content-Type": "application/json",
		},
	})
	const body: ITicket[] = await response.json()
	return body
}

export const fetchTicketsByApi = async (root_id: string): Promise<ITicket[]> => {
	const response = await fetch(API_URL + "/tickets/root/" + root_id, {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({}), // TODO: add filters
	})
	const body: ITicket[] = await response.json()
	return body
}

export const fetchUsersTickets = async (): Promise<ITicket[]> => {
	const user = get_user_id()
	const response = await fetch(API_URL + "/users/" + user + "/tickets", {
		method: "GET",
		headers: {
			"Content-Type": "application/json",
		},
	})
	const body: ITicket[] = await response.json()
	return body
}

export const subscRibeToTickets = async (ticketId: string) => {
	const user = get_user_id()
	console.log(user)
	const response = await fetch(API_URL + "/users/" + user + "/subscribe/" + ticketId, {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
	})
	return response
}

export const unsubscRibeToTickets = async (ticketId: string) => {
	const user = get_user_id()
	const response = await fetch(API_URL + "/users/" + user + "/subscribe/" + ticketId, {
		method: "DELETE",
		headers: {
			"Content-Type": "application/json",
		},
	})
	return response
}

export interface IUpdateTicket {
	status?: States
	header: string
	description: string
}


export const createTicket = async(ticket: IUpdateTicket) => {
	ticket.status = States.NEW
	const response = await fetch(API_URL + "/tickets", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify(ticket)
	})
	return response
}

export const fetchTicketMeetingNotes = async (ticketId: string) => {
	const response = await fetch(API_URL + "/update/get/" + ticketId, {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({}),
	})
	const body: ITicketComment[] = await response.json()
	return body
}
