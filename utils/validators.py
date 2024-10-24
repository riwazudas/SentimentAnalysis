# Valid input data
def validate_input(data):
    if not data:
        return "Invalid input format. Expected JSON."
    if 'review' not in data:
        return "Missing 'review' key in input."
    review = data.get('review', '')
    if not isinstance(review, str) or review.strip() == "":
        return "The 'review' field must be a non-empty string."
    return None
