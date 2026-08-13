"""Auto-generated OpenAPI smoke tests (integration)."""

from __future__ import annotations

import httpx
import pytest

@pytest.mark.integration
def test_integration_sign_in_auth_sign_in_post(base_url: str) -> None:
    """Sign In"""
    url = f"{base_url}/auth/sign-in"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('POST', url)
    assert response.status_code in (200, 422,), (
        f"Unexpected status {response.status_code} for POST {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_sign_up_auth_sign_up_post(base_url: str) -> None:
    """Sign Up"""
    url = f"{base_url}/auth/sign-up"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('POST', url)
    assert response.status_code in (200, 422,), (
        f"Unexpected status {response.status_code} for POST {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_get_captcha_auth_captcha_get(base_url: str) -> None:
    """Get Captcha"""
    url = f"{base_url}/auth/captcha"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_refresh_token_auth_refresh_post(base_url: str) -> None:
    """Refresh Token"""
    url = f"{base_url}/auth/refresh"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('POST', url)
    assert response.status_code in (200, 422,), (
        f"Unexpected status {response.status_code} for POST {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_get_appointments_appointments_get_appointments_get(base_url: str) -> None:
    """Get Appointments"""
    url = f"{base_url}/appointments/get_appointments"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_get_news_list_news_get(base_url: str) -> None:
    """Get News List"""
    url = f"{base_url}/news"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_get_news_item_news_id_get(base_url: str) -> None:
    """Get News Item"""
    pytest.skip('path/query parameters required — fill in when staging fixtures are available')

@pytest.mark.integration
def test_integration_parse_and_save_news_news_parse_save_post(base_url: str) -> None:
    """Parse And Save News"""
    url = f"{base_url}/news/parse/save"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('POST', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for POST {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_get_current_user_info_users_me_get(base_url: str) -> None:
    """Get Current User Info"""
    url = f"{base_url}/users/me"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_create_admin_admins_create_admin_post(base_url: str) -> None:
    """Create Admin"""
    url = f"{base_url}/admins/create_admin"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('POST', url)
    assert response.status_code in (200, 422,), (
        f"Unexpected status {response.status_code} for POST {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_get_admins_admins_get_admins_get(base_url: str) -> None:
    """Get Admins"""
    url = f"{base_url}/admins/get_admins"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_update_admin_admins_update_admin_put(base_url: str) -> None:
    """Update Admin"""
    url = f"{base_url}/admins/update_admin"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('PUT', url)
    assert response.status_code in (200, 422,), (
        f"Unexpected status {response.status_code} for PUT {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_delete_admin_admins_delete_admin_id_delete(base_url: str) -> None:
    """Delete Admin"""
    pytest.skip('path/query parameters required — fill in when staging fixtures are available')

@pytest.mark.integration
def test_integration_create_teacher_teachers_create_teacher_post(base_url: str) -> None:
    """Create Teacher"""
    url = f"{base_url}/teachers/create_teacher"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('POST', url)
    assert response.status_code in (200, 422,), (
        f"Unexpected status {response.status_code} for POST {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_get_teachers_teachers_get_teachers_get(base_url: str) -> None:
    """Get Teachers"""
    url = f"{base_url}/teachers/get_teachers"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_update_teacher_teachers_update_teacher_id_put(base_url: str) -> None:
    """Update Teacher"""
    pytest.skip('path/query parameters required — fill in when staging fixtures are available')

@pytest.mark.integration
def test_integration_assign_student_to_group_teachers_assign_to_groups_put(base_url: str) -> None:
    """Assign Student To Group"""
    url = f"{base_url}/teachers/assign_to_groups"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('PUT', url)
    assert response.status_code in (200, 422,), (
        f"Unexpected status {response.status_code} for PUT {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_assign_teacher_to_subjects_teachers_assign_to_subjects_put(base_url: str) -> None:
    """Assign Teacher To Subjects"""
    url = f"{base_url}/teachers/assign_to_subjects"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('PUT', url)
    assert response.status_code in (200, 422,), (
        f"Unexpected status {response.status_code} for PUT {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_delete_teacher_teachers_delete_teacher_id_delete(base_url: str) -> None:
    """Delete Teacher"""
    pytest.skip('path/query parameters required — fill in when staging fixtures are available')

@pytest.mark.integration
def test_integration_get_students_students_get_students_get(base_url: str) -> None:
    """Get Students"""
    url = f"{base_url}/students/get_students"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_delete_student_students_delete_student_id_delete(base_url: str) -> None:
    """Delete Student"""
    pytest.skip('path/query parameters required — fill in when staging fixtures are available')

@pytest.mark.integration
def test_integration_update_student_students_update_student_put(base_url: str) -> None:
    """Update Student"""
    url = f"{base_url}/students/update_student"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('PUT', url)
    assert response.status_code in (200, 422,), (
        f"Unexpected status {response.status_code} for PUT {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_assign_student_to_group_students_assign_to_group_put(base_url: str) -> None:
    """Assign Student To Group"""
    url = f"{base_url}/students/assign_to_group"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('PUT', url)
    assert response.status_code in (200, 422,), (
        f"Unexpected status {response.status_code} for PUT {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_get_my_groups_groups_my_get(base_url: str) -> None:
    """Get My Groups"""
    url = f"{base_url}/groups/my"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_get_groups_groups_get_groups_get(base_url: str) -> None:
    """Get Groups"""
    url = f"{base_url}/groups/get_groups"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_create_group_groups_create_group_post(base_url: str) -> None:
    """Create Group"""
    url = f"{base_url}/groups/create_group"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('POST', url)
    assert response.status_code in (200, 422,), (
        f"Unexpected status {response.status_code} for POST {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_update_group_groups_update_group_group_id_put(base_url: str) -> None:
    """Update Group"""
    pytest.skip('path/query parameters required — fill in when staging fixtures are available')

@pytest.mark.integration
def test_integration_delete_group_groups_delete_group_group_id_delete(base_url: str) -> None:
    """Delete Group"""
    pytest.skip('path/query parameters required — fill in when staging fixtures are available')

@pytest.mark.integration
def test_integration_get_my_subjects_subjects_my_get(base_url: str) -> None:
    """Get My Subjects"""
    url = f"{base_url}/subjects/my"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_get_students_subjects_get_subjects_get(base_url: str) -> None:
    """Get Students"""
    url = f"{base_url}/subjects/get_subjects"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_create_subject_subjects_create_subject_post(base_url: str) -> None:
    """Create Subject"""
    url = f"{base_url}/subjects/create_subject"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('POST', url)
    assert response.status_code in (200, 422,), (
        f"Unexpected status {response.status_code} for POST {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_update_student_subjects_update_subject_put(base_url: str) -> None:
    """Update Student"""
    url = f"{base_url}/subjects/update_subject"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('PUT', url)
    assert response.status_code in (200, 422,), (
        f"Unexpected status {response.status_code} for PUT {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_delete_subject_subjects_delete_subject_id_delete(base_url: str) -> None:
    """Delete Subject"""
    pytest.skip('path/query parameters required — fill in when staging fixtures are available')

@pytest.mark.integration
def test_integration_get_classrooms_classrooms_get_classrooms_get(base_url: str) -> None:
    """Get Classrooms"""
    url = f"{base_url}/classrooms/get_classrooms"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_create_classroom_classrooms_create_classroom_post(base_url: str) -> None:
    """Create Classroom"""
    url = f"{base_url}/classrooms/create_classroom"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('POST', url)
    assert response.status_code in (200, 422,), (
        f"Unexpected status {response.status_code} for POST {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_delete_classroom_classrooms_delete_classroom_id_delete(base_url: str) -> None:
    """Delete Classroom"""
    pytest.skip('path/query parameters required — fill in when staging fixtures are available')

@pytest.mark.integration
def test_integration_update_classroom_classrooms_update_classroom_put(base_url: str) -> None:
    """Update Classroom"""
    pytest.skip('path/query parameters required — fill in when staging fixtures are available')

@pytest.mark.integration
def test_integration_get_my_journals_journals_my_get(base_url: str) -> None:
    """Get My Journals"""
    url = f"{base_url}/journals/my"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_get_journals_journals_get(base_url: str) -> None:
    """Get Journals"""
    url = f"{base_url}/journals"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_create_journal_journals_post(base_url: str) -> None:
    """Create Journal"""
    url = f"{base_url}/journals"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('POST', url)
    assert response.status_code in (201, 422,), (
        f"Unexpected status {response.status_code} for POST {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_get_journal_journals_journal_id_get(base_url: str) -> None:
    """Get Journal"""
    pytest.skip('path/query parameters required — fill in when staging fixtures are available')

@pytest.mark.integration
def test_integration_delete_journal_journals_journal_id_delete(base_url: str) -> None:
    """Delete Journal"""
    pytest.skip('path/query parameters required — fill in when staging fixtures are available')

@pytest.mark.integration
def test_integration_export_journal_journals_journal_id_export_get(base_url: str) -> None:
    """Export Journal"""
    pytest.skip('path/query parameters required — fill in when staging fixtures are available')

@pytest.mark.integration
def test_integration_get_lesson_types_lessons_get_lesson_types_get(base_url: str) -> None:
    """Get Lesson Types"""
    url = f"{base_url}/lessons/get_lesson_types"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_get_lesson_periods_lessons_get_lesson_periods_get(base_url: str) -> None:
    """Get Lesson Periods"""
    url = f"{base_url}/lessons/get_lesson_periods"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_get_my_lessons_lessons_my_get(base_url: str) -> None:
    """Get My Lessons"""
    url = f"{base_url}/lessons/my"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_add_lesson_journals_journal_id_lessons_post(base_url: str) -> None:
    """Add Lesson"""
    pytest.skip('path/query parameters required — fill in when staging fixtures are available')

@pytest.mark.integration
def test_integration_get_lessons_journals_journal_id_lessons_get(base_url: str) -> None:
    """Get Lessons"""
    pytest.skip('path/query parameters required — fill in when staging fixtures are available')

@pytest.mark.integration
def test_integration_update_lesson_journals_journal_id_lessons_lesson_id_put(base_url: str) -> None:
    """Update Lesson"""
    pytest.skip('path/query parameters required — fill in when staging fixtures are available')

@pytest.mark.integration
def test_integration_delete_lesson_journals_journal_id_lessons_lesson_id_delete(base_url: str) -> None:
    """Delete Lesson"""
    pytest.skip('path/query parameters required — fill in when staging fixtures are available')

@pytest.mark.integration
def test_integration_upsert_grade_journals_journal_id_grades_put(base_url: str) -> None:
    """Upsert Grade"""
    pytest.skip('path/query parameters required — fill in when staging fixtures are available')

@pytest.mark.integration
def test_integration_get_grades_journals_journal_id_grades_get(base_url: str) -> None:
    """Get Grades"""
    pytest.skip('path/query parameters required — fill in when staging fixtures are available')

@pytest.mark.integration
def test_integration_bulk_upsert_grades_journals_journal_id_grades_bulk_put(base_url: str) -> None:
    """Bulk Upsert Grades"""
    pytest.skip('path/query parameters required — fill in when staging fixtures are available')

@pytest.mark.integration
def test_integration_delete_grade_journals_journal_id_grades_grade_id_delete(base_url: str) -> None:
    """Delete Grade"""
    pytest.skip('path/query parameters required — fill in when staging fixtures are available')

@pytest.mark.integration
def test_integration_get_total_count_total_count_get(base_url: str) -> None:
    """Get Total Count"""
    url = f"{base_url}/total_count"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

@pytest.mark.integration
def test_integration_health_health_get(base_url: str) -> None:
    """Health"""
    url = f"{base_url}/health"
    with httpx.Client(timeout=30.0) as client:
        response = client.request('GET', url)
    assert response.status_code in (200,), (
        f"Unexpected status {response.status_code} for GET {url}: {response.text[:200]}"
    )

