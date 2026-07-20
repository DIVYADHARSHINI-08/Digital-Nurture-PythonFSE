import { Component, OnInit } from '@angular/core';
import { getAllCourses } from './api/courseApi';

@Component({
  selector: 'app-root',
  standalone: true,
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App implements OnInit {

  courses: any[] = [];

  async ngOnInit() {
  try {
    this.courses = await getAllCourses();
    console.log('Courses:', this.courses);
  } catch (error) {
    console.error('API Error:', error);
  }
}

/*ngOnInit() {
  throw new Error('Test Global Error');
}*/

}