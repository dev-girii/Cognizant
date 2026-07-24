import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import { Provider } from 'react-redux';
import { store } from './redux/store';
import { EnrollmentProvider } from './context/EnrollmentContext';
import ErrorBoundary from './components/ErrorBoundary';
import './index.css';
import App from './App.jsx';

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <ErrorBoundary>
      <Provider store={store}>
        <EnrollmentProvider>
          <BrowserRouter>
            <App />
          </BrowserRouter>
        </EnrollmentProvider>
      </Provider>
    </ErrorBoundary>
  </StrictMode>
);
