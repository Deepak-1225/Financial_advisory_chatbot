import unittest
from unittest.mock import MagicMock, patch
from chatbot import FinancialAdvisorRAG

class TestFinancialAdvisorRAG(unittest.TestCase):
    """Test cases for the FinancialAdvisorRAG class"""
    
    def setUp(self):
        """Set up a test environment before each test"""
        self.mock_processor = MagicMock()
        self.chatbot = FinancialAdvisorRAG(self.mock_processor)
    
    def test_generate_response_with_content(self):
        """Test response generation when content is found"""
        # Mock the search results
        mock_results = [
            {
                'content': 'A well-diversified portfolio requires strategic allocation across multiple asset classes.',
                'score': 0.95
            },
            {
                'content': 'Modern portfolio theory suggests including a mix of stocks, bonds, and alternative investments.',
                'score': 0.85
            }
        ]
        
        self.mock_processor.search_similar_content.return_value = mock_results
        
        # Test response generation
        query = "How should I diversify my portfolio?"
        response = self.chatbot.generate_response(query)
        
        # Verify a response was generated
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)
        
        # Verify the search was called with correct parameters
        self.mock_processor.search_similar_content.assert_called_once()
    
    def test_generate_response_no_content(self):
        """Test response generation when no content is found"""
        # Mock empty search results
        self.mock_processor.search_similar_content.return_value = []
        
        # Test response generation
        query = "How should I invest in cryptocurrency?"
        response = self.chatbot.generate_response(query)
        
        # Verify a fallback response was generated
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)
        self.assertIn("don't have enough information", response)
    
    def test_conversation_history(self):
        """Test that conversation history is maintained"""
        # Mock search results
        mock_results = [{'content': 'Test content', 'score': 0.9}]
        self.mock_processor.search_similar_content.return_value = mock_results
        
        # Generate a response
        query = "Test question"
        self.chatbot.generate_response(query)
        
        # Check conversation history
        self.assertEqual(len(self.chatbot.conversation_history), 2)
        self.assertEqual(self.chatbot.conversation_history[0]['role'], 'user')
        self.assertEqual(self.chatbot.conversation_history[0]['content'], query)
        self.assertEqual(self.chatbot.conversation_history[1]['role'], 'assistant')
    
    def test_dynamic_response_variation(self):
        """Test that responses have variation"""
        # Mock the same search results for multiple queries
        mock_results = [{'content': 'Test content', 'score': 0.9}]
        self.mock_processor.search_similar_content.return_value = mock_results
        
        # Generate multiple responses to the same query
        responses = set()
        for _ in range(5):
            response = self.chatbot.generate_response("Test question")
            responses.add(response)
        
        # Check if there is variation in responses
        # Note: There's a small chance this could fail randomly if the same intro is chosen multiple times
        self.assertGreater(len(responses), 1, "Response generation lacks variation")

if __name__ == '__main__':
    unittest.main()