<template>
  <div class="profile-container">

    <h2>Student Profile</h2>

    <h3>Enrolled Courses</h3>

    <div v-if="store.enrolledCourses.length > 0">

      <div
        v-for="course in store.enrolledCourses"
        :key="course.id"
        class="course-card"
      >
        <h4>{{ course.name }}</h4>

        <p><strong>Code:</strong> {{ course.code }}</p>

        <p><strong>Credits:</strong> {{ course.credits }}</p>

        <p><strong>Grade:</strong> {{ course.grade }}</p>
      </div>

      <h3>Total Credits: {{ store.totalCredits }}</h3>

    </div>

    <div v-else>
      <p>No courses enrolled yet.</p>
    </div>

  </div>
</template>

<script setup>
import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()
</script>

<style scoped>
.profile-container {
  padding: 20px;
}

.course-card {
  background: white;
  border-radius: 10px;
  padding: 15px;
  margin: 15px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.15);
}

h2 {
  color: #1976d2;
}

h3 {
  margin-top: 20px;
}
</style>