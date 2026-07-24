import React, { useState, useEffect } from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import CourseCard from './components/CourseCard';
import StudentProfile from './components/StudentProfile';
import { initialCourses } from './courses';
import './App.css';

function App() {
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [searchTerm, setSearchTerm] = useState('');
  const [enrolledCourses, setEnrolledCourses] = useState([]);

  // Fetch courses from JSONPlaceholder API on mount
  useEffect(() => {
    fetch('https://jsonplaceholder.typicode.com/posts')
      .then((res) => {
        if (!res.ok) {
          throw new Error(`Failed to fetch data: HTTP status ${res.status}`);
        }
        return res.json();
      })
      .then((data) => {
        // Slice the first 5 posts and map to course-like structures matching previous handson
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
  }, []); // Empty dependency array runs once after initial render (componentDidMount behavior)

  // Log course updates whenever the 'courses' state changes
  useEffect(() => {
    if (courses.length > 0) {
      console.log('Courses updated');
    }
    /*
      Why the dependency array matters:
      - If [courses] is specified, this effect will only run when 'courses' value changes (e.g. after fetch completes).
      - If the dependency array is empty [], it would only run once on component mount.
      - If the dependency array is missing altogether, it would run on every single render, which can lead to
        wasted resources or infinite loops if state changes occur inside the effect.
    */
  }, [courses]);

  const handleEnroll = (course) => {
    if (!enrolledCourses.some((c) => c.id === course.id)) {
      setEnrolledCourses([...enrolledCourses, course]);
    }
  };

  const filteredCourses = courses.filter(
    (course) =>
      course.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      course.code.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="app-container">
      <Header siteName="Student Portal" enrolledCount={enrolledCourses.length} />
      
      <main>
        {/* Hero Section */}
        <section id="hero">
          <div className="hero-content">
            <h1>Welcome to the Student Portal</h1>
            <p>Empowering students with seamless access to academic resources, course listings, schedule management, and grading progress. Dive in and explore your academic journey.</p>
            <button type="button" className="btn-primary" onClick={() => document.getElementById('courses').scrollIntoView({ behavior: 'smooth' })}>
              Explore Courses
            </button>
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

        {/* Profile Section */}
        <StudentProfile />

        {/* Courses Section */}
        <section id="courses">
          <div className="section-header">
            <h2>Featured Courses</h2>
            <div className="section-underline"></div>
          </div>

          {/* Search Controls */}
          <div className="controls-panel">
            <input
              type="text"
              id="search-courses"
              placeholder="Search courses by name or code..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
            />
          </div>

          {/* Conditional Rendering: Loading, Error, or Grid */}
          {loading && (
            <div className="loading-state">Loading courses...</div>
          )}

          {error && (
            <div className="error-container">
              <span className="error-message">Error: {error}</span>
            </div>
          )}

          {!loading && !error && (
            <div className="course-grid">
              {filteredCourses.length > 0 ? (
                filteredCourses.map((course) => {
                  const isEnrolled = enrolledCourses.some((c) => c.id === course.id);
                  return (
                    <CourseCard
                      key={course.id}
                      {...course}
                      isEnrolled={isEnrolled}
                      onEnroll={() => handleEnroll(course)}
                    />
                  );
                })
              ) : (
                <p style={{ gridColumn: '1 / -1', textAlign: 'center', color: '#64748b', padding: '2rem 0' }}>
                  No courses found matching "{searchTerm}"
                </p>
              )}
            </div>
          )}
        </section>
      </main>

      <Footer />
    </div>
  );
}

export default App;
