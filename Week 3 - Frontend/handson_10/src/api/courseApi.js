import apiClient from './apiClient';
import { initialCourses } from '../courses';

export async function getAllCourses() {
  const posts = await apiClient.get('/posts');
  return posts.slice(0, 5).map((post, idx) => {
    const localCourse = initialCourses[idx] || {
      name: post.title,
      code: `CS-${100 + post.id}`,
      credits: 3,
      grade: 'A',
      description: post.body
    };
    return {
      id: post.id,
      name: localCourse.name,
      code: localCourse.code,
      credits: localCourse.credits,
      grade: localCourse.grade,
      description: localCourse.description
    };
  });
}

export async function getCourseById(id) {
  const post = await apiClient.get(`/posts/${id}`);
  const idx = parseInt(id, 10) - 1;
  const localCourse = initialCourses[idx] || {
    name: post.title,
    code: `CS-${100 + post.id}`,
    credits: 3,
    grade: 'A',
    description: post.body
  };
  return {
    id: post.id,
    name: localCourse.name,
    code: localCourse.code,
    credits: localCourse.credits,
    grade: localCourse.grade,
    description: localCourse.description
  };
}

export async function enrollStudent(studentId, courseId) {
  return await apiClient.post('/posts', { studentId, courseId });
}
