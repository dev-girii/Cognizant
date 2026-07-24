import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-course-card',
  templateUrl: './course-card.component.html',
  styleUrl: './course-card.component.css'
})
export class CourseCardComponent {
  @Input() name: string = '';
  @Input() code: string = '';
  @Input() credits: number = 0;
  @Input() grade: string = '';
  @Input() description: string = '';
}
