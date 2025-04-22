import { AdvocacyProgram } from "./advocacy-program/advocacy-program";

export interface User {
    name?: string;
    email?: string;
    instagram_handle?: string;
    tiktok_handle?: string;
    joined_at?: Date;
    advocacy_programs?: AdvocacyProgram[];
}