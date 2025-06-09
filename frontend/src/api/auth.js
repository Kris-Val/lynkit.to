// auth.js (or wherever)
import Cookies from 'js-cookie';
import {useEffect} from "react";

export async function getCSRFToken() {
  const res = await fetch("http://127.0.0.1:8000/api/get-csrf-token/", {
    method: "GET",
    credentials: "include",
  });
  if (!res.ok) {
    throw new Error(`Could not fetch CSRF token: HTTP ${res.status}`);
  }
  const { csrfToken } = await res.json();

  return csrfToken;
}


export async function signUp(email,username, password) {
  const csrfToken = await getCSRFToken();
  console.log(`CSRF Token: ${csrfToken}`);
  return fetch('http://127.0.0.1:8000/_allauth/browser/v1/auth/signup', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken,
    },
    credentials: 'include',
    body: JSON.stringify({
      email,
      username:username,
      password: password,
    }),
  });
}
