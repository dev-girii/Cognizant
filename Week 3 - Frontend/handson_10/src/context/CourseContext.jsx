import React, { createContext, useState, useEffect } from 'react';
import { initialCourses } from '../courses';

export const CourseContext = createContext();

export function CourseProvider({ children }) {
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('https://jsonplaceholder.typicode.com/posts')
      .then((res) => {
        if (!res.ok) {
          throw new Error(`Failed to fetch data: HTTP status ${res.status}`);
        }
        return res.json();
      })
      .then((data) => {
        const mappedCourses = data.slice(0, 5).map((post, idx) => {
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
        setCourses(mappedCourses);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  return (
    <CourseContext.Provider value={{ courses, loading, error }}>
      {children}
    </CourseContext.Provider>
  );
}
