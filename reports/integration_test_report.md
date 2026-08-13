# Integration / E2E Test Report

**Status:** FAILED  
**Task / run:** `32031c1d-06db-40c0-847d-7f160718c9a6`  
**Results:** 18/70 passed  
**Provisioned:** yes  
**Base URL:** `https://lms-core-api-production.up.railway.app`  

---

## OpenAPI contract

- **Title:** LMS Core API
- **Version:** 1.0.0
- **Source:** `https://lms-core-api-production.up.railway.app/openapi.json`
- **Endpoints:** 56

| Method | Path | Operation |
| --- | --- | --- |
| POST | `/auth/sign-in` | sign_in_auth_sign_in_post |
| POST | `/auth/sign-up` | sign_up_auth_sign_up_post |
| GET | `/auth/captcha` | get_captcha_auth_captcha_get |
| POST | `/auth/refresh` | refresh_token_auth_refresh_post |
| GET | `/appointments/get_appointments` | get_appointments_appointments_get_appointments_get |
| GET | `/news` | get_news_list_news_get |
| GET | `/news/{id}` | get_news_item_news__id__get |
| POST | `/news/parse/save` | parse_and_save_news_news_parse_save_post |
| GET | `/users/me` | get_current_user_info_users_me_get |
| POST | `/admins/create_admin` | create_admin_admins_create_admin_post |
| GET | `/admins/get_admins` | get_admins_admins_get_admins_get |
| PUT | `/admins/update_admin` | update_admin_admins_update_admin_put |
| DELETE | `/admins/delete_admin/{id}` | delete_admin_admins_delete_admin__id__delete |
| POST | `/teachers/create_teacher` | create_teacher_teachers_create_teacher_post |
| GET | `/teachers/get_teachers` | get_teachers_teachers_get_teachers_get |
| PUT | `/teachers/update_teacher/{id}` | update_teacher_teachers_update_teacher__id__put |
| PUT | `/teachers/assign_to_groups` | assign_student_to_group_teachers_assign_to_groups_put |
| PUT | `/teachers/assign_to_subjects` | assign_teacher_to_subjects_teachers_assign_to_subjects_put |
| DELETE | `/teachers/delete_teacher/{id}` | delete_teacher_teachers_delete_teacher__id__delete |
| GET | `/students/get_students` | get_students_students_get_students_get |
| DELETE | `/students/delete_student/{id}` | delete_student_students_delete_student__id__delete |
| PUT | `/students/update_student` | update_student_students_update_student_put |
| PUT | `/students/assign_to_group` | assign_student_to_group_students_assign_to_group_put |
| GET | `/groups/my` | get_my_groups_groups_my_get |
| GET | `/groups/get_groups` | get_groups_groups_get_groups_get |
| POST | `/groups/create_group` | create_group_groups_create_group_post |
| PUT | `/groups/update_group/{group_id}` | update_group_groups_update_group__group_id__put |
| DELETE | `/groups/delete_group/{group_id}` | delete_group_groups_delete_group__group_id__delete |
| GET | `/subjects/my` | get_my_subjects_subjects_my_get |
| GET | `/subjects/get_subjects` | get_students_subjects_get_subjects_get |
| POST | `/subjects/create_subject` | create_subject_subjects_create_subject_post |
| PUT | `/subjects/update_subject` | update_student_subjects_update_subject_put |
| DELETE | `/subjects/delete_subject/{id}` | delete_subject_subjects_delete_subject__id__delete |
| GET | `/classrooms/get_classrooms` | get_classrooms_classrooms_get_classrooms_get |
| POST | `/classrooms/create_classroom` | create_classroom_classrooms_create_classroom_post |
| DELETE | `/classrooms/delete_classroom/{id}` | delete_classroom_classrooms_delete_classroom__id__delete |
| PUT | `/classrooms/update_classroom` | update_classroom_classrooms_update_classroom_put |
| GET | `/journals/my` | get_my_journals_journals_my_get |
| GET | `/journals` | get_journals_journals_get |
| POST | `/journals` | create_journal_journals_post |
| GET | `/journals/{journal_id}` | get_journal_journals__journal_id__get |
| DELETE | `/journals/{journal_id}` | delete_journal_journals__journal_id__delete |
| GET | `/journals/{journal_id}/export` | export_journal_journals__journal_id__export_get |
| GET | `/lessons/get_lesson_types` | get_lesson_types_lessons_get_lesson_types_get |
| GET | `/lessons/get_lesson_periods` | get_lesson_periods_lessons_get_lesson_periods_get |
| GET | `/lessons/my` | get_my_lessons_lessons_my_get |
| POST | `/journals/{journal_id}/lessons` | add_lesson_journals__journal_id__lessons_post |
| GET | `/journals/{journal_id}/lessons` | get_lessons_journals__journal_id__lessons_get |
| PUT | `/journals/{journal_id}/lessons/{lesson_id}` | update_lesson_journals__journal_id__lessons__lesson_id__put |
| DELETE | `/journals/{journal_id}/lessons/{lesson_id}` | delete_lesson_journals__journal_id__lessons__lesson_id__delete |
| … | 6 more | |

