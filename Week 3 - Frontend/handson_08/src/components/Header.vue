<template>
  <header>
    <div class="logo">
      <span class="logo-icon">🎓</span>
      <span class="logo-text">Student Portal</span>
    </div>
    <div class="hamburger">☰</div>
    <nav>
      <ul>
        <li><RouterLink to="/" active-class="active" exact-active-class="active">Home</RouterLink></li>
        <li><RouterLink to="/courses" active-class="active">Courses</RouterLink></li>
        <li>
          <RouterLink to="/profile" active-class="active">
            Profile
            <span v-if="store.enrolledCourses.length > 0" class="badge" style="background-color: var(--accent-color); color: #ffffff; padding: 0.1rem 0.4rem; font-size: 0.75rem; border-radius: 10px; margin-left: 0.25rem;">
              {{ store.enrolledCourses.length }}
            </span>
          </RouterLink>
        </li>
      </ul>
    </nav>
  </header>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()
</script>

<style scoped>
</style>
