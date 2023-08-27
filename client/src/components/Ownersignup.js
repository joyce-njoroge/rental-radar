import React from 'react';
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
  hashed_password: Yup.string()
    .min(6, 'Password must be at least 6 characters')
    .required('Password is required'),
  confirm_password: Yup.string()
    .required('Confirm Password is required')
    .test('passwords-match', 'Passwords must match', function (value, formikBag) {
      return value === formikBag.parent.hashed_password;
    }),
});

function Tenantsignup() {
  const navigate = useNavigate();

  const handleSubmit = async (values, { setSubmitting }) => {
    if (values.hashed_password !== values.confirm_password) {
      console.error('Passwords do not match.');
      // Handle password mismatch error or display an error message
      return;
    }

    try {
      const response = await fetch('/check_username_and_email', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username: values.username,
          email: values.email,
        }),
      });

      if (!response.ok) {
        throw new Error('Failed to check username and email.');
      }

      const data = await response.json();
      if (data.usernameExists) {
        console.error('Username already exists.');
        setSubmitting(false); 
        return;
      }
      if (data.emailExists) {
        console.error('Email already exists.');
        setSubmitting(false); 
        return;
      }
      // Continue with form submission if email and username are not taken
      const createUserResponse = await fetch('/users', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username: values.username,
          email: values.email,
          password: values.hashed_password,
          role: 'owner',
        }),
      });

      if (!createUserResponse.ok) {
        throw new Error('Failed to create user');
      }

      const createUserData = await createUserResponse.json();
      console.log('User created successfully:', createUserData);
      // #######saves token  to lacal storage 
      localStorage.setItem('access_token', createUserData.access_token);
      navigate('/login'); // takes you to the home page after successful signup
    
    } catch (error) {
      console.error('Error creating user:', error);
    
    }
  };

  return (
    <div className="container">
    <h1 className="h3 mb-3 font-weight-normal">Owner Signup</h1>
    <Formik
      initialValues={{
        username: '',
        email: '',
        hashed_password: '',
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
            <label htmlFor="hashed_password">Password</label>
            <Field type="password" id="hashed_password" name="hashed_password" className="form-control" required />
            <ErrorMessage name="hashed_password" component="div" className="text-danger" />
          </div>
          <div className="form-group">
            <label htmlFor="confirm_password">Confirm Password</label>
            <Field type="password" id="confirm_password" name="confirm_password" className="form-control" required />
            <ErrorMessage name="confirm_password" component="div" className="text-danger" />
          </div>
          <button type="submit" className="btn btn-primary" disabled={isSubmitting}>
            Sign Up
          </button>
        </Form>
      )}
    </Formik>
  </div>
);
}

export default Tenantsignup;
