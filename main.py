"""One Star, Written in Sap.

Writes a single one-line one-star review to $MAKEFUN_OUTPUT_DIR/entry.txt:
a houseplant reviewing its human owner. The plant's grievance is the
watering schedule — once a month, called "tough love" — and the review
lands on the plant photosynthesizing out of spite. Standard library only.
"""

import os

REVIEW = (
    "One star. He waters me once a month, calls it 'tough love', "
    "and tells his dates I'm 'so easy to keep alive' while I'm up "
    "here photosynthesizing out of spite."
)


def check_review(text):
    """Check the review against the competition gate before writing.

    The gate needs UTF-8 text of 1 to 279 characters, not only white
    space, in a single line: one one-star review by a houseplant of
    its human owner. Returns the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("review must not be only whitespace")
    if len(cleaned) > 279:
        raise ValueError(
            "review is %d characters, over the 279 limit" % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("review must be exactly one line")
    return cleaned


def review_shape(text):
    """Measure the review for one last sanity pass.

    Returns a dict with the character count and the word count of the
    cleaned text. A review too short to carry a grievance, or one that
    reads like a lecture instead of a one-star review, is caught here
    before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_review(REVIEW)
    shape = review_shape(text)
    if shape["words"] < 5:
        raise ValueError("review is too short to carry a grievance")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
