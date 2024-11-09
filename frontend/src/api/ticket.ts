import { States, API_URL } from "./common"

export interface Ticket {
	id: string
	title: string
	description: string
	status: States
	created_at?: string
	updated_at?: string
	root_id: string
	development_proposal_and_clarification?: string
	ball_park_estimate?: string
	impact_on_market?: number // 0 to 3
	priority?: number // 1 to 3
	argumentation_for_proposal?: string
	proposal_impact?: string
	next_steps?: string
	categories?: string
	planned_release_version?: string
}

export interface TicketResponse {
	data: Ticket[]
}

export const fetchTickets = async (): Promise<TicketResponse> => {
	const response = await fetch(API_URL + "/tickets/all", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({})
	})
	const body: TicketResponse = await response.json()
	return body
}

export const fetchTicketsByApi = async (root_id: string): Promise<TicketResponse> => {
	const response = await fetch(API_URL + "/tickets/root/" + root_id, {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({})
	})
	const body: TicketResponse = await response.json()
	return body
}

export const fetchUsersTickets = async (userId: string): Promise<TicketResponse> => {
	const response = await fetch(API_URL + "/tickets/user/" + userId + "/tickets", {
		method: "GET",
		headers: {
			"Content-Type": "application/json",
		},
	})
	const body: TicketResponse = await response.json()
	return body
}

export const subscRibeToTickets = async (userId: string, ticketId: string) => {
	const response = await fetch(API_URL + "/tickets/user/" + userId + "/subscribe/" + ticketId, {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
	})
	return response
}
