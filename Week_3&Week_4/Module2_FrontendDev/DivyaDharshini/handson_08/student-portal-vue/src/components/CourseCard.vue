<template>
  <div class="course-card">
    <h2>{{ name }}</h2>

    <p><strong>Code:</strong> {{ code }}</p>
    <p><strong>Credits:</strong> {{ credits }}</p>
    <p><strong>Grade:</strong> {{ grade }}</p>

    <button @click="emit('enroll')">
      Enroll
    </button>
  </div>
</template>

<script setup>
defineProps({
  name: String,
  code: String,
  credits: Number,
  grade: String
})

const emit = defineEmits(['enroll'])
</script>

<style scoped>
.course-card {
  background: white;
  border-radius: 10px;
  padding: 20px;
  margin: 15px;
  box-shadow: 0 2px 8px rgba(0,0,0,.15);
}

h2 {
  margin-top: 0;
  color: #1976d2;
}

p {
  margin: 8px 0;
}

button {
  margin-top: 15px;
  padding: 10px 20px;
  background: #1976d2;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background: #1565c0;
}
</style>