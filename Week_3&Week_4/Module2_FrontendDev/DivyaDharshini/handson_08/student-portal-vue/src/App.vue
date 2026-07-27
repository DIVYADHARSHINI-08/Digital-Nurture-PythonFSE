<template>
  <div>

    <Header />

    <nav class="navbar">
      <div class="nav-links">
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/courses">Courses</RouterLink>
        <RouterLink to="/profile">Profile</RouterLink>
      </div>

      <div class="enrolled-count">
        Enrolled Courses: {{ store.enrolledCourses.length }}
      </div>
    </nav>

    <RouterView />

  </div>
</template>

<script setup>
import Header from './components/Header.vue'
import { RouterLink, RouterView } from 'vue-router'

import { useEnrollmentStore } from './stores/enrollment'

const store = useEnrollmentStore()
</script>

<style>
body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
  background: #f5f5f5;
}

.nav {
  background: #333;
  padding: 12px;
}

.nav a {
  color: white;
  text-decoration: none;
  margin-right: 20px;
  font-weight: bold;
}

.nav a:hover {
  color: gold;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #333;
  padding: 12px 20px;
}

.nav-links {
  display: flex;
  gap: 20px;
}

.nav-links a {
  color: white;
  text-decoration: none;
  font-weight: bold;
}

.enrolled-count {
  color: white;
  font-weight: bold;
}
</style>