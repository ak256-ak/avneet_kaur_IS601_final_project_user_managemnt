from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional, List
from uuid import UUID
from datetime import datetime


# Base class for all user-related schemas
class UserBase(BaseModel):
    email: EmailStr = Field(..., example="john.doe@example.com")
    first_name: Optional[str] = Field(None, example="John")
    last_name: Optional[str] = Field(None, example="Doe")
    bio: Optional[str] = Field(None, example="Experienced software developer.")
    profile_picture_url: Optional[str] = Field(None, example="https://example.com/profile.jpg")

    class Config:
        from_attributes = True


# Schema for creating a new user
class UserCreate(UserBase):
    password: str = Field(..., min_length=6, example="Secure*1234")


# Schema for updating user information
class UserUpdate(BaseModel):
    first_name: Optional[str] = Field(None, example="John")
    last_name: Optional[str] = Field(None, example="Doe")
    bio: Optional[str] = Field(None, example="Experienced backend developer.")
    profile_picture_url: Optional[str] = Field(None, example="https://example.com/profile.jpg")

    @validator('*', pre=True, always=True)
    def at_least_one_field_required(cls, value, field):
        if not value:
            raise ValueError(f"{field.name} cannot be None.")
        return value


# Schema for user response
class UserResponse(UserBase):
    id: UUID = Field(..., example="123e4567-e89b-12d3-a456-426614174000")
    created_at: datetime = Field(..., example="2024-01-01T00:00:00")
    updated_at: datetime = Field(..., example="2024-01-01T12:00:00")


# Schema for paginated list of users
class UserListResponse(BaseModel):
    items: List[UserResponse]
    total: int
    page: int
    size: int


# Schema for user login request
class LoginRequest(BaseModel):
    email: EmailStr = Field(..., example="john.doe@example.com")
    password: str = Field(..., example="Secure*1234")

