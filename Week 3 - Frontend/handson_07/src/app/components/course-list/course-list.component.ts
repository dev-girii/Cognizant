import { Component, OnInit, OnDestroy } from '@angular/core';
import { CourseService } from '../../services/course.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-course-list',
  templateUrl: './course-list.component.html',
  styleUrl: './course-list.component.css'
})
export class CourseListComponent implements OnInit, OnDestroy {
  courses: any[] = [];
  loading: boolean = true;
  searchTerm: string = '';
  private subscription?: Subscription;

  constructor(private courseService: CourseService) {}

  ngOnInit(): void {
    const initialCourses = [
      { name: "Introduction to Computer Science", code: "CS101", credits: 4, grade: "A" },
      { name: "Web Design & Development", code: "WEB102", credits: 3, grade: "B+" },
      { name: "Database Management Systems", code: "DB103", credits: 4, grade: "A-" },
      { name: "Software Engineering", code: "SE201", credits: 3, grade: "B" },
      { name: "Mobile App Development", code: "MOB202", credits: 4, grade: "A" }
    ];

    this.loading = true;
    this.subscription = this.courseService.getCourses().subscribe({
      next: (data) => {
        this.courses = data.map((post, idx) => {
          const fallback = initialCourses[idx] || {
            name: post.title,
            code: `CS-${100 + post.id}`,
            credits: 3,
            grade: 'A'
          };
          return {
            id: post.id,
            name: fallback.name,
            code: fallback.code,
            credits: fallback.credits,
            grade: fallback.grade,
            description: post.body
          };
        });
        this.loading = false;
      },
      error: (err) => {
        console.error('Error loading courses:', err);
        this.loading = false;
      }
    });
  }

  ngOnDestroy(): void {
    if (this.subscription) {
      this.subscription.unsubscribe();
    }
  }

  getFilteredCourses() {
    const term = this.searchTerm.trim().toLowerCase();
    if (!term) {
      return this.courses;
    }
    return this.courses.filter(course => 
      course.name.toLowerCase().includes(term) || 
      course.code.toLowerCase().includes(term)
    );
  }
}
