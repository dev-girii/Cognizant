import { configureStore } from '@reduxjs/toolkit';
import enrollmentReducer from './enrollmentSlice';
import coursesReducer from './coursesSlice';

export const store = configureStore({
  reducer: {
    enrollment: enrollmentReducer,
    courses: coursesReducer
  }
});
