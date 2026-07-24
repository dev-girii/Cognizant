import React, { useState, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import CourseCard from '../components/CourseCard';
import { CourseContext } from '../context/CourseContext';
import { enroll } from '../redux/enrollmentSlice';

function CoursesPage() {
  const { courses, loading, error } = useContext(CourseContext);
  const enrolledCourses = useSelector((state) => state.enrollment.enrolledCourses);
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const [searchTerm, setSearchTerm] = useState('');

  const handleEnroll = (course) => {
    dispatch(enroll(course));
    navigate('/profile');
  };

  const filteredCourses = courses.filter(
    (course) =>
      course.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      course.code.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
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
      {loading && <div className="loading-state">Loading courses...</div>}

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
  );
}

export default CoursesPage;
