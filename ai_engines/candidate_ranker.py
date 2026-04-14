class CandidateRanker:

    def __init__(self, shortlist_threshold=70, review_threshold=50):
        self.shortlist_threshold = shortlist_threshold
        self.review_threshold = review_threshold

    def rank_candidates(self, candidates):
        # Sort candidates by score
        ranked = sorted(candidates, key=lambda x: x["score"], reverse=True)

        # Add status
        for c in ranked:
            c["status"] = self.classify(c["score"])

        return ranked

    def classify(self, score):
        if score >= self.shortlist_threshold:
            return "SHORTLISTED"
        elif score >= self.review_threshold:
            return "REVIEW"
        else:
            return "REJECTED"

    def get_top_candidates(self, ranked, top_n=3):
        return ranked[:top_n]