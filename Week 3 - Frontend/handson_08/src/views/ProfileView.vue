<template>
  <div style="display: flex; flex-direction: column; gap: 3rem; padding: 2rem 0;">
    <!-- Profile Edit Section -->
    <section>
      <div class="section-header">
        <h2>Student Profile</h2>
        <div class="section-underline"></div>
      </div>
      
      <form 
        style="max-width: 500px; margin: 0 auto; background-color: var(--bg-white); padding: 2rem; border-radius: 8px; border: 1px solid var(--border-subtle); box-shadow: 0 2px 4px rgba(0,0,0,0.02);"
        @submit.prevent="onSubmit"
      >
        <div style="margin-bottom: 1.25rem; display: flex; flex-direction: column; gap: 0.5rem; text-align: left;">
          <label style="font-size: 0.9rem; font-weight: 600; color: var(--text-dark);">Name</label>
          <input
            type="text"
            v-model="profile.name"
            style="padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-color); font-size: 0.95rem; width: 100%; box-sizing: border-box;"
          />
        </div>

        <div style="margin-bottom: 1.25rem; display: flex; flex-direction: column; gap: 0.5rem; text-align: left;">
          <label style="font-size: 0.9rem; font-weight: 600; color: var(--text-dark);">Email</label>
          <input
            type="email"
            v-model="profile.email"
            style="padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-color); font-size: 0.95rem; width: 100%; box-sizing: border-box;"
          />
        </div>

        <div style="margin-bottom: 1.25rem; display: flex; flex-direction: column; gap: 0.5rem; text-align: left;">
          <label style="font-size: 0.9rem; font-weight: 600; color: var(--text-dark);">Semester</label>
          <input
            type="number"
            v-model="profile.semester"
            style="padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-color); font-size: 0.95rem; width: 100%; box-sizing: border-box;"
          />
        </div>

        <button type="submit" class="btn-primary" style="width: 100%; padding: 0.75rem;">
          Save Changes
        </button>

        <div 
          style="margin-top: 1.5rem; padding: 0.75rem; background-color: var(--accent-light); border: 1px dashed rgba(29, 78, 216, 0.3); border-radius: 6px; font-size: 0.9rem; color: var(--accent-color); font-weight: 500; text-align: center; box-sizing: border-box;"
        >
          State Live Preview: {{ profile.name }} ({{ profile.email }}) - Semester {{ profile.semester }}
        </div>
      </form>
    </section>

    <!-- Enrolled Courses Section -->
    <section style="border-top: 1px solid var(--border-subtle); padding-top: 3rem;">
      <div class="section-header">
        <h2>Enrolled Courses</h2>
        <div class="section-underline"></div>
      </div>

      <div style="max-width: 800px; margin: 0 auto;">
        <div v-if="store.enrolledCourses.length > 0" style="display: flex; flex-direction: column; gap: 1rem;">
          <div 
            v-for="course in store.enrolledCourses" 
            :key="course.id"
            style="display: flex; justify-content: space-between; align-items: center; background-color: var(--bg-white); border: 1px solid var(--border-subtle); padding: 1.25rem; border-radius: 8px; text-align: left; box-shadow: 0 1px 3px rgba(0,0,0,0.01);"
          >
            <div>
              <h4 style="font-size: 1.05rem; font-weight: 600; color: var(--text-dark); margin-bottom: 0.25rem;">
                {{ course.name }}
              </h4>
              <div style="display: flex; gap: 0.75rem; align-items: center;">
                <span class="course-tag" style="font-size: 0.65rem; padding: 0.15rem 0.4rem;">{{ course.code }}</span>
                <span style="font-size: 0.8rem; color: var(--text-muted);">Credits: {{ course.credits }}</span>
                <span style="font-size: 0.8rem; color: var(--text-muted);">Grade: {{ course.grade }}</span>
              </div>
            </div>
            
            <button 
              type="button" 
              class="btn-primary" 
              style="background-color: #ef4444; color: #ffffff; padding: 0.5rem 1rem; font-size: 0.8rem; border: none; border-radius: 6px; cursor: pointer;"
              @click="store.unenroll(course.id)"
            >
              Remove
            </button>
          </div>

          <!-- Summary Credits Bar -->
          <div style="margin-top: 1.5rem; display: flex; justify-content: space-between; align-items: center; padding: 1rem 1.25rem; background-color: var(--bg-white); border: 1px solid var(--border-subtle); border-radius: 8px;">
            <span style="font-size: 1rem; font-weight: 600; color: var(--text-dark);">Total Enrolled Courses: {{ store.enrolledCourses.length }}</span>
            <span style="font-size: 1.05rem; font-weight: 700; color: var(--accent-color);">Total Credits: {{ store.totalCredits }}</span>
          </div>
        </div>

        <div v-else style="text-align: center; color: var(--text-muted); padding: 3rem 0; border: 1px dashed var(--border-color); border-radius: 8px; background-color: var(--bg-white);">
          <span style="font-size: 2.5rem; display: block; margin-bottom: 0.75rem;">📚</span>
          <p style="font-size: 0.95rem; font-weight: 500; margin-bottom: 1rem;">No courses enrolled yet.</p>
          <RouterLink to="/courses" class="btn-primary" style="font-size: 0.85rem; padding: 0.5rem 1.25rem;">
            Explore Catalogue
          </RouterLink>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { reactive } from 'vue'
import { RouterLink } from 'vue-router'
import { useEnrollmentStore } from '../stores/enrollment'

const profile = reactive({
  name: 'Sanjay Gupta',
  email: 'sanjay.gupta@example.com',
  semester: 6
})

const store = useEnrollmentStore()

const onSubmit = () => {
  console.log('Profile saved:', profile)
}
</script>

<style scoped>
</style>
