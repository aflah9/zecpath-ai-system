from transcript_normalizer import normalize_transcript

def process_transcript(raw_answers):

    processed = []

    for ans in raw_answers:

        normalized = normalize_transcript(ans["text"])

        processed.append({
            "question_id": ans["question_id"],
            "answer_text": normalized,
            "confidence_score": ans.get("confidence", 0.9)
        })

    return processed