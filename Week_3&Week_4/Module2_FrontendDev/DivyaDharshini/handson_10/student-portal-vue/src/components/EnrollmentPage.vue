<script setup>
import { storeToRefs } from 'pinia';
import { useEnrollmentStore } from '../stores/enrollmentStore';

const store = useEnrollmentStore();

// Keep reactivity while destructuring
const { enrolledCourses, loading, error } = storeToRefs(store);

// Enroll in Course ID 1
const enroll = () => {
  store.fetchAndEnroll(1);
};

// Reset store
const reset = () => {
  store.clearEnrollment();
};
</script>

<template>
  <div>
    <h1>Course Enrollment</h1>

    <button @click="enroll">Enroll</button>
    <button @click="reset">Reset</button>

    <p v-if="loading">Loading...</p>

    <p v-if="error" style="color:red">
      {{ error }}
    </p>

    <h3>Enrolled Courses</h3>

    <ul>
      <li
        v-for="course in enrolledCourses"
        :key="course.id"
      >
        Course ID: {{ course.courseId }} -
        {{ course.status }}
      </li>
    </ul>
  </div>
</template>