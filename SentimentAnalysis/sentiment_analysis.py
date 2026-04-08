import requests

def sentiment_analyzer(text_to_analyse):
    try:
        url = "https://router.huggingface.co/hf-inference/models/cardiffnlp/twitter-roberta-base-sentiment"
        headers = {
            "Authorization": "Bearer REMOVED"
        }

        response = requests.post(
            url,
            headers=headers,
            json={"inputs": text_to_analyse},
            timeout=10
        )

        result = response.json()

        # 🔍 Debug (you can remove later)
        print("HF RAW:", result)

        # Handle different response formats
        if isinstance(result, list):
            if isinstance(result[0], list):
                best = result[0][0]
            else:
                best = result[0]
        else:
            raise Exception("Unexpected response format")

        label_map = {
            "LABEL_0": "SENT_NEGATIVE",
            "LABEL_1": "SENT_NEUTRAL",
            "LABEL_2": "SENT_POSITIVE"
        }

        label = label_map.get(best['label'], "SENT_NEUTRAL")
        score = best['score']

        return {"label": label, "score": score}

    except Exception as e:
        print("HF ERROR:", e)
        return {"label": "SENT_NEUTRAL", "score": 0.0}
    

    