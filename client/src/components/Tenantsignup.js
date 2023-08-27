import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';

const validationSchema = Yup.object().shape({
  username: Yup.string().required('Username is required').test('checkUsername', 'Username already exists.', async function (value) {
    if (!value) return false; 
    try {
      const response = await fetch('/check_username_and_email', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username: value,
        }),
      });
      if (!response.ok) {
        throw new Error('Failed to check username.');
      }
      const data = await response.json();
      return !data.usernameExists;
    } catch (error) {
      console.error('Error checking username:', error);
      return false;
    }
  }),
  email: Yup.string().email('Invalid email address').required('Email is required').test('checkEmail', 'Email already exists.', async function (value) {
    if (!value) return false; // Skip validation if email is empty
    try {
      const response = await fetch('/check_username_and_email', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: value,
        }),
      });
      if (!response.ok) {
        throw new Error('Failed to check email.');
      }
      const data = await response.json();
      return !data.emailExists;
    } catch (error) {
      console.error('Error checking email:', error);
      return false;
    }
  }),
  password: Yup.string()
    .min(6, 'Password must be at least 6 characters')
    .required('Password is required'),
  confirm_password: Yup.string()
    .required('Confirm Password is required')
    .test('passwords-match', 'Passwords must match', function (value, formikBag) {
      return value === formikBag.parent.password;
    }),
});

function Tenantsignup() {
  const navigate = useNavigate();
  const [error, setError] = useState('');

  const handleGoogleSignup = () => {
    // Initialize Google Sign-In with your client ID
    window.gapi.load('auth2', () => {
      window.gapi.auth2.init({
        client_id: '718394920660-ona73bdtqv0u5nduk09hkgmr9q3qrmus.apps.googleusercontent.com',
      }).then(
        // On successful initialization, show the Google Sign-In popup
        () => {
          const auth2 = window.gapi.auth2.getAuthInstance();
          auth2.signIn().then(
            // On successful Google Sign-In, send the user's Google credentials to the backend
            (googleUser) => {
              const id_token = googleUser.getAuthResponse().id_token;
              // Send the id_token to your backend for verification and user creation
              sendGoogleCredentialsToBackend(id_token);
            },
            (error) => {
              console.error('Google Sign-In failed:', error);
              setError('Google Sign-In failed.');
            }
          );
        },
        (error) => {
          console.error('Google Sign-In initialization failed:', error);
          setError('Google Sign-In initialization failed.');
        }
      );
    });
  };

  const sendGoogleCredentialsToBackend = async (id_token) => {
    try {
      // Send the id_token to your backend for verification and user creation
      const response = await fetch('/signup-with-google', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ id_token }),
      });

      if (!response.ok) {
        throw new Error('Failed to signup with Google.');
      }

      const data = await response.json();
      console.log('User created successfully with Google:', data);
      navigate('/login'); // Navigate to the login page after successful signup
    } catch (error) {
      console.error('Error signing up with Google:', error);
      setError('Error signing up with Google.');
    }
  };

  const handleSubmit = async (values, { setSubmitting }) => {
    if (values.password !== values.confirm_password) {
      console.error('Passwords do not match.');
      // Handle password mismatch error or display an error message
      return;
    }

    try {
      // Continue with form submission if email and username are not taken
      const createUserResponse = await fetch('/users', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username: values.username,
          email: values.email,
          password: values.password,
          role: 'tenant',
        }),
      });

      if (!createUserResponse.ok) {
        throw new Error('Failed to create user');
      }

      const createUserData = await createUserResponse.json();
      console.log('User created successfully:', createUserData);
      navigate('/login'); // takes you to the home page after successful signup
    } catch (error) {
      console.error('Error creating user:', error);
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="cont">
      <h1 className="h3 mb-3 font-weight-normal">Tenant Signup</h1>
      <Formik
        initialValues={{
          username: '',
          email: '',
          password: '',
          confirm_password: '',
        }}
        validationSchema={validationSchema}
        onSubmit={handleSubmit}
      >
        {({ isSubmitting }) => (
          <Form>
            <div className="form-group">
              <label htmlFor="username">Full Name</label>
              <Field type="text" id="username" name="username" className="form-control" required />
              <ErrorMessage name="username" component="div" className="text-danger" />
            </div>
            <div className="form-group">
              <label htmlFor="email">Email</label>
              <Field type="email" id="email" name="email" className="form-control" required />
              <ErrorMessage name="email" component="div" className="text-danger" />
            </div>
            <div className="form-group">
              <label htmlFor="password">Password</label>
              <Field type="password" id="password" name="password" className="form-control" required />
              <ErrorMessage name="password" component="div" className="text-danger" />
            </div>
            <div className="form-group">
              <label htmlFor="confirm_password">Confirm Password</label>
              <Field type="password" id="confirm_password" name="confirm_password" className="form-control" required />
              <ErrorMessage name="confirm_password" component="div" className="text-danger" />
            </div>
            <button type="submit" className="btn btn-primary" disabled={isSubmitting}>
              Sign Up
            </button>
            {/* Add a button for Google Sign-In */}
            {/* <button type="button" className="btn btn-danger" onClick={handleGoogleSignup}>
              Sign Up with Google
            </button> */}

            {/* Show any error from Google Sign-In */}
            {error && <div className="text-danger">{error}</div>}

          </Form>
        )}
      </Formik>
    </div>
  );
}

export default Tenantsignup;
