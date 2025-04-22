import { Task } from "./task/task";

export interface AdvocacyProgram {
    brand?: string;
    total_sales_attributed: number;
    tasks_completed: Task[];
}