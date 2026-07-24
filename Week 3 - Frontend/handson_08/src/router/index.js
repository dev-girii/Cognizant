import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CoursesView from '../views/CoursesView.vue'
import CourseDetailView from '../views/CourseDetailView.vue'
import ProfileView from '../views/ProfileView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/courses',
      name: 'courses',
      component: CoursesView
    },
    {
      path: '/courses/:id',
      name: 'course-detail',
      component: CourseDetailView
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView
    }
  ]
})

// Navigation guard logging route changes
router.beforeEach((to, from, next) => {
  console.log(`Navigating to: ${to.path}`)
  next()
})

export default router
