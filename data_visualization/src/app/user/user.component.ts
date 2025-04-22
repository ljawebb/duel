import { Component, Input } from '@angular/core';
import { AdvocacyProgramComponent } from './advocacy-program/advocacy-program.component';
import { User } from './user';
import { NgFor, NgIf } from '@angular/common';

@Component({
  selector: 'app-user',
  imports: [AdvocacyProgramComponent, NgFor, NgIf],
  template: `
    <div class="user-card">
      <h2>{{ user.name }}</h2>
      <p><strong>Email:</strong> {{ user.email }}</p>
      <p><strong>Instagram Handle:</strong> {{ user.instagram_handle }}</p>
      <p><strong>TikTok Handle:</strong> {{ user.tiktok_handle }}</p>
      <p><strong>Joined:</strong> {{ user.joined_at }}</p>
      <div *ngIf="user.advocacy_programs && user.advocacy_programs.length > 0">
        <h3>Advocacy Programs</h3>
        <div *ngFor="let program of user.advocacy_programs">
          <app-advocacy-program [advocacyProgram]="program"></app-advocacy-program>
      </div>
    </div>
  `,
  styleUrl: './user.component.css',
})
export class UserComponent {
  @Input() user!: User;
}
