import React from 'react';
import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux';

function HomePage() {
  const enrolledCourses = useSelector((state) => state.enrollment.enrolledCourses);

  return (
    <div className="home-page-container">
      {/* Hero Section */}
      <section id="hero">
        <div className="hero-content">
          <h1>Welcome to the Student Portal</h1>
          <p>Empowering students with seamless access to academic resources, course listings, schedule management, and grading progress. Dive in and explore your academic journey.</p>
          <Link to="/courses" className="btn-primary" style={{ textDecoration: 'none', display: 'inline-block' }}>
            Explore Courses
          </Link>
        </div>
        <div className="hero-glow"></div>
      </section>

      {/* Stats Section */}
      <section id="stats">
        <div className="stat-card">
          <span className="stat-label">Courses Enrolled</span>
          <span className="stat-value">{enrolledCourses.length}</span>
        </div>
        <div className="stat-card">
          <span className="stat-label">GPA</span>
          <span className="stat-value">3.8</span>
        </div>
        <div className="stat-card">
          <span className="stat-label">Semester</span>
          <span className="stat-value">6</span>
        </div>
      </section>
    </div>
  );
}

export default HomePage;
