const API_URL = 'http://127.0.0.1:8000';

export async function loginWithGoogle(idToken) {
	console.log("Sending token to backend");
	console.log(idToken.substring(0, 50));
	
	const response = await fetch(`${API_URL}/auth/google`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({
			token: idToken
		})
	});

	if (!response.ok) {
		throw new Error('Google login failed');
	}

	return await response.json();
}

export async function register(
	name,
	email,
	password
) {
	const response = await fetch(
		`${API_URL}/auth/register`,
		{
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				name,
				email,
				password
			})
		}
	);

	const data = await response.json();

	if (!response.ok) {
		throw new Error(
			data.detail || 'Registration failed'
		);
	}

	return data;
}

export async function login(
	email,
	password
) {
	const response = await fetch(
		`${API_URL}/auth/login`,
		{
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				email,
				password
			})
		}
	);

	const data = await response.json();

	if (!response.ok) {
		throw new Error(
			data.detail || 'Login failed'
		);
	}

	return data;
}

export async function forgotPassword(email) {
	const response = await fetch(
		`${API_URL}/auth/forgot-password`,
		{
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				email
			})
		}
	);

	const data = await response.json();

	if (!response.ok) {
		throw new Error(
			data.detail || 'Failed to send OTP'
		);
	}

	return data;
}

export async function verifyOtp(
	email,
	otp
) {
	const response = await fetch(
		`${API_URL}/auth/verify-otp`,
		{
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				email,
				otp
			})
		}
	);

	const data = await response.json();

	if (!response.ok) {
		throw new Error(
			data.detail || 'OTP verification failed'
		);
	}

	return data;
}

export async function resetPassword(
	email,
	otp,
	password
) {
	const response = await fetch(
		`${API_URL}/auth/reset-password`,
		{
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				email,
				otp,
				password
			})
		}
	);

	const data = await response.json();

	if (!response.ok) {
		throw new Error(
			data.detail || 'Password reset failed'
		);
	}

	return data;
}
