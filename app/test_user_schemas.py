import pytest
from pydantic import ValidationError
from app.schemas.user_schemas import UserCreate, UserUpdate, UserResponse, LoginRequest, UserRole
import uuid



# Test valid UserCreate input
def test_user_create_valid():
    user = UserCreate(
        email="john.doe@example.com",
        password="Secure*1234",
        role=UserRole.ADMIN
    )
    assert user.email == "john.doe@example.com"
    assert user.password == "Secure*1234"
    assert user.role == UserRole.ADMIN


# Test invalid email format
def test_user_create_invalid_email():
    with pytest.raises(ValidationError) as e:
        UserCreate(
            email="invalid-email",
            password="Secure*1234",
            role=UserRole.USER
        )
    assert "value is not a valid email address" in str(e.value)


# Test invalid role value
def test_user_create_invalid_role():
    with pytest.raises(ValidationError) as e:
        UserCreate(
            email="john.doe@example.com",
            password="Secure*1234",
            role="INVALID_ROLE"  # Invalid role
        )
    assert "value is not a valid enumeration member" in str(e.value)


# Test missing required fields
def test_user_create_missing_fields():
    with pytest.raises(ValidationError) as e:
        UserCreate(password="Secure*1234")  # Missing email
    assert "field required" in str(e.value)



# Test valid UserUpdate input
def test_user_update_valid():
    user_update = UserUpdate(
        email="john.doe@example.com",
        nickname="john_doe",
        first_name="John",
        last_name="Doe",
        bio="Updated bio",
        role=UserRole.USER
    )
    assert user_update.email == "john.doe@example.com"
    assert user_update.nickname == "john_doe"
    assert user_update.bio == "Updated bio"
    assert user_update.role == UserRole.USER


# Test invalid email format in UserUpdate
def test_user_update_invalid_email():
    with pytest.raises(ValidationError) as e:
        UserUpdate(email="invalid-email")
    assert "value is not a valid email address" in str(e.value)


# ----------------------- TESTS FOR UserResponse -----------------------

# Test valid UserResponse
def test_user_response_valid():
    user_response = UserResponse(
        id=uuid.uuid4(),
        email="john.doe@example.com",
        role=UserRole.AUTHENTICATED
    )
    assert user_response.email == "john.doe@example.com"
    assert user_response.role == UserRole.AUTHENTICATED



# Test valid LoginRequest input
def test_login_request_valid():
    login = LoginRequest(
        email="john.doe@example.com",
        password="Secure*1234"
    )
    assert login.email == "john.doe@example.com"
    assert login.password == "Secure*1234"


# Test invalid email format in LoginRequest
def test_login_request_invalid_email():
    with pytest.raises(ValidationError) as e:
        LoginRequest(
            email="invalid-email",
            password="Secure*1234"
        )
    assert "value is not a valid email address" in str(e.value)


# Test missing email field in LoginRequest
def test_login_request_missing_email():
    with pytest.raises(ValidationError) as e:
        LoginRequest(password="Secure*1234")
    assert "field required" in str(e.value)


# Test missing password field in LoginRequest
def test_login_request_missing_password():
    with pytest.raises(ValidationError) as e:
        LoginRequest(email="john.doe@example.com")
    assert "field required" in str(e.value)
