import React, { Component } from 'react';

class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    console.error("ErrorBoundary caught an error:", error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div style={{
          padding: '2.5rem',
          textAlign: 'center',
          backgroundColor: '#fff5f5',
          border: '1px solid #feb2b2',
          borderRadius: '12px',
          margin: '3rem auto',
          maxWidth: '600px',
          boxShadow: '0 10px 15px -3px rgba(0, 0, 0, 0.05)'
        }}>
          <span style={{ fontSize: '3rem', display: 'block', marginBottom: '1rem' }} role="img" aria-label="Warning sign">⚠️</span>
          <h2 style={{ color: '#c53030', fontWeight: '700', fontSize: '1.5rem', marginBottom: '0.75rem' }}>
            Application Rendering Error
          </h2>
          <p style={{ color: '#742a2a', fontSize: '0.95rem', lineHeight: '1.6', marginBottom: '1.5rem' }}>
            We apologize for the inconvenience. A critical error was detected in the UI interface:
            <code style={{ display: 'block', backgroundColor: '#fff', border: '1px solid #e2e8f0', padding: '0.75rem', margin: '0.75rem 0', borderRadius: '6px', fontFamily: 'monospace', color: '#e53e3e', overflowX: 'auto', textAlign: 'left' }}>
              {this.state.error && this.state.error.toString()}
            </code>
          </p>
          <button 
            type="button"
            className="btn-primary" 
            onClick={() => window.location.reload()}
            style={{ padding: '0.75rem 2rem', fontSize: '0.95rem' }}
          >
            Reload Interface
          </button>
        </div>
      );
    }

    return this.props.children;
  }
}

export default ErrorBoundary;
