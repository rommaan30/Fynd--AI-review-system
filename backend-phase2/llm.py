# def generate_ai_outputs(review: str):
#     if not review.strip():
#         return (
#             "Thanks for your feedback!",
#             "Empty review submitted",
#             "Ignore"
#         )

#     return (
#         "Thank you for sharing your experience.",
#         "User provided feedback.",
#         "Consider follow-up if rating is low."
#     )


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
