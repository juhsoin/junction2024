import {API_URL} from './common';


export const subscribeUserToTicket = async (userId: string, ticketId: string) => {
    const response = await fetch(
        API_URL + '/tickets/user/' + userId + "/subscribe/" + ticketId, {
        method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
        }
    );
    return response
}