## Generated test files

- `tests/integration/conftest.py`
- `tests/integration/test_openapi_smoke.py`
- `tests/e2e/conftest.py`
- `tests/e2e/test_openapi_flows.py`

## Failures

### `tests/integration/test_openapi_smoke.py::test_integration_get_appointments_appointments_get_appointments_get`

```
tests\integration\test_openapi_smoke.py:54: in test_integration_get_appointments_appointments_get_appointments_get
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for GET https://lms-core-api-production.up.railway.app/appointments/get_appointments: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/integration/test_openapi_smoke.py::test_integration_get_news_list_news_get`

```
tests\integration\test_openapi_smoke.py:64: in test_integration_get_news_list_news_get
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for GET https://lms-core-api-production.up.railway.app/news: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/integration/test_openapi_smoke.py::test_integration_parse_and_save_news_news_parse_save_post`

```
tests\integration\test_openapi_smoke.py:79: in test_integration_parse_and_save_news_news_parse_save_post
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for POST https://lms-core-api-production.up.railway.app/news/parse/save: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/integration/test_openapi_smoke.py::test_integration_get_current_user_info_users_me_get`

```
tests\integration\test_openapi_smoke.py:89: in test_integration_get_current_user_info_users_me_get
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for GET https://lms-core-api-production.up.railway.app/users/me: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/integration/test_openapi_smoke.py::test_integration_get_admins_admins_get_admins_get`

```
tests\integration\test_openapi_smoke.py:109: in test_integration_get_admins_admins_get_admins_get
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for GET https://lms-core-api-production.up.railway.app/admins/get_admins: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/integration/test_openapi_smoke.py::test_integration_update_admin_admins_update_admin_put`

```
tests\integration\test_openapi_smoke.py:119: in test_integration_update_admin_admins_update_admin_put
    assert response.status_code in (200, 422,), (
E   AssertionError: Unexpected status 403 for PUT https://lms-core-api-production.up.railway.app/admins/update_admin: {"detail":"Not authenticated"}
E   assert 403 in (200, 422)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/integration/test_openapi_smoke.py::test_integration_create_teacher_teachers_create_teacher_post`

```
tests\integration\test_openapi_smoke.py:134: in test_integration_create_teacher_teachers_create_teacher_post
    assert response.status_code in (200, 422,), (
E   AssertionError: Unexpected status 403 for POST https://lms-core-api-production.up.railway.app/teachers/create_teacher: {"detail":"Not authenticated"}
E   assert 403 in (200, 422)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/integration/test_openapi_smoke.py::test_integration_get_teachers_teachers_get_teachers_get`

```
tests\integration\test_openapi_smoke.py:144: in test_integration_get_teachers_teachers_get_teachers_get
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for GET https://lms-core-api-production.up.railway.app/teachers/get_teachers: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/integration/test_openapi_smoke.py::test_integration_assign_student_to_group_teachers_assign_to_groups_put`

