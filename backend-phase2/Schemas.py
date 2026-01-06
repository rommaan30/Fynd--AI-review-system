from pydantic import BaseModel

class ReviewCreate(BaseModel):
    rating: int
    review: str

class ReviewOut(BaseModel):
    id: int
    rating: int
    review: str
    ai_summary: str
    ai_action: str

    class Config:
        orm_mode = True  # ⭐ VERY IMPORTANT
