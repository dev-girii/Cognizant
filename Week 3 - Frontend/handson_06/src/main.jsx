import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import { Provider } from 'react-redux';
import { store } from './redux/store';
import { EnrollmentProvider } from './context/EnrollmentContext';
import { CourseProvider } from './context/CourseContext';
import './index.css';
import App from './App.jsx';

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Provider store={store}>
      <EnrollmentProvider>
        <CourseProvider>
          <BrowserRouter>
            <App />
          </BrowserRouter>
        </CourseProvider>
      </EnrollmentProvider>
    </Provider>
  </StrictMode>
);
