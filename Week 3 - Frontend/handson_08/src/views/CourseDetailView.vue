<template>
  <div style="max-width: 600px; margin: 0 auto; padding: 2rem 0;">
    <div class="section-header">
      <h2>Course Details</h2>
      <div class="section-underline"></div>
    </div>

    <div v-if="course" class="course-card" style="padding: 2rem; border-radius: 12px; min-height: auto; gap: 1.5rem; text-align: left;">
      <div class="course-header" style="align-items: center;">
        <h3 style="font-size: 1.4rem; font-weight: 700; color: var(--text-dark);">{{ course.name }}</h3>
        <span class="course-tag" style="font-size: 0.8rem; padding: 0.3rem 0.6rem;">{{ course.code }}</span>
      </div>
      
      <p style="font-size: 0.95rem; line-height: 1.6; color: var(--text-muted); margin-bottom: 1.5rem;">
        {{ course.description }}
      </p>

      <div style="display: flex; gap: 1.5rem; border-bottom: 1px solid var(--border-subtle); padding-bottom: 1.5rem; margin-bottom: 1.5rem;">
        <div style="display: flex; flex-direction: column;">
          <span style="font-size: 0.8rem; color: var(--text-muted); font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px;">Credits</span>
          <span style="font-size: 1.1rem; font-weight: 700; color: var(--text-dark);">{{ course.credits }} Credits</span>
        </div>
        <div style="display: flex; flex-direction: column;">
          <span style="font-size: 0.8rem; color: var(--text-muted); font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px;">Expected Grade</span>
          <span style="font-size: 1.1rem; font-weight: 700; color: var(--accent-color);">{{ course.grade }}</span>
        </div>
      </div>

      <div style="display: flex; gap: 1rem; width: 100%;">
        <button type="button" @click="goBack" class="btn-primary" style="flex: 1; background-color: transparent; color: var(--accent-color); border: 1px solid var(--accent-color);">
          Back to Courses
        </button>
        <button type="button" @click="enroll" class="btn-primary" style="flex: 1;">
          Enroll Course
        </button>
      </div>
    </div>

    <div v-else style="text-align: center; color: var(--text-muted); padding: 3rem 0;">
      Course not found.
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useEnrollmentStore } from '../stores/enrollment'

const route = useRoute()
const router = useRouter()
const store = useEnrollmentStore()
const course = ref(null)

const courses = [
  { 
    id: 1, 
    name: "Introduction to Computer Science", 
    code: "CS101", 
    credits: 4, 
    grade: "A",
    description: "Learn the foundational concepts of programming, algorithms, data structures, and computational thinking. Perfect for aspiring software developers."
  },
  { 
    id: 2, 
    name: "Web Design & Development", 
    code: "WEB102", 
    credits: 3, 
    grade: "B+",
    description: "Master semantic HTML5, modern CSS layouts (Flexbox/Grid), responsive design, and dynamic Javascript interfaces to build interactive web apps."
  },
  { 
    id: 3, 
    name: "Database Management Systems", 
    code: "DB103", 
    credits: 4, 
    grade: "A-",
    description: "Dive deep into relational database design, schema normalization, structured query language (SQL), transaction control, and performance indexing."
  },
  { 
    id: 4, 
    name: "Software Engineering", 
    code: "SE201", 
    credits: 3, 
    grade: "B",
    description: "Study the software lifecycle, requirements gathering, design patterns, testing methodologies, and agile project management practices."
  },
  { 
    id: 5, 
    name: "Mobile App Development", 
    code: "MOB202", 
    credits: 4, 
    grade: "A",
    description: "Create cross-platform mobile experiences. Learn state management, native APIs, local storage, deployment pipelines, and mobile UX design."
  }
]

onMounted(() => {
  const courseId = Number(route.params.id)
  const found = courses.find(c => c.id === courseId)
  if (found) {
    course.value = found
  }
})

const goBack = () => {
  router.push('/courses')
}

const enroll = () => {
  if (course.value) {
    store.enroll(course.value)
  }
  router.push('/profile')
}
</script>

<style scoped>
</style>
