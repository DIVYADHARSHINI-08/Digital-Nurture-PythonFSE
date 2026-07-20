import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'https://jsonplaceholder.typicode.com',
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json'
  }
});

// Request Interceptor
apiClient.interceptors.request.use(
  (config) => {
    const mockToken = 'Bearer mock-token-12345';

    config.headers.Authorization = mockToken;

    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response Interceptor
apiClient.interceptors.response.use(
  (response) => {
    return response.data;
  },
  (error) => {
    const standardError = {
      message:
        error.response?.data?.message ||
        error.message ||
        'Something went wrong',

      statusCode:
        error.response?.status || 500
    };

    return Promise.reject(standardError);
  }
);

export default apiClient;