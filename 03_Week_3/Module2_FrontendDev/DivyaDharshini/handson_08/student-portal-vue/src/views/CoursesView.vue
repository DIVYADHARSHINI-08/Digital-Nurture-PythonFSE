<template>
  <div class="courses-container">

    <h2>Courses</h2>
    
    <input
  type="text"
  v-model="searchTerm"
  placeholder="Search courses..."
   />


    <CourseCard
  v-for="course in filteredCourses"
  :key="course.id"
  :name="course.name"
  :code="course.code"
  :credits="course.credits"
  :grade="course.grade"
  @enroll="enrollCourse(course)"
  />
  </div>
</template> 

<script setup>
import { ref, onMounted, computed } from 'vue'
import CourseCard from '../components/CourseCard.vue'
import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()

const courses = ref([])
const searchTerm = ref('')

const filteredCourses = computed(() => {
  return courses.value.filter(course =>
    course.name.toLowerCase().includes(searchTerm.value.toLowerCase())
  )
})

function enrollCourse(course) {
  store.enroll(course)
  console.log(store.enrolledCourses)
}

onMounted(() => {
  courses.value = [
    {
      id: 1,
      name: "React",
      code: "CS101",
      credits: 4,
      grade: "A"
    },
    {
      id: 2,
      name: "Angular",
      code: "CS102",
      credits: 3,
      grade: "A+"
    },
    {
      id: 3,
      name: "Vue",
      code: "CS103",
      credits: 4,
      grade: "A"
    },
    {
      id: 4,
      name: "Java",
      code: "CS104",
      credits: 3,
      grade: "B+"
    },
    {
      id: 5,
      name: "Python",
      code: "CS105",
      credits: 4,
      grade: "A+"
    }
  ]
})
</script>

<style scoped>
.courses-container {
  padding: 20px;
}

input {
  width: 100%;
  padding: 10px;
  margin: 15px 0;
  border-radius: 6px;
  border: 1px solid #ccc;
  font-size: 16px;
}
</style>