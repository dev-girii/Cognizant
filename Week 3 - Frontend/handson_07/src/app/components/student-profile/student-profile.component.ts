import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'app-student-profile',
  templateUrl: './student-profile.component.html',
  styleUrl: './student-profile.component.css'
})
export class StudentProfileComponent implements OnInit {
  profileForm!: FormGroup;

  ngOnInit(): void {
    this.profileForm = new FormGroup({
      name: new FormControl('Sanjay Gupta', [Validators.required]),
      email: new FormControl('sanjay.gupta@example.com', [Validators.required, Validators.email]),
      semester: new FormControl(6, [
        Validators.required,
        Validators.min(1),
        Validators.max(8)
      ])
    });
  }

  onSubmit(): void {
    if (this.profileForm.valid) {
      console.log('Form Submitted!', this.profileForm.value);
    }
  }

  // Helper getters to check control validation in template markup
  get name() {
    return this.profileForm.get('name');
  }

  get email() {
    return this.profileForm.get('email');
  }

  get semester() {
    return this.profileForm.get('semester');
  }
}