```
tests\integration\test_openapi_smoke.py:159: in test_integration_assign_student_to_group_teachers_assign_to_groups_put
    assert response.status_code in (200, 422,), (
E   AssertionError: Unexpected status 403 for PUT https://lms-core-api-production.up.railway.app/teachers/assign_to_groups: {"detail":"Not authenticated"}
E   assert 403 in (200, 422)
E    +  where 403 = <Response [403 Forbidden]>.status_code
_ test_integration_assign_teacher_to_subjects_teachers_assign_to_subjects_put _
tests\integration\test_openapi_smoke.py:169: in test_integration_assign_teacher_to_subjects_teachers_assign_to_subjects_put
    assert response.status_code in (200, 422,), (
E   AssertionError: Unexpected status 403 for PUT https://lms-core-api-production.up.railway.app/teachers/assign_to_subjects: {"detail":"Not authenticated"}
E   assert 403 in (200, 422)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/integration/test_openapi_smoke.py::test_integration_assign_teacher_to_subjects_teachers_assign_to_subjects_put`

```
(see output)
```

### `tests/integration/test_openapi_smoke.py::test_integration_get_students_students_get_students_get`

```
tests\integration\test_openapi_smoke.py:184: in test_integration_get_students_students_get_students_get
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for GET https://lms-core-api-production.up.railway.app/students/get_students: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/integration/test_openapi_smoke.py::test_integration_update_student_students_update_student_put`

```
tests\integration\test_openapi_smoke.py:199: in test_integration_update_student_students_update_student_put
    assert response.status_code in (200, 422,), (
E   AssertionError: Unexpected status 403 for PUT https://lms-core-api-production.up.railway.app/students/update_student: {"detail":"Not authenticated"}
E   assert 403 in (200, 422)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/integration/test_openapi_smoke.py::test_integration_get_my_groups_groups_my_get`

```
tests\integration\test_openapi_smoke.py:219: in test_integration_get_my_groups_groups_my_get
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for GET https://lms-core-api-production.up.railway.app/groups/my: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/integration/test_openapi_smoke.py::test_integration_get_groups_groups_get_groups_get`

```
tests\integration\test_openapi_smoke.py:229: in test_integration_get_groups_groups_get_groups_get
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for GET https://lms-core-api-production.up.railway.app/groups/get_groups: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/integration/test_openapi_smoke.py::test_integration_get_my_subjects_subjects_my_get`

```
tests\integration\test_openapi_smoke.py:259: in test_integration_get_my_subjects_subjects_my_get
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for GET https://lms-core-api-production.up.railway.app/subjects/my: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/integration/test_openapi_smoke.py::test_integration_get_students_subjects_get_subjects_get`

```
tests\integration\test_openapi_smoke.py:269: in test_integration_get_students_subjects_get_subjects_get
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for GET https://lms-core-api-production.up.railway.app/subjects/get_subjects: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/integration/test_openapi_smoke.py::test_integration_create_subject_subjects_create_subject_post`

```
tests\integration\test_openapi_smoke.py:279: in test_integration_create_subject_subjects_create_subject_post
    assert response.status_code in (200, 422,), (
E   AssertionError: Unexpected status 403 for POST https://lms-core-api-production.up.railway.app/subjects/create_subject: {"detail":"Not authenticated"}
E   assert 403 in (200, 422)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/integration/test_openapi_smoke.py::test_integration_update_student_subjects_update_subject_put`

```
tests\integration\test_openapi_smoke.py:289: in test_integration_update_student_subjects_update_subject_put
    assert response.status_code in (200, 422,), (
E   AssertionError: Unexpected status 403 for PUT https://lms-core-api-production.up.railway.app/subjects/update_subject: {"detail":"Not authenticated"}
E   assert 403 in (200, 422)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/integration/test_openapi_smoke.py::test_integration_create_classroom_classrooms_create_classroom_post`

```
tests\integration\test_openapi_smoke.py:314: in test_integration_create_classroom_classrooms_create_classroom_post
    assert response.status_code in (200, 422,), (
E   AssertionError: Unexpected status 403 for POST https://lms-core-api-production.up.railway.app/classrooms/create_classroom: {"detail":"Not authenticated"}
E   assert 403 in (200, 422)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/integration/test_openapi_smoke.py::test_integration_get_my_journals_journals_my_get`

