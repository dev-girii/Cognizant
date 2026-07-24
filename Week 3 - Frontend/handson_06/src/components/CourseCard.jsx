import React from 'react';
import { Link } from 'react-router-dom';

function CourseCard({ id, name, code, credits, grade, description, onEnroll, isEnrolled }) {
  return (
    <article className="course-card">
      <div className="course-header">
        <h3>{name}</h3>
        <span className="course-tag">{code}</span>
      </div>
      <p>{description}</p>
      <div className="course-footer" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', width: '100%', marginTop: 'auto', gap: '0.5rem', flexWrap: 'wrap' }}>
        <span className="credits">Credits: {credits}</span>
        <div style={{ display: 'flex', gap: '0.5rem', alignItems: 'center' }}>
          <Link
            to={`/courses/${id}`}
            style={{
              textDecoration: 'none',
              color: 'var(--accent-color)',
              fontSize: '0.8rem',
              fontWeight: '600',
              border: '1px solid var(--accent-color)',
              padding: '0.4rem 0.8rem',
              borderRadius: '6px',
              transition: 'all 0.15s ease-in-out'
            }}
            onMouseEnter={(e) => {
              e.target.style.backgroundColor = 'var(--accent-light)';
            }}
            onMouseLeave={(e) => {
              e.target.style.backgroundColor = 'transparent';
            }}
          >
            Details
          </Link>
          <button
            type="button"
            className="btn-primary"
            onClick={onEnroll}
            disabled={isEnrolled}
            style={
              isEnrolled
                ? { backgroundColor: '#cbd5e1', color: '#64748b', border: '1px solid #cbd5e1', cursor: 'not-allowed', padding: '0.4rem 0.8rem', fontSize: '0.8rem', height: '100%' }
                : { padding: '0.4rem 0.8rem', fontSize: '0.8rem', height: '100%' }
            }
          >
            {isEnrolled ? 'Enrolled' : 'Enroll'}
          </button>
        </div>
      </div>
    </article>
  );
}

export default CourseCard;
