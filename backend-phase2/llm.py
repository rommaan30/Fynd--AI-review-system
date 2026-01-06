
def generate_ai_outputs(review: str, rating: int):
    if not review.strip():
        return (
            "Thanks!",
            "Empty review",
            "Ignore"
        )

    if rating <= 2:
        return (
            "Sorry for the inconvenience.",
            "Negative feedback detected.",
            "Urgent follow-up required."
        )

    elif rating == 3:
        return (
            "Thanks for the feedback.",
            "Neutral review.",
            "Optional follow-up."
        )

    else:
        return (
            "Thank you for your positive feedback!",
            "Positive review.",
            "No action required."
        )