```
tests\integration\test_openapi_smoke.py:334: in test_integration_get_my_journals_journals_my_get
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for GET https://lms-core-api-production.up.railway.app/journals/my: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/integration/test_openapi_smoke.py::test_integration_get_journals_journals_get`

```
tests\integration\test_openapi_smoke.py:344: in test_integration_get_journals_journals_get
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for GET https://lms-core-api-production.up.railway.app/journals: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/integration/test_openapi_smoke.py::test_integration_create_journal_journals_post`

```
tests\integration\test_openapi_smoke.py:354: in test_integration_create_journal_journals_post
    assert response.status_code in (201, 422,), (
E   AssertionError: Unexpected status 403 for POST https://lms-core-api-production.up.railway.app/journals: {"detail":"Not authenticated"}
E   assert 403 in (201, 422)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/integration/test_openapi_smoke.py::test_integration_get_lesson_types_lessons_get_lesson_types_get`

```
tests\integration\test_openapi_smoke.py:379: in test_integration_get_lesson_types_lessons_get_lesson_types_get
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for GET https://lms-core-api-production.up.railway.app/lessons/get_lesson_types: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/integration/test_openapi_smoke.py::test_integration_get_lesson_periods_lessons_get_lesson_periods_get`

```
tests\integration\test_openapi_smoke.py:389: in test_integration_get_lesson_periods_lessons_get_lesson_periods_get
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for GET https://lms-core-api-production.up.railway.app/lessons/get_lesson_periods: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/integration/test_openapi_smoke.py::test_integration_get_my_lessons_lessons_my_get`

```
tests\integration\test_openapi_smoke.py:399: in test_integration_get_my_lessons_lessons_my_get
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for GET https://lms-core-api-production.up.railway.app/lessons/my: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/integration/test_openapi_smoke.py::test_integration_get_total_count_total_count_get`

```
tests\integration\test_openapi_smoke.py:449: in test_integration_get_total_count_total_count_get
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for GET https://lms-core-api-production.up.railway.app/total_count: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/e2e/test_openapi_flows.py::test_e2e_get_appointments_appointments_get_appointments_get`

```
tests\e2e\test_openapi_flows.py:54: in test_e2e_get_appointments_appointments_get_appointments_get
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for GET https://lms-core-api-production.up.railway.app/appointments/get_appointments: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/e2e/test_openapi_flows.py::test_e2e_get_news_list_news_get`

```
tests\e2e\test_openapi_flows.py:64: in test_e2e_get_news_list_news_get
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for GET https://lms-core-api-production.up.railway.app/news: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/e2e/test_openapi_flows.py::test_e2e_parse_and_save_news_news_parse_save_post`

```
tests\e2e\test_openapi_flows.py:79: in test_e2e_parse_and_save_news_news_parse_save_post
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for POST https://lms-core-api-production.up.railway.app/news/parse/save: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/e2e/test_openapi_flows.py::test_e2e_get_current_user_info_users_me_get`

```
tests\e2e\test_openapi_flows.py:89: in test_e2e_get_current_user_info_users_me_get
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for GET https://lms-core-api-production.up.railway.app/users/me: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/e2e/test_openapi_flows.py::test_e2e_get_admins_admins_get_admins_get`

```
tests\e2e\test_openapi_flows.py:109: in test_e2e_get_admins_admins_get_admins_get
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for GET https://lms-core-api-production.up.railway.app/admins/get_admins: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/e2e/test_openapi_flows.py::test_e2e_update_admin_admins_update_admin_put`

```
tests\e2e\test_openapi_flows.py:119: in test_e2e_update_admin_admins_update_admin_put
    assert response.status_code in (200, 422,), (
E   AssertionError: Unexpected status 403 for PUT https://lms-core-api-production.up.railway.app/admins/update_admin: {"detail":"Not authenticated"}
E   assert 403 in (200, 422)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/e2e/test_openapi_flows.py::test_e2e_create_teacher_teachers_create_teacher_post`

