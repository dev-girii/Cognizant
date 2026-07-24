import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import HomePage from './pages/HomePage';
import CoursesPage from './pages/CoursesPage';
import CourseDetailPage from './pages/CourseDetailPage';
import ProfilePage from './pages/ProfilePage';
import './App.css';

function App() {
  return (
    <div className="app-container">
      <Header siteName="Student Portal" />
      
      <main>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/courses" element={<CoursesPage />} />
          <Route path="/profile" element={<ProfilePage />} />
          <Route path="/courses/:courseId" element={<CourseDetailPage />} />
        </Routes>
      </main>

      <Footer />
    </div>
  );
}

export default App;
