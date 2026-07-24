import React from 'react';

function Header(props) {
  return (
    <header>
      <div className="logo">
        <span className="logo-icon">🎓</span>
        <span className="logo-text">{props.siteName}</span>
      </div>
      <div className="hamburger">☰</div>
      <nav>
        <ul>
          <li><a href="#" className="active">Home</a></li>
          <li><a href="#courses">Courses</a></li>
          <li><a href="#">Profile</a></li>
          {props.enrolledCount !== undefined && (
            <li className="enrolled-indicator">
              <span className="enrolled-badge">Enrolled: {props.enrolledCount}</span>
            </li>
          )}
        </ul>
      </nav>
    </header>
  );
}

export default Header;
