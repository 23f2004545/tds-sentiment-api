from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SentimentRequest(BaseModel):
    sentences: list[str]

POSITIVE = {
"love","great","awesome","excellent",
"happy","good","amazing","wonderful",
"fantastic","best"
}

NEGATIVE = {
"bad","terrible","awful","hate",
"sad","horrible","worst","angry",
"poor","disappointed"
}

@app.post("/sentiment")
def sentiment(req: SentimentRequest):
    results = []

    for sentence in req.sentences:

        text = sentence.lower()

        positive_hits = sum(
            word in text
            for word in POSITIVE
        )

        negative_hits = sum(
            word in text
            for word in NEGATIVE
        )

        if positive_hits > negative_hits:
            sentiment = "happy"
        elif negative_hits > positive_hits:
            sentiment = "sad"
        else:
            sentiment = "neutral"

        results.append({
            "sentence": sentence,
            "sentiment": sentiment
        })

    return {"results": results}

