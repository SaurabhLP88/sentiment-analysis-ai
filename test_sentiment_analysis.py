from unittest.mock import patch
import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer


class TestSentimentAnalyzer(unittest.TestCase):

    @patch('SentimentAnalysis.sentiment_analysis.requests.post')
    def test_sentiment_analyzer(self, mock_post):

        # Positive
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "documentSentiment": {
                "label": "SENT_POSITIVE",
                "score": 0.95
            }
        }
        result_1 = sentiment_analyzer('I love working with Python')
        self.assertEqual(result_1['label'], 'SENT_POSITIVE')

        # Negative
        mock_post.return_value.json.return_value = {
            "documentSentiment": {
                "label": "SENT_NEGATIVE",
                "score": -0.85
            }
        }
        result_2 = sentiment_analyzer('I hate working with Python')
        self.assertEqual(result_2['label'], 'SENT_NEGATIVE')

        # Neutral
        mock_post.return_value.json.return_value = {
            "documentSentiment": {
                "label": "SENT_NEUTRAL",
                "score": 0.0
            }
        }
        result_3 = sentiment_analyzer('I am neutral on Python')
        self.assertEqual(result_3['label'], 'SENT_NEUTRAL')


if __name__ == "__main__":
    unittest.main()