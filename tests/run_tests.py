import unittest
import os
import sys

# Add the parent directory to the path so tests can import the main package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import test modules
from test_document_processor import TestDocumentProcessor
from test_chatbot import TestFinancialAdvisorRAG

if __name__ == '__main__':
    # Initialize the test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add tests to the suite
    suite.addTests(loader.loadTestsFromTestCase(TestDocumentProcessor))
    suite.addTests(loader.loadTestsFromTestCase(TestFinancialAdvisorRAG))
    
    # Initialize a runner and run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Exit with non-zero code if there were failures
    sys.exit(not result.wasSuccessful())