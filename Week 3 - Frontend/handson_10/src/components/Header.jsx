import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';

function Header(props) {
  const enrolledCourses = useSelector((state) => state.enrollment.enrolledCourses);

  return (
    <header>
      <div className="logo">
        <span className="logo-icon">🎓</span>
        <span className="logo-text">{props.siteName || "Student Portal"}</span>
      </div>
      <div className="hamburger">☰</div>
      <nav>
        <ul>
          <li>
            <NavLink to="/" end className={({ isActive }) => (isActive ? 'active' : '')}>
              Home
            </NavLink>
          </li>
          <li>
            <NavLink to="/courses" className={({ isActive }) => (isActive ? 'active' : '')}>
              Courses
            </NavLink>
          </li>
          <li>
            <NavLink to="/profile" className={({ isActive }) => (isActive ? 'active' : '')}>
              Profile
            </NavLink>
          </li>
          {enrolledCourses.length > 0 && (
            <li className="enrolled-indicator">
              <span className="enrolled-badge">Enrolled: {enrolledCourses.length}</span>
            </li>
          )}
        </ul>
      </nav>
    </header>
  );
}

export default Header;
