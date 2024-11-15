import { API_URL } from "./common"

export interface IApi {
	id?: string
	title: string
	description: string
	status: string
	created_at?: string
	updated_at?: string
	update_summary?: string
	version?: string
	next_release?: string
}

export const fetchApis = async (): Promise<IApi[]> => {
	const response = await fetch(API_URL + "/apis", {
		method: "GET",
		headers: {
			"Access-Control-Allow-Origin": "*",
		},
	})
	const body: IApi[] = await response.json()
	return body
}