```
tests\e2e\test_openapi_flows.py:129: in test_e2e_create_teacher_teachers_create_teacher_post
    assert response.status_code in (200, 422,), (
E   AssertionError: Unexpected status 403 for POST https://lms-core-api-production.up.railway.app/teachers/create_teacher: {"detail":"Not authenticated"}
E   assert 403 in (200, 422)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/e2e/test_openapi_flows.py::test_e2e_get_teachers_teachers_get_teachers_get`

```
tests\e2e\test_openapi_flows.py:139: in test_e2e_get_teachers_teachers_get_teachers_get
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for GET https://lms-core-api-production.up.railway.app/teachers/get_teachers: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/e2e/test_openapi_flows.py::test_e2e_assign_student_to_group_teachers_assign_to_groups_put`

```
tests\e2e\test_openapi_flows.py:149: in test_e2e_assign_student_to_group_teachers_assign_to_groups_put
    assert response.status_code in (200, 422,), (
E   AssertionError: Unexpected status 403 for PUT https://lms-core-api-production.up.railway.app/teachers/assign_to_groups: {"detail":"Not authenticated"}
E   assert 403 in (200, 422)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/e2e/test_openapi_flows.py::test_e2e_assign_teacher_to_subjects_teachers_assign_to_subjects_put`

```
tests\e2e\test_openapi_flows.py:159: in test_e2e_assign_teacher_to_subjects_teachers_assign_to_subjects_put
    assert response.status_code in (200, 422,), (
E   AssertionError: Unexpected status 403 for PUT https://lms-core-api-production.up.railway.app/teachers/assign_to_subjects: {"detail":"Not authenticated"}
E   assert 403 in (200, 422)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/e2e/test_openapi_flows.py::test_e2e_get_students_students_get_students_get`

```
tests\e2e\test_openapi_flows.py:169: in test_e2e_get_students_students_get_students_get
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for GET https://lms-core-api-production.up.railway.app/students/get_students: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/e2e/test_openapi_flows.py::test_e2e_update_student_students_update_student_put`

```
tests\e2e\test_openapi_flows.py:179: in test_e2e_update_student_students_update_student_put
    assert response.status_code in (200, 422,), (
E   AssertionError: Unexpected status 403 for PUT https://lms-core-api-production.up.railway.app/students/update_student: {"detail":"Not authenticated"}
E   assert 403 in (200, 422)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/e2e/test_openapi_flows.py::test_e2e_get_my_groups_groups_my_get`

```
tests\e2e\test_openapi_flows.py:199: in test_e2e_get_my_groups_groups_my_get
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for GET https://lms-core-api-production.up.railway.app/groups/my: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/e2e/test_openapi_flows.py::test_e2e_get_groups_groups_get_groups_get`

```
tests\e2e\test_openapi_flows.py:209: in test_e2e_get_groups_groups_get_groups_get
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for GET https://lms-core-api-production.up.railway.app/groups/get_groups: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/e2e/test_openapi_flows.py::test_e2e_get_my_subjects_subjects_my_get`

```
tests\e2e\test_openapi_flows.py:229: in test_e2e_get_my_subjects_subjects_my_get
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for GET https://lms-core-api-production.up.railway.app/subjects/my: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/e2e/test_openapi_flows.py::test_e2e_get_students_subjects_get_subjects_get`

```
tests\e2e\test_openapi_flows.py:239: in test_e2e_get_students_subjects_get_subjects_get
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for GET https://lms-core-api-production.up.railway.app/subjects/get_subjects: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/e2e/test_openapi_flows.py::test_e2e_create_subject_subjects_create_subject_post`

```
tests\e2e\test_openapi_flows.py:249: in test_e2e_create_subject_subjects_create_subject_post
    assert response.status_code in (200, 422,), (
E   AssertionError: Unexpected status 403 for POST https://lms-core-api-production.up.railway.app/subjects/create_subject: {"detail":"Not authenticated"}
E   assert 403 in (200, 422)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/e2e/test_openapi_flows.py::test_e2e_update_student_subjects_update_subject_put`

