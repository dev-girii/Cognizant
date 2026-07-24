<template>
  <div>
    <!-- Courses Catalogue Section -->
    <section id="courses" style="border-top: none; padding-top: 0.5rem;">
      <div class="section-header">
        <h2>Featured Courses</h2>
        <div class="section-underline"></div>
      </div>

      <!-- Search Controls -->
      <div class="controls-panel">
        <input
          type="text"
          id="search-courses"
          placeholder="Search courses by name or code..."
          v-model="searchTerm"
        />
      </div>

      <!-- Course Card Grid -->
      <div class="course-grid" v-if="filteredCourses.length > 0">
        <div
          v-for="course in filteredCourses"
          :key="course.id"
          class="course-card-wrapper"
          style="display: flex; flex-direction: column; align-items: stretch; background-color: var(--bg-white); border: 1px solid var(--border-subtle); border-radius: 8px; overflow: hidden; transition: box-shadow 0.2s;"
        >
          <RouterLink
            :to="'/courses/' + course.id"
            style="text-decoration: none; color: inherit; display: flex; flex-direction: column; flex-grow: 1;"
          >
            <CourseCard
              :name="course.name"
              :code="course.code"
              :credits="course.credits"
              :grade="course.grade"
              :description="course.description"
              style="border: none; box-shadow: none; margin-bottom: 0; flex-grow: 1;"
            />
          </RouterLink>
          <div style="padding: 1rem; border-top: 1px solid var(--border-subtle); background-color: #fafbfd; display: flex; gap: 0.5rem; justify-content: space-between; align-items: center;">
            <button 
              type="button" 
              class="btn-primary" 
              style="font-size: 0.8rem; padding: 0.5rem 1rem; width: 100%;"
              @click.stop.prevent="enrollCourse(course)"
            >
              Enroll Course
            </button>
          </div>
        </div>
      </div>

      <!-- Fallback alert if filtered list is empty -->
      <div v-else style="text-align: center; color: #64748b; padding: 2rem 0; font-weight: 500;">
        No courses found matching "{{ searchTerm }}"
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import CourseCard from '../components/CourseCard.vue'
import { useEnrollmentStore } from '../stores/enrollment'

const courses = ref([])
const searchTerm = ref('')
const store = useEnrollmentStore()

onMounted(() => {
  courses.value = [
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
})

const filteredCourses = computed(() => {
  const term = searchTerm.value.trim().toLowerCase()
  if (!term) {
    return courses.value
  }
  return courses.value.filter(course => 
    course.name.toLowerCase().includes(term) || 
    course.code.toLowerCase().includes(term)
  )
})

const enrollCourse = (course) => {
  store.enroll(course)
}
</script>

<style scoped>
</style>
