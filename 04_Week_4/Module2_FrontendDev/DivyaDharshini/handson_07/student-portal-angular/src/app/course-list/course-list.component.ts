import { Component, OnInit } from '@angular/core';
import { CourseCardComponent } from '../course-card/course-card.component';

import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { CourseService } from '../course.service';

@Component({
  selector: 'app-course-list',
  standalone: true,
  imports: [
  CommonModule,
  FormsModule,
  CourseCardComponent
  ],
  templateUrl: './course-list.component.html',
  styleUrl: './course-list.component.css',
})

export class CourseListComponent implements OnInit {

  constructor(private courseService: CourseService) {}

  ngOnInit(): void {

  this.loading = true;

  this.courseService.getCourses().subscribe(data => {

    this.courses = data;

    this.loading = false;

  });

}

  searchTerm: string = '';

  loading = false;

  courses: any[] = [];

  /*
  courses = [

    {
      name: "React",
      code: "CS101",
      credits: 4,
      grade: "A"
    },

    {
      name: "Angular",
      code: "CS102",
      credits: 3,
      grade: "A+"
    },

    {
      name: "Java",
      code: "CS103",
      credits: 4,
      grade: "B+"
    }

  ];
  */

  get filteredCourses() {
  return this.courses.filter(course =>
    course.name.toLowerCase().includes(this.searchTerm.toLowerCase())
  );
}

}