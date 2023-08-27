import React from 'react';
import { Route, Navigate } from 'react-router-dom';

function ProtectedRoute({ accessToken, children }) {
  if (!accessToken) {
    return <Navigate to="/login" replace />;
  }

  return children;
}

export default ProtectedRoute;

