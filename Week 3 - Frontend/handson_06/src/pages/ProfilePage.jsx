import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Link } from 'react-router-dom';
import StudentProfile from '../components/StudentProfile';
import { unenroll } from '../redux/enrollmentSlice';

function ProfilePage() {
  const enrolledCourses = useSelector((state) => state.enrollment.enrolledCourses);
  const dispatch = useDispatch();

  const handleRemove = (courseId) => {
    dispatch(unenroll(courseId));
  };

  return (
    <div className="profile-page-container">
      {/* Student Profile Form */}
      <StudentProfile />

      {/* Enrolled Courses List */}
      <section id="enrolled-courses" style={{ padding: '2.5rem 0', borderTop: '1px solid var(--border-subtle)', marginTop: '2rem' }}>
        <div className="section-header">
          <h2>My Enrolled Courses</h2>
          <div className="section-underline"></div>
        </div>

        <div style={{ maxWidth: '600px', margin: '0 auto' }}>
          {enrolledCourses.length > 0 ? (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
              {enrolledCourses.map((course) => (
                <div
                  key={course.id}
                  style={{
                    display: 'flex',
                    justifyContent: 'space-between',
                    alignItems: 'center',
                    backgroundColor: 'var(--bg-white)',
                    border: '1px solid var(--border-subtle)',
                    padding: '1.25rem',
                    borderRadius: '8px',
                    boxShadow: '0 1px 3px rgba(0, 0, 0, 0.01)'
                  }}
                >
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '0.25rem', textAlign: 'left' }}>
                    <span style={{ fontWeight: '700', fontSize: '1.05rem', color: 'var(--text-dark)' }}>{course.name}</span>
                    <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>{course.code} • {course.credits} Credits</span>
                  </div>
                  <button
                    type="button"
                    onClick={() => handleRemove(course.id)}
                    style={{
                      backgroundColor: 'transparent',
                      border: '1px solid #ef4444',
                      color: '#ef4444',
                      padding: '0.4rem 0.8rem',
                      borderRadius: '6px',
                      cursor: 'pointer',
                      fontSize: '0.85rem',
                      fontWeight: '600',
                      transition: 'all 0.15s ease-in-out'
                    }}
                    onMouseEnter={(e) => {
                      e.target.style.backgroundColor = '#ef4444';
                      e.target.style.color = '#ffffff';
                    }}
                    onMouseLeave={(e) => {
                      e.target.style.backgroundColor = 'transparent';
                      e.target.style.color = '#ef4444';
                    }}
                  >
                    Remove
                  </button>
                </div>
              ))}
            </div>
          ) : (
            <div style={{ textAlign: 'center', color: '#64748b', padding: '2rem', border: '1px dashed var(--border-color)', borderRadius: '8px' }}>
              No courses enrolled yet. Go to the <Link to="/courses" style={{ color: 'var(--accent-color)', fontWeight: '600', textDecoration: 'none' }}>Courses</Link> tab to enroll.
            </div>
          )}
        </div>
      </section>
    </div>
  );
}

export default ProfilePage;
