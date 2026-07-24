import apiClient from './apiClient';

export const getAllCourses = async (): Promise<any[]> => {
  return await apiClient.get<any[], any[]>('/posts');
};

export const getCourseById = async (id: number): Promise<any> => {
  return await apiClient.get<any, any>(`/posts/${id}`);
};

export const enrollStudent = async (
  studentId: number,
  courseId: number
): Promise<any> => {
  return await apiClient.post<any, any>('/posts', {
    studentId,
    courseId,
    status: 'Enrolled'
  });
};