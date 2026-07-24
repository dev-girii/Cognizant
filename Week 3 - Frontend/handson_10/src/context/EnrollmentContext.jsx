import React, { createContext, useState } from 'react';

export const EnrollmentContext = createContext();

export function EnrollmentProvider({ children }) {
  const [enrolledCourses, setEnrolledCourses] = useState([]);

  const enrollCourse = (course) => {
    if (!enrolledCourses.some((c) => c.id === course.id)) {
      setEnrolledCourses((prev) => [...prev, course]);
    }
  };

  const removeCourse = (courseId) => {
    setEnrolledCourses((prev) => prev.filter((course) => course.id !== courseId));
  };

  return (
    <EnrollmentContext.Provider value={{ enrolledCourses, enrollCourse, removeCourse }}>
      {children}
    </EnrollmentContext.Provider>
  );
}
