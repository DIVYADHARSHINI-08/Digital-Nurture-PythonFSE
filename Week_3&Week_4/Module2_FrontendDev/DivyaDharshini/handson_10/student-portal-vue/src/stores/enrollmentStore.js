import { defineStore } from 'pinia';
import { enrollStudent } from '../api/courseApi';

export const useEnrollmentStore = defineStore('enrollment', {
  state: () => ({
    enrolledCourses: [],
    loading: false,
    error: null
  }),

  actions: {
    async fetchAndEnroll(courseId) {
      this.loading = true;
      this.error = null;

      try {
        const response = await enrollStudent(1, courseId);

        this.enrolledCourses.push(response);

      } catch (err) {
        this.error = err.message;
      } finally {
        this.loading = false;
      }
    },

    clearEnrollment() {
      this.$reset();
    }
  }
});