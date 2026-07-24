import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useEnrollmentStore = defineStore('enrollment', () => {
  const enrolledCourses = ref([])

  const totalCredits = computed(() => {
    return enrolledCourses.value.reduce((total, course) => total + course.credits, 0)
  })

  function enroll(course) {
    const exists = enrolledCourses.value.some(c => c.id === course.id)
    if (!exists) {
      enrolledCourses.value.push(course)
      console.log(`Enrolled in course: ${course.name}`)
    }
  }

  function unenroll(courseId) {
    enrolledCourses.value = enrolledCourses.value.filter(c => c.id !== courseId)
    console.log(`Unenrolled from course ID: ${courseId}`)
  }

  return { enrolledCourses, totalCredits, enroll, unenroll }
})
