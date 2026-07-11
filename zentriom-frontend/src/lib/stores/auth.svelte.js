export const authStore = $state({
	user: null,
	token: null,
	isAuthenticated: false,
	loading: false
});

export function setAuth(user, token) {
	authStore.user = user;
	authStore.token = token;
	authStore.isAuthenticated = true;

	localStorage.setItem(
		'auth',
		JSON.stringify({
			user,
			token
		})
	);
}

export function loadAuth() {
	const stored = localStorage.getItem('auth');

	if (!stored) return;

	try {
		const data = JSON.parse(stored);

		authStore.user = data.user;
		authStore.token = data.token;
		authStore.isAuthenticated = true;
	}
	catch (err) {
		console.error('Failed to load auth', err);
		localStorage.removeItem('auth');
	}
}

export function logout() {
	authStore.user = null;
	authStore.token = null;
	authStore.isAuthenticated = false;
	authStore.loading = false;

	localStorage.removeItem('auth');
}
