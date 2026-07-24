<template>
  <div>
    <!-- Hero Section -->
    <section id="hero">
      <div class="hero-content">
        <h1>Welcome to the Student Portal</h1>
        <p>Empowering students with seamless access to academic resources, course listings, schedule management, and grading progress. Dive in and explore your academic journey.</p>
        <RouterLink to="/courses" class="btn-primary">
          Explore Courses
        </RouterLink>
      </div>
      <div class="hero-glow"></div>
    </section>

    <!-- Stats Section -->
    <section id="stats">
      <div class="stat-card">
        <span class="stat-label">Courses Enrolled</span>
        <span class="stat-value">3</span>
      </div>
      <div class="stat-card">
        <span class="stat-label">GPA</span>
        <span class="stat-value">3.8</span>
      </div>
      <div class="stat-card">
        <span class="stat-label">Semester</span>
        <span class="stat-value">6</span>
      </div>
    </section>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
</style>
