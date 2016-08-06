import indicoio
import os

indicoio.config.api_key = os.getenv("INDICO_API_KEY", "")

def analyze(text):
	val = indicoio.sentiment(text)
	if val < 0.2:
		return "bad"
	else:
		return "good"