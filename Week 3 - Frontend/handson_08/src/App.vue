<template>
  <div class="app-container">
    <Header />
    
    <main>
      <RouterView />
    </main>

    <footer>
      <div class="footer-content">
        <p>&copy; 2026 Student Portal. All rights reserved.</p>
        <div class="footer-links">
          <a href="#">Privacy Policy</a>
          <a href="#">Terms of Service</a>
          <a href="#">Contact Support</a>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { RouterView } from 'vue-router'
import Header from './components/Header.vue'
</script>

<style scoped>
</style>
