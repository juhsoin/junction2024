
import {API_URL} from './common';

export interface ITicket {
    id?: string;
    title: string;
    description: string;
    status: string;
    created_at?: string;
    updated_at?: string;
    root_id: string;
    development_proposal?: string;
    development_clarification?: string;
    ball_park_estimate?: string;
    impact_on_market?: number; // 0 to 3
    priority?: number; // 1 to 3
    argumentation_for_proposal?: string;
    proposal_impact?: string;
    next_steps?: string;
    planned_release?: string;
}

export type ITicketResponse = [ITicket]; 

export const fetchTickets = async (): Promise<ITicketResponse> => {
    const response = await fetch(
        API_URL + '/tickets/all', {
        method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        }
    );
    const body: ITicketResponse  = await response.json()
    return body
}

export const fetchUsersTickets = async (userId: string): Promise<ITicketResponse> => {
    const response = await fetch(
        API_URL + '/tickets/user/' + userId + "/tickets", {
        method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        }
    );
    const body: ITicketResponse  = await response.json()
    return body
}

export const fetchTicket = async (ticketId: string): Promise<ITicket> => {
    const response = await fetch(
        API_URL + '/tickets/' + ticketId, {
        method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        }
    );
    const body: ITicket  = await response.json()
    return body
}

