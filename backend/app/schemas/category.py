from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from app.models.enums import CategoryType

class CategoryBase(BaseModel):
    name: str
    type: CategoryType
    icon: Optional[str] = None
    parent_id: Optional[int] = None

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    icon: Optional[str] = None

class CategoryResponse(CategoryBase):
    category_id: int
    user_id: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)

# Schema để trả về cây danh mục (Nested)
class CategoryTreeResponse(CategoryResponse):
    subcategories: Optional[List['CategoryTreeResponse']] = []

    model_config = ConfigDict(from_attributes=True)

# Bắt buộc trong Pydantic V2 để xử lý cấu trúc đệ quy (Forward Reference)
CategoryTreeResponse.model_rebuild()