import unittest
import os
import tempfile
from fpdf import FPDF
from document_processor import SimpleDocumentProcessor

class TestDocumentProcessor(unittest.TestCase):
    """Test cases for the SimpleDocumentProcessor class"""
    
    def setUp(self):
        """Set up a test environment before each test"""
        self.processor = SimpleDocumentProcessor()
        
        # Create a temporary test document
        self.test_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.test_dir, "test_document.pdf")
        
        # Create a simple PDF for testing
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, txt="This is a test document for financial analysis. It contains information about investments, risk management, and portfolio diversification strategies.")
        pdf.output(self.test_file)
    
    def tearDown(self):
        """Clean up after each test"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists(self.test_dir):
            os.rmdir(self.test_dir)
    
    def test_document_loading(self):
        """Test that documents can be loaded correctly"""
        result = self.processor.process_document(self.test_file)
        self.assertTrue(result)
        self.assertGreater(len(self.processor.document_chunks), 0)
    
    def test_document_chunking(self):
        """Test that document text is properly chunked"""
        self.processor.process_document(self.test_file)
        
        # Verify chunks were created
        self.assertGreater(len(self.processor.document_chunks), 0)
        
        # Check content of chunks
        for chunk in self.processor.document_chunks:
            self.assertIsInstance(chunk, str)
            self.assertGreater(len(chunk), 0)
    
    def test_vector_creation(self):
        """Test that TF-IDF vectors are created correctly"""
        self.processor.process_document(self.test_file)
        
        # Verify vectors were created
        self.assertIsNotNone(self.processor.vectors)
        
        # Check dimensions of vectors
        self.assertEqual(self.processor.vectors.shape[0], len(self.processor.document_chunks))
    
    def test_similar_content_search(self):
        """Test search functionality"""
        self.processor.process_document(self.test_file)
        
        # Search for relevant content
        results = self.processor.search_similar_content("investment strategies")
        
        # Verify search results
        self.assertIsInstance(results, list)
        if results:  # If any results found
            self.assertIsInstance(results[0], dict)
            self.assertIn('content', results[0])
            self.assertIn('score', results[0])
    
    def test_nonexistent_file(self):
        """Test handling of nonexistent files"""
        result = self.processor.process_document("nonexistent_file.pdf")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()