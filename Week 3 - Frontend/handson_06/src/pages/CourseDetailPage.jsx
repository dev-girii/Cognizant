import React, { useContext } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import { CourseContext } from '../context/CourseContext';
import { enroll } from '../redux/enrollmentSlice';

function CourseDetailPage() {
  const { courseId } = useParams();
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const { courses, loading, error } = useContext(CourseContext);
  const enrolledCourses = useSelector((state) => state.enrollment.enrolledCourses);

  // Safely find the course matching courseId
  const course = courses.find((c) => c.id === parseInt(courseId, 10));
  const isEnrolled = course ? enrolledCourses.some((c) => c.id === course.id) : false;

  const handleEnroll = () => {
    if (course) {
      dispatch(enroll(course));
      navigate('/profile');
    }
  };

  if (loading) {
    return <div className="loading-state">Loading course details...</div>;
  }

  if (error || !course) {
    return (
      <div className="error-container" style={{ textAlign: 'center', padding: '2rem' }}>
        <h3>Course Not Found</h3>
        <p style={{ color: 'var(--text-muted)', margin: '1rem 0' }}>
          {error || `No course found with ID "${courseId}"`}
        </p>
        <Link to="/courses" className="btn-primary" style={{ textDecoration: 'none' }}>
          Back to Courses
        </Link>
      </div>
    );
  }

  return (
    <div className="course-detail-container" style={{ maxWidth: '800px', margin: '0 auto', padding: '2rem' }}>
      <Link to="/courses" className="back-link" style={{ textDecoration: 'none', color: 'var(--accent-color)', fontWeight: '600', display: 'inline-flex', alignItems: 'center', gap: '0.5rem', marginBottom: '1.5rem' }}>
        ← Back to Courses
      </Link>
      <div className="detail-card" style={{ backgroundColor: 'var(--bg-white)', border: '1px solid var(--border-subtle)', borderRadius: '12px', padding: '2.5rem', boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03)' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem', flexWrap: 'wrap', gap: '1rem' }}>
          <h1 style={{ fontSize: '2rem', fontWeight: '700', color: 'var(--text-dark)' }}>{course.name}</h1>
          <span className="course-tag" style={{ fontSize: '0.9rem', padding: '0.3rem 0.8rem' }}>{course.code}</span>
        </div>
        <p style={{ fontSize: '1.1rem', color: 'var(--text-muted)', lineHeight: '1.7', marginBottom: '2rem' }}>
          {course.description}
        </p>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderTop: '1px solid var(--border-subtle)', paddingTop: '1.5rem', flexWrap: 'wrap', gap: '1rem' }}>
          <div style={{ display: 'flex', gap: '1.5rem' }}>
            <span className="credits" style={{ fontSize: '0.95rem', padding: '0.4rem 0.8rem' }}>Credits: {course.credits}</span>
            <span style={{ fontSize: '0.95rem', padding: '0.4rem 0.8rem', backgroundColor: '#f1f5f9', color: '#475569', borderRadius: '4px', border: '1px solid var(--border-subtle)' }}>Grade: {course.grade}</span>
          </div>
          <button
            type="button"
            className="btn-primary"
            onClick={handleEnroll}
            disabled={isEnrolled}
            style={
              isEnrolled
                ? { backgroundColor: '#cbd5e1', color: '#64748b', border: '1px solid #cbd5e1', cursor: 'not-allowed', padding: '0.75rem 2rem' }
                : { padding: '0.75rem 2rem' }
            }
          >
            {isEnrolled ? 'Enrolled' : 'Enroll Now'}
          </button>
        </div>
      </div>
    </div>
  );
}

export default CourseDetailPage;
