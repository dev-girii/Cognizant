import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'https://jsonplaceholder.typicode.com',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request Interceptor
apiClient.interceptors.request.use(
  (config) => {
    config.headers.Authorization = 'Bearer mock-token-12345';
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response Interceptor
apiClient.interceptors.response.use(
  (response) => {
    // Return response.data directly
    return response.data;
  },
  (error) => {
    // Catch errors and throw a standardized Error object
    const errorData = {
      message: 'An unexpected error occurred.',
      statusCode: 500,
    };

    if (error.response) {
      errorData.message = error.response.data.message || error.message;
      errorData.statusCode = error.response.status;
    } else if (error.request) {
      errorData.message = 'No response received from the server.';
      errorData.statusCode = 503;
    } else {
      errorData.message = error.message;
    }

    const customError = new Error(errorData.message);
    customError.statusCode = errorData.statusCode;
    
    return Promise.reject(customError);
  }
);

export default apiClient;