```
tests\e2e\test_openapi_flows.py:259: in test_e2e_update_student_subjects_update_subject_put
    assert response.status_code in (200, 422,), (
E   AssertionError: Unexpected status 403 for PUT https://lms-core-api-production.up.railway.app/subjects/update_subject: {"detail":"Not authenticated"}
E   assert 403 in (200, 422)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/e2e/test_openapi_flows.py::test_e2e_create_classroom_classrooms_create_classroom_post`

```
tests\e2e\test_openapi_flows.py:279: in test_e2e_create_classroom_classrooms_create_classroom_post
    assert response.status_code in (200, 422,), (
E   AssertionError: Unexpected status 403 for POST https://lms-core-api-production.up.railway.app/classrooms/create_classroom: {"detail":"Not authenticated"}
E   assert 403 in (200, 422)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/e2e/test_openapi_flows.py::test_e2e_get_my_journals_journals_my_get`

```
tests\e2e\test_openapi_flows.py:289: in test_e2e_get_my_journals_journals_my_get
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for GET https://lms-core-api-production.up.railway.app/journals/my: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/e2e/test_openapi_flows.py::test_e2e_get_journals_journals_get`

```
tests\e2e\test_openapi_flows.py:299: in test_e2e_get_journals_journals_get
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for GET https://lms-core-api-production.up.railway.app/journals: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/e2e/test_openapi_flows.py::test_e2e_create_journal_journals_post`

```
tests\e2e\test_openapi_flows.py:309: in test_e2e_create_journal_journals_post
    assert response.status_code in (201, 422,), (
E   AssertionError: Unexpected status 403 for POST https://lms-core-api-production.up.railway.app/journals: {"detail":"Not authenticated"}
E   assert 403 in (201, 422)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/e2e/test_openapi_flows.py::test_e2e_get_lesson_types_lessons_get_lesson_types_get`

```
tests\e2e\test_openapi_flows.py:329: in test_e2e_get_lesson_types_lessons_get_lesson_types_get
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for GET https://lms-core-api-production.up.railway.app/lessons/get_lesson_types: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/e2e/test_openapi_flows.py::test_e2e_get_lesson_periods_lessons_get_lesson_periods_get`

```
tests\e2e\test_openapi_flows.py:339: in test_e2e_get_lesson_periods_lessons_get_lesson_periods_get
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for GET https://lms-core-api-production.up.railway.app/lessons/get_lesson_periods: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/e2e/test_openapi_flows.py::test_e2e_get_my_lessons_lessons_my_get`

