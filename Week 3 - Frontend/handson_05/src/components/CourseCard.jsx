import React from 'react';

function CourseCard({ id, name, code, credits, grade, description, onEnroll, isEnrolled }) {
  return (
    <article className="course-card">
      <div className="course-header">
        <h3>{name}</h3>
        <span className="course-tag">{code}</span>
      </div>
      <p>{description}</p>
      <div className="course-footer" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', width: '100%', marginTop: 'auto' }}>
        <span className="credits">Credits: {credits}</span>
        <button
          type="button"
          className="btn-primary"
          onClick={onEnroll}
          disabled={isEnrolled}
          style={
            isEnrolled
              ? { backgroundColor: '#cbd5e1', color: '#64748b', border: '1px solid #cbd5e1', cursor: 'not-allowed', padding: '0.4rem 1rem', fontSize: '0.8rem' }
              : { padding: '0.4rem 1rem', fontSize: '0.8rem' }
          }
        >
          {isEnrolled ? 'Enrolled' : 'Enroll'}
        </button>
      </div>
    </article>
  );
}

export default CourseCard;
