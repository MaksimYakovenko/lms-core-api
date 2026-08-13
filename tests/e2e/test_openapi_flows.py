"""Auto-generated OpenAPI happy-path tests (e2e)."""

from __future__ import annotations

import httpx
import pytest

@pytest.mark.e2e
def test_e2e_sign_in_auth_sign_in_post(base_url: str) -> None:
    """E2E: Sign In"""
    url = f"{base_url}/auth/sign-in"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('POST', url, json={})
    assert response.status_code in (200, 422,), (
        f"Unexpected status {response.status_code} for POST {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_sign_up_auth_sign_up_post(base_url: str) -> None:
    """E2E: Sign Up"""
    url = f"{base_url}/auth/sign-up"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('POST', url, json={})
    assert response.status_code in (200, 422,), (
        f"Unexpected status {response.status_code} for POST {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_get_captcha_auth_captcha_get(base_url: str) -> None:
    """E2E: Get Captcha"""
    url = f"{base_url}/auth/captcha"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_refresh_token_auth_refresh_post(base_url: str) -> None:
    """E2E: Refresh Token"""
    url = f"{base_url}/auth/refresh"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('POST', url, json={})
    assert response.status_code in (200, 422,), (
        f"Unexpected status {response.status_code} for POST {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_get_appointments_appointments_get_appointments_get(base_url: str) -> None:
    """E2E: Get Appointments"""
    url = f"{base_url}/appointments/get_appointments"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_get_news_list_news_get(base_url: str) -> None:
    """E2E: Get News List"""
    url = f"{base_url}/news"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_get_news_item_news_id_get(base_url: str) -> None:
    """E2E: Get News Item"""
    pytest.skip('path/query parameters required — fill in when staging fixtures are available')

@pytest.mark.e2e
def test_e2e_parse_and_save_news_news_parse_save_post(base_url: str) -> None:
    """E2E: Parse And Save News"""
    url = f"{base_url}/news/parse/save"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('POST', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for POST {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_get_current_user_info_users_me_get(base_url: str) -> None:
    """E2E: Get Current User Info"""
    url = f"{base_url}/users/me"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_create_admin_admins_create_admin_post(base_url: str) -> None:
    """E2E: Create Admin"""
    url = f"{base_url}/admins/create_admin"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('POST', url, json={})
    assert response.status_code in (200, 422,), (
        f"Unexpected status {response.status_code} for POST {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_get_admins_admins_get_admins_get(base_url: str) -> None:
    """E2E: Get Admins"""
    url = f"{base_url}/admins/get_admins"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_update_admin_admins_update_admin_put(base_url: str) -> None:
    """E2E: Update Admin"""
    url = f"{base_url}/admins/update_admin"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('PUT', url, json={})
    assert response.status_code in (200, 422,), (
        f"Unexpected status {response.status_code} for PUT {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_create_teacher_teachers_create_teacher_post(base_url: str) -> None:
    """E2E: Create Teacher"""
    url = f"{base_url}/teachers/create_teacher"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('POST', url, json={})
    assert response.status_code in (200, 422,), (
        f"Unexpected status {response.status_code} for POST {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_get_teachers_teachers_get_teachers_get(base_url: str) -> None:
    """E2E: Get Teachers"""
    url = f"{base_url}/teachers/get_teachers"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_assign_student_to_group_teachers_assign_to_groups_put(base_url: str) -> None:
    """E2E: Assign Student To Group"""
    url = f"{base_url}/teachers/assign_to_groups"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('PUT', url, json={})
    assert response.status_code in (200, 422,), (
        f"Unexpected status {response.status_code} for PUT {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_assign_teacher_to_subjects_teachers_assign_to_subjects_put(base_url: str) -> None:
    """E2E: Assign Teacher To Subjects"""
    url = f"{base_url}/teachers/assign_to_subjects"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('PUT', url, json={})
    assert response.status_code in (200, 422,), (
        f"Unexpected status {response.status_code} for PUT {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_get_students_students_get_students_get(base_url: str) -> None:
    """E2E: Get Students"""
    url = f"{base_url}/students/get_students"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_update_student_students_update_student_put(base_url: str) -> None:
    """E2E: Update Student"""
    url = f"{base_url}/students/update_student"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('PUT', url, json={})
    assert response.status_code in (200, 422,), (
        f"Unexpected status {response.status_code} for PUT {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_assign_student_to_group_students_assign_to_group_put(base_url: str) -> None:
    """E2E: Assign Student To Group"""
    url = f"{base_url}/students/assign_to_group"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('PUT', url, json={})
    assert response.status_code in (200, 422,), (
        f"Unexpected status {response.status_code} for PUT {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_get_my_groups_groups_my_get(base_url: str) -> None:
    """E2E: Get My Groups"""
    url = f"{base_url}/groups/my"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_get_groups_groups_get_groups_get(base_url: str) -> None:
    """E2E: Get Groups"""
    url = f"{base_url}/groups/get_groups"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_create_group_groups_create_group_post(base_url: str) -> None:
    """E2E: Create Group"""
    url = f"{base_url}/groups/create_group"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('POST', url, json={})
    assert response.status_code in (200, 422,), (
        f"Unexpected status {response.status_code} for POST {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_get_my_subjects_subjects_my_get(base_url: str) -> None:
    """E2E: Get My Subjects"""
    url = f"{base_url}/subjects/my"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_get_students_subjects_get_subjects_get(base_url: str) -> None:
    """E2E: Get Students"""
    url = f"{base_url}/subjects/get_subjects"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_create_subject_subjects_create_subject_post(base_url: str) -> None:
    """E2E: Create Subject"""
    url = f"{base_url}/subjects/create_subject"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('POST', url, json={})
    assert response.status_code in (200, 422,), (
        f"Unexpected status {response.status_code} for POST {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_update_student_subjects_update_subject_put(base_url: str) -> None:
    """E2E: Update Student"""
    url = f"{base_url}/subjects/update_subject"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('PUT', url, json={})
    assert response.status_code in (200, 422,), (
        f"Unexpected status {response.status_code} for PUT {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_get_classrooms_classrooms_get_classrooms_get(base_url: str) -> None:
    """E2E: Get Classrooms"""
    url = f"{base_url}/classrooms/get_classrooms"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_create_classroom_classrooms_create_classroom_post(base_url: str) -> None:
    """E2E: Create Classroom"""
    url = f"{base_url}/classrooms/create_classroom"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('POST', url, json={})
    assert response.status_code in (200, 422,), (
        f"Unexpected status {response.status_code} for POST {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_get_my_journals_journals_my_get(base_url: str) -> None:
    """E2E: Get My Journals"""
    url = f"{base_url}/journals/my"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_get_journals_journals_get(base_url: str) -> None:
    """E2E: Get Journals"""
    url = f"{base_url}/journals"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_create_journal_journals_post(base_url: str) -> None:
    """E2E: Create Journal"""
    url = f"{base_url}/journals"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('POST', url, json={})
    assert response.status_code in (201, 422,), (
        f"Unexpected status {response.status_code} for POST {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_get_journal_journals_journal_id_get(base_url: str) -> None:
    """E2E: Get Journal"""
    pytest.skip('path/query parameters required — fill in when staging fixtures are available')

@pytest.mark.e2e
def test_e2e_export_journal_journals_journal_id_export_get(base_url: str) -> None:
    """E2E: Export Journal"""
    pytest.skip('path/query parameters required — fill in when staging fixtures are available')

@pytest.mark.e2e
def test_e2e_get_lesson_types_lessons_get_lesson_types_get(base_url: str) -> None:
    """E2E: Get Lesson Types"""
    url = f"{base_url}/lessons/get_lesson_types"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_get_lesson_periods_lessons_get_lesson_periods_get(base_url: str) -> None:
    """E2E: Get Lesson Periods"""
    url = f"{base_url}/lessons/get_lesson_periods"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_get_my_lessons_lessons_my_get(base_url: str) -> None:
    """E2E: Get My Lessons"""
    url = f"{base_url}/lessons/my"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_get_lessons_journals_journal_id_lessons_get(base_url: str) -> None:
    """E2E: Get Lessons"""
    pytest.skip('path/query parameters required — fill in when staging fixtures are available')

@pytest.mark.e2e
def test_e2e_get_grades_journals_journal_id_grades_get(base_url: str) -> None:
    """E2E: Get Grades"""
    pytest.skip('path/query parameters required — fill in when staging fixtures are available')

@pytest.mark.e2e
def test_e2e_get_total_count_total_count_get(base_url: str) -> None:
    """E2E: Get Total Count"""
    url = f"{base_url}/total_count"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.e2e
def test_e2e_health_health_get(base_url: str) -> None:
    """E2E: Health"""
    url = f"{base_url}/health"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

