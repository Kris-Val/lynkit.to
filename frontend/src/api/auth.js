const DJANGO_DOMAIN = "http://127.0.0.1:8000"

const ACCEPT_JSON = {
    accept: 'application/json'
}

export const Client = Object.freeze({
    APP: 'app',
    BROWSER: 'browser'
})

export const settings = {
    client: Client.BROWSER,
    baseUrl: `${DJANGO_DOMAIN}/_allauth/${Client.BROWSER}/v1`,
    // Always include credentials (cookies) for browser requests to support CSRF
    withCredentials: true
}

export const URLs = Object.freeze({
    SIGNUP: '/auth/signup',
    LOGIN: '/auth/login',
    PROVIDER_SIGNUP: '/auth/provider/signup',
    REDIRECT_TO_PROVIDER: '/auth/provider/redirect',
    PROVIDER_TOKEN: '/auth/provider/token',

});

async function getCSRFToken() {
    const response = await fetch(`${DJANGO_DOMAIN}/api/v1/get-csrf-token/`, {
        method: "GET",
        credentials: "include",
    });
    if (!response.ok) {
        throw new Error(`Could not fetch CSRF token: HTTP ${response.status}`);
    }
    const {csrfToken} = await response.json();

    return csrfToken;
}

async function request(method, path, data, headers = {}) {
    let options = {method, headers: {...ACCEPT_JSON, ...headers}, credentials: 'include'};

    let csrfToken = await getCSRFToken();
    if (csrfToken) {
        options.headers['X-CSRFToken'] = csrfToken;
    }
    if (data) {
        options.body = JSON.stringify(data);
        options.headers['Content-Type'] = 'application/json';
    }

    let response = await fetch(settings.baseUrl + path, options);
    return await response.json()
}

export const auth = {
    signUp: (data) => request('POST', URLs.SIGNUP, data),
    login: (data) => request('POST', URLs.LOGIN, data),

}
