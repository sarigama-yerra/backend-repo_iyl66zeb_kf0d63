"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Rare cat breed for sale schema
class Cat(BaseModel):
    """
    Cat breeds for sale
    Collection name: "cat"
    """
    name: str = Field(..., description="Cat name")
    breed: str = Field(..., description="Breed name")
    price: float = Field(..., ge=0, description="Price in USD")
    description: Optional[str] = Field(None, description="Short description")
    image: Optional[HttpUrl] = Field(None, description="Primary image URL")
    gallery: Optional[List[HttpUrl]] = Field(default_factory=list, description="Additional image URLs")
    age_months: Optional[int] = Field(None, ge=0, description="Age in months")
    gender: Optional[str] = Field(None, description="Male/Female")
    temperament: Optional[List[str]] = Field(default_factory=list, description="Temperament tags")
    location: Optional[str] = Field(None, description="City, Country")
    available: bool = Field(True, description="Availability status")

# Add your own schemas here:
# --------------------------------------------------

# Note: The Flames database viewer will automatically:
# 1. Read these schemas from GET /schema endpoint
# 2. Use them for document validation when creating/editing
# 3. Handle all database operations (CRUD) directly
# 4. You don't need to create any database endpoints!
