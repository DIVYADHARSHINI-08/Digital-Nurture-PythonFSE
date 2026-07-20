import apiClient from './apiClient';

export const enrollStudent = async (studentId, courseId) => {
  return await apiClient.post('/posts', {
    studentId,
    courseId,
    status: 'Enrolled'
  });
};