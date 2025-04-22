import { Component, Input } from '@angular/core';
import { Task } from './task';

@Component({
  selector: 'app-task',
  imports: [],
  template: `
    <div class="task-card">
      <h4>{{ task.platform }}</h4>
      <p><strong>Post URL:</strong> <a href="{{ task.post_url }}" target="_blank">{{ task.post_url }}</a></p>
      <p><strong>Likes:</strong> {{ task.likes }}</p>
      <p><strong>Comments:</strong> {{ task.comments }}</p>
      <p><strong>Shares:</strong> {{ task.shares }}</p>
      <p><strong>Reach:</strong> {{ task.reach }}</p>
    </div>
  `,
  styleUrl: './task.component.css',
})
export class TaskComponent {
  @Input() task!: Task;
}
