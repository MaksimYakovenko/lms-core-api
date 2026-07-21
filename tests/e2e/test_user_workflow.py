import pytest
import httpx

@pytest.mark.asyncio
async def test_user_signup_and_initial_actions(client: httpx.AsyncClient):
    # Step 1: Obtain a CAPTCHA
    captcha_response = await client.get('/auth/captcha')
    assert captcha_response.status_code == 200
    captcha_id = captcha_response.json().get('id')

    # Step 2: Register a new user
    signup_payload = {
        'email': 'testuser@example.com',
        'first_name': 'Test',
        'last_name': 'User',
        'password': 'strongpassword',
        'birthday': '2000-01-01',
        'captcha_id': captcha_id,
        'captcha_answer': '42'
    }
    signup_response = await client.post('/auth/sign-up', json=signup_payload)
    assert signup_response.status_code == 200
    assert signup_response.json().get('message') == 'Successfully registered.'

    # Step 3: Log in as the new user
    login_payload = {'email': 'testuser@example.com', 'password': 'strongpassword'}
    login_response = await client.post('/auth/sign-in', json=login_payload)
    assert login_response.status_code == 200
    token = login_response.json()['access_token']

    # Step 4: Access a protected resource with the token
    auth_headers = {'Authorization': f'Bearer {token}'}
    user_info_response = await client.get('/users/me', headers=auth_headers)
    assert user_info_response.status_code == 200
    assert user_info_response.json()['email'] == 'testuser@example.com'