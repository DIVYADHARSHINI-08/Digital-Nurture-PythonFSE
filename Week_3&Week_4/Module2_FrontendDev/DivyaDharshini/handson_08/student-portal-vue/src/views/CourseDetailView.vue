<template>
  <div class="container">

    <h2>Course Detail</h2>

    <div v-if="course">
      <p><strong>Name:</strong> {{ course.name }}</p>
      <p><strong>Code:</strong> {{ course.code }}</p>
      <p><strong>Credits:</strong> {{ course.credits }}</p>
      <p><strong>Grade:</strong> {{ course.grade }}</p>

      <button @click="enrollCourse">
         Enroll
      </button>
    </div>

    <div v-else>
      <p>Course not found.</p>
    </div>

  </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()

const router = useRouter()

const courses = [
  {
    id: 1,
    name: 'React',
    code: 'CS101',
    credits: 4,
    grade: 'A'
  },
  {
    id: 2,
    name: 'Angular',
    code: 'CS102',
    credits: 3,
    grade: 'A+'
  },
  {
    id: 3,
    name: 'Vue',
    code: 'CS103',
    credits: 4,
    grade: 'A'
  },
  {
    id: 4,
    name: 'Java',
    code: 'CS104',
    credits: 3,
    grade: 'B+'
  },
  {
    id: 5,
    name: 'Python',
    code: 'CS105',
    credits: 4,
    grade: 'A+'
  }
]

const course = courses.find(
  c => c.id === Number(route.params.id)
)

function enrollCourse() {
  router.push('/profile')
}

</script>

<style scoped>
.container{
    padding:20px;
}

button{
    margin-top:15px;
    padding:10px 20px;
    background:#1976d2;
    color:white;
    border:none;
    border-radius:5px;
    cursor:pointer;
}

button:hover{
    background:#0d47a1;
}

</style>