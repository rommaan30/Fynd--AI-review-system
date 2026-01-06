from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from fastapi import HTTPException

from database import SessionLocal
from models import Review
from Schemas import ReviewCreate
from llm import generate_ai_outputs


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/reviews")
def create_review(data: ReviewCreate, db: Session = Depends(get_db)):
    ai_response, summary, action = generate_ai_outputs(
    data.review,
    data.rating
)

    review = Review(
        rating=data.rating,
        review=data.review,
        ai_response=ai_response,
        ai_summary=summary,
        ai_action=action
    )

    db.add(review)
    db.commit()
    db.refresh(review)

    return {"message": "Review submitted successfully"}

@router.delete("/admin/reviews/{review_id}")
def delete_review(review_id: int, db: Session = Depends(get_db)):
    review = db.query(Review).filter(Review.id == review_id).first()

    if not review:
        raise HTTPException(status_code=404, detail="Review not found")

    db.delete(review)
    db.commit()

    return {"message": "Review deleted successfully"}


@router.get("/admin/reviews")
def get_reviews(db: Session = Depends(get_db)):
    return db.query(Review).all()
