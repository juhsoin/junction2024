export interface IFilter {
    id?: string;
    status?: string;
    created_after?: number;
    updated_after?: number;
    created_before?: number;
    updated_before?: number;
    categories?: string;
    state?: EStates;
    root?: string;
}

export enum EStates {
    NEW = 1,
    CLARIFICATION = 2,
    RECOMMENDATION = 3,
    WIP = 4,
    READY = 5,
    REJECTED = 6
}