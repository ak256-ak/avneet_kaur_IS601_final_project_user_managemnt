import pytest
from pydantic import ValidationError
from app.schemas.user_schemas import UserBase, UserCreate, LoginRequest


# ----------------------- TEST CASES -----------------------

# 1. Test valid UserBase
def test_user_base_valid():
    user = UserBase(
        email="john.doe@example.com",
        first_name="John",
        last_name="Doe",
        role="ADMIN",
        bio="Software engineer",
        profile_picture_url="https://example.com/profile.jpg"
    )
    assert user.email == "john.doe@example.com"
    assert user.role == "ADMIN"


# 2. Test invalid email format in UserBase
def test_user_base_invalid_email():
    with pytest.raises(ValidationError) as e:
        UserBase(email="invalid-email", first_name="John", role="USER")
    assert "value is not a valid email address" in str(e.value)


# 3. Test missing email in UserBase
def test_user_base_missing_email():
    with pytest.raises(ValidationError) as e:
        UserBase(first_name="John", role="USER")
    assert "field required" in str(e.value)


# 4. Test valid UserCreate
def test_user_create_valid():
    user = UserCreate(
        email="john.doe@example.com",
        password="Secure*1234",
        first_name="John",
        role="ADMIN"
    )
    assert user.email == "john.doe@example.com"
    assert user.password == "Secure*1234"


# 5. Test invalid password in UserCreate
def test_user_create_invalid_password():
    with pytest.raises(ValidationError) as e:
        UserCreate(email="john.doe@example.com", password="123")
    assert "ensure this value has at least 6 characters" in str(e.value)


# 6. Test missing password in UserCreate
def test_user_create_missing_password():
    with pytest.raises(ValidationError) as e:
        UserCreate(email="john.doe@example.com")
    assert "field required" in str(e.value)


# 7. Test valid LoginRequest
def test_login_request_valid():
    login = LoginRequest(email="john.doe@example.com", password="Secure*1234")
    assert login.email == "john.doe@example.com"
    assert login.password == "Secure*1234"


# 8. Test invalid email in LoginRequest
def test_login_request_invalid_email():
    with pytest.raises(ValidationError) as e:
        LoginRequest(email="not-an-email", password="Secure*1234")
    assert "value is not a valid email address" in str(e.value)


# 9. Test missing password in LoginRequest
def test_login_request_missing_password():
    with pytest.raises(ValidationError) as e:
        LoginRequest(email="john.doe@example.com")
    assert "field required" in str(e.value)


# 10. Test missing email in LoginRequest
def test_login_request_missing_email():
    with pytest.raises(ValidationError) as e:
        LoginRequest(password="Secure*1234")
    assert "field required" in str(e.value)
