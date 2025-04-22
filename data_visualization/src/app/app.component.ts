import { Component, OnInit } from '@angular/core';
import { UserComponent } from './user/user.component';
import { User } from './user/user';
import { UserService } from './user/user.service';
import { NgFor } from '@angular/common';

@Component({
  selector: 'app-root',
  imports: [UserComponent, NgFor],
  template: `
    <h1>{{ title }}</h1>
    <li *ngFor="let user of users">
      <app-user [user]=user></app-user>
    </li>
  `,
  styleUrls: ['./app.component.css'],
})
export class AppComponent implements OnInit {

  users: User[] = [];

  constructor(private userService: UserService) { }

  ngOnInit(): void {
    this.getUsers();
  }

  getUsers(): void {
    this.userService.getUsers()
      .subscribe(users => { 
        console.log(users);
        this.users = users 
      });
  }

  title = 'Top Users';
}
