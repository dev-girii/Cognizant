import React, { useState } from 'react';

function StudentProfile() {
  const [profile, setProfile] = useState({
    name: 'Sanjay Gupta',
    email: 'sanjay.gupta@example.com',
    semester: '6'
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setProfile((prevProfile) => ({
      ...prevProfile,
      [name]: value
    }));
  };

  return (
    <section id="profile" style={{ padding: '2.5rem 0', borderTop: '1px solid var(--border-subtle)' }}>
      <div className="section-header">
        <h2>Student Profile</h2>
        <div className="section-underline"></div>
      </div>
      <form 
        style={{ 
          maxWidth: '500px', 
          margin: '0 auto', 
          backgroundColor: 'var(--bg-white)', 
          padding: '2rem', 
          borderRadius: '8px', 
          border: '1px solid var(--border-subtle)', 
          boxShadow: '0 2px 4px rgba(0,0,0,0.02)' 
        }}
        onSubmit={(e) => e.preventDefault()}
      >
        <div style={{ marginBottom: '1.25rem', display: 'flex', flexDirection: 'column', gap: '0.5rem', textAlign: 'left' }}>
          <label style={{ fontSize: '0.9rem', fontWeight: '600', color: 'var(--text-dark)' }}>Name</label>
          <input
            type="text"
            name="name"
            value={profile.name}
            onChange={handleChange}
            style={{ padding: '0.75rem', borderRadius: '6px', border: '1px solid var(--border-color)', fontSize: '0.95rem' }}
          />
        </div>
        <div style={{ marginBottom: '1.25rem', display: 'flex', flexDirection: 'column', gap: '0.5rem', textAlign: 'left' }}>
          <label style={{ fontSize: '0.9rem', fontWeight: '600', color: 'var(--text-dark)' }}>Email</label>
          <input
            type="email"
            name="email"
            value={profile.email}
            onChange={handleChange}
            style={{ padding: '0.75rem', borderRadius: '6px', border: '1px solid var(--border-color)', fontSize: '0.95rem' }}
          />
        </div>
        <div style={{ marginBottom: '1.25rem', display: 'flex', flexDirection: 'column', gap: '0.5rem', textAlign: 'left' }}>
          <label style={{ fontSize: '0.9rem', fontWeight: '600', color: 'var(--text-dark)' }}>Semester</label>
          <input
            type="number"
            name="semester"
            value={profile.semester}
            onChange={handleChange}
            style={{ padding: '0.75rem', borderRadius: '6px', border: '1px solid var(--border-color)', fontSize: '0.95rem' }}
          />
        </div>
        <div 
          style={{ 
            marginTop: '1.5rem', 
            padding: '0.75rem', 
            backgroundColor: 'var(--accent-light)', 
            border: '1px dashed rgba(29, 78, 216, 0.3)', 
            borderRadius: '6px', 
            fontSize: '0.9rem', 
            color: 'var(--accent-color)', 
            fontWeight: '500', 
            textAlign: 'center' 
          }}
        >
          State Live Preview: {profile.name} ({profile.email}) - Semester {profile.semester}
        </div>
      </form>
    </section>
  );
}

export default StudentProfile;
