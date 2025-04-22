import { Component, Input } from '@angular/core';
import { AdvocacyProgram } from './advocacy-program';
import { TaskComponent } from './task/task.component';
import { NgFor, NgIf } from '@angular/common';

@Component({
  selector: 'app-advocacy-program',
  imports: [TaskComponent, NgFor, NgIf],
  template: `
    <div class="advocacy-program-card">
      <h3>{{ advocacyProgram.brand }}</h3>
      <p><strong>Total Sales Attributed:</strong> {{ advocacyProgram.total_sales_attributed }}</p>
      <div *ngIf="advocacyProgram.tasks_completed && advocacyProgram.tasks_completed.length > 0">
        <h4>Tasks</h4>
        <div *ngFor="let task of advocacyProgram.tasks_completed">
          <app-task [task]="task"></app-task>
        </div>
    </div>
  `,
  styleUrl: './advocacy-program.component.css',
})
export class AdvocacyProgramComponent {
  @Input() advocacyProgram!: AdvocacyProgram;
}
