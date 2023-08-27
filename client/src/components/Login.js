import React, { useState } from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import { Navigate } from 'react-router-dom';
import '../CSS/login.css';

const validationSchema = Yup.object().shape({
  email: Yup.string().email('Invalid email address').required('Email is required'),
  password: Yup.string().required('Password is required'),
});

function Login({ onLogin }) {
  const [error, setError] = useState('');
  const [isSuccessful, setIsSuccessful] = useState(false);

  const handleSubmit = async (values, { setSubmitting }) => {
    try {
      const response = await fetch('/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: values.email,
          password: values.password,
        }),
      });
  
      if (!response.ok) {
        const data = await response.json();
        setError(data.message);
        setSubmitting(false);
        return;
      }
  
      const data = await response.json();
      // Assuming the server returns an access token after successful login
      localStorage.setItem('access_token', data.access_token);
      
      // Log the current logged-in user and role
      console.log('Logged-in User:', data.user.username);
      console.log('Role:', data.user.role);
      
      onLogin(data.access_token); // Pass the access token to the parent component (App)
      setIsSuccessful(true); // Set the flag to true to trigger the <Navigate> component
    } catch (error) {
      console.error('Error during login:', error);
      setError('An error occurred during login.');
      setSubmitting(false);
    }
  };
  

  return (
    <div className="login-container">
      <h2>Login</h2>
      <Formik
        initialValues={{
          email: '',
          password: '',
        }}
        validationSchema={validationSchema}
        onSubmit={handleSubmit}
      >
        {({ isSubmitting }) => (
          <Form>
            {/* Display server-side error if present */}
            {error && <div className="error">{error}</div>}
            {/* Use Navigate to redirect after successful login */}
            {isSuccessful && <Navigate to="/" replace />}
            <div className="form-group">
              <label htmlFor="email">Email</label>
              <Field type="email" id="email" name="email" required />
              <ErrorMessage name="email" component="div" className="error" />
            </div>
            <div className="form-group">
              <label htmlFor="password">Password</label>
              <Field type="password" id="password" name="password" required />
              <ErrorMessage name="password" component="div" className="error" />
            </div>
            <button type="submit" disabled={isSubmitting}>
              Login
            </button>
          </Form>
        )}
      </Formik>
    </div>
  );
}

export default Login;