```
tests\e2e\test_openapi_flows.py:349: in test_e2e_get_my_lessons_lessons_my_get
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for GET https://lms-core-api-production.up.railway.app/lessons/my: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

### `tests/e2e/test_openapi_flows.py::test_e2e_get_total_count_total_count_get`

```
tests\e2e\test_openapi_flows.py:369: in test_e2e_get_total_count_total_count_get
    assert response.status_code in (200,), (
E   AssertionError: Unexpected status 403 for GET https://lms-core-api-production.up.railway.app/total_count: {"detail":"Not authenticated"}
E   assert 403 in (200,)
E    +  where 403 = <Response [403 Forbidden]>.status_code
```

## Pytest output (truncated)

```
cts_put
FAILED tests/integration/test_openapi_smoke.py::test_integration_get_students_students_get_students_get
FAILED tests/integration/test_openapi_smoke.py::test_integration_update_student_students_update_student_put
FAILED tests/integration/test_openapi_smoke.py::test_integration_get_my_groups_groups_my_get
FAILED tests/integration/test_openapi_smoke.py::test_integration_get_groups_groups_get_groups_get
FAILED tests/integration/test_openapi_smoke.py::test_integration_get_my_subjects_subjects_my_get
FAILED tests/integration/test_openapi_smoke.py::test_integration_get_students_subjects_get_subjects_get
FAILED tests/integration/test_openapi_smoke.py::test_integration_create_subject_subjects_create_subject_post
FAILED tests/integration/test_openapi_smoke.py::test_integration_update_student_subjects_update_subject_put
FAILED tests/integration/test_openapi_smoke.py::test_integration_create_classroom_classrooms_create_classroom_post
FAILED tests/integration/test_openapi_smoke.py::test_integration_get_my_journals_journals_my_get
FAILED tests/integration/test_openapi_smoke.py::test_integration_get_journals_journals_get
FAILED tests/integration/test_openapi_smoke.py::test_integration_create_journal_journals_post
FAILED tests/integration/test_openapi_smoke.py::test_integration_get_lesson_types_lessons_get_lesson_types_get
FAILED tests/integration/test_openapi_smoke.py::test_integration_get_lesson_periods_lessons_get_lesson_periods_get
FAILED tests/integration/test_openapi_smoke.py::test_integration_get_my_lessons_lessons_my_get
FAILED tests/integration/test_openapi_smoke.py::test_integration_get_total_count_total_count_get
FAILED tests/e2e/test_openapi_flows.py::test_e2e_get_appointments_appointments_get_appointments_get
FAILED tests/e2e/test_openapi_flows.py::test_e2e_get_news_list_news_get - Ass...
FAILED tests/e2e/test_openapi_flows.py::test_e2e_parse_and_save_news_news_parse_save_post
FAILED tests/e2e/test_openapi_flows.py::test_e2e_get_current_user_info_users_me_get
FAILED tests/e2e/test_openapi_flows.py::test_e2e_get_admins_admins_get_admins_get
FAILED tests/e2e/test_openapi_flows.py::test_e2e_update_admin_admins_update_admin_put
FAILED tests/e2e/test_openapi_flows.py::test_e2e_create_teacher_teachers_create_teacher_post
FAILED tests/e2e/test_openapi_flows.py::test_e2e_get_teachers_teachers_get_teachers_get
FAILED tests/e2e/test_openapi_flows.py::test_e2e_assign_student_to_group_teachers_assign_to_groups_put
FAILED tests/e2e/test_openapi_flows.py::test_e2e_assign_teacher_to_subjects_teachers_assign_to_subjects_put
FAILED tests/e2e/test_openapi_flows.py::test_e2e_get_students_students_get_students_get
FAILED tests/e2e/test_openapi_flows.py::test_e2e_update_student_students_update_student_put
FAILED tests/e2e/test_openapi_flows.py::test_e2e_get_my_groups_groups_my_get
FAILED tests/e2e/test_openapi_flows.py::test_e2e_get_groups_groups_get_groups_get
FAILED tests/e2e/test_openapi_flows.py::test_e2e_get_my_subjects_subjects_my_get
FAILED tests/e2e/test_openapi_flows.py::test_e2e_get_students_subjects_get_subjects_get
FAILED tests/e2e/test_openapi_flows.py::test_e2e_create_subject_subjects_create_subject_post
FAILED tests/e2e/test_openapi_flows.py::test_e2e_update_student_subjects_update_subject_put
FAILED tests/e2e/test_openapi_flows.py::test_e2e_create_classroom_classrooms_create_classroom_post
FAILED tests/e2e/test_openapi_flows.py::test_e2e_get_my_journals_journals_my_get
FAILED tests/e2e/test_openapi_flows.py::test_e2e_get_journals_journals_get - ...
FAILED tests/e2e/test_openapi_flows.py::test_e2e_create_journal_journals_post
FAILED tests/e2e/test_openapi_flows.py::test_e2e_get_lesson_types_lessons_get_lesson_types_get
FAILED tests/e2e/test_openapi_flows.py::test_e2e_get_lesson_periods_lessons_get_lesson_periods_get
FAILED tests/e2e/test_openapi_flows.py::test_e2e_get_my_lessons_lessons_my_get
FAILED tests/e2e/test_openapi_flows.py::test_e2e_get_total_count_total_count_get
52 failed, 18 passed, 26 skipped, 96 warnings in 14.43s
```

---
_Generated by AI Factory at 2026-08-13 12:59:08Z_
