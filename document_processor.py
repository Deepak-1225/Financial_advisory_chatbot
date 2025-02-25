import os
import logging
import numpy as np
from typing import List, Dict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
from pypdf import PdfReader

class SimpleDocumentProcessor:
    """Document processing pipeline for financial documents using TF-IDF"""
    
    def __init__(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)
        
        # Initialize vectorizer
        self.vectorizer = TfidfVectorizer(
            stop_words='english',
            ngram_range=(1, 2),
            max_features=10000
        )
        
        # Storage for documents and vectors
        self.document_chunks = []
        self.chunk_texts = []
        self.vectors = None
            
    def process_document(self, file_path: str, chunk_size: int = 200):
        """Load and process a document into chunks"""
        try:
            if not os.path.exists(file_path):
                self.logger.error(f"Document not found: {file_path}")
                return False
                
            # Read PDF text content
            reader = PdfReader(file_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n\n"
                
            # Split into chunks
            chunks = self._split_into_chunks(text, chunk_size)
            self.document_chunks = chunks
            self.chunk_texts = chunks  # In this simple version, they're the same
            
            # Create TF-IDF vectors
            self.vectors = self.vectorizer.fit_transform(chunks)
            
            self.logger.info(f"Processed document into {len(chunks)} chunks")
            return True
            
        except Exception as e:
            self.logger.error(f"Error processing document: {str(e)}")
            return False
            
    def _split_into_chunks(self, text: str, chunk_size: int) -> List[str]:
        """Split text into chunks of approximately equal size"""
        chunks = []
        sentences = re.split(r'(?<=[.!?])\s+', text)
        current_chunk = ""
        
        for sentence in sentences:
            if len(current_chunk) + len(sentence) <= chunk_size:
                current_chunk += sentence + " "
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = sentence + " "
                
        if current_chunk:
            chunks.append(current_chunk.strip())
            
        return chunks
            
    def search_similar_content(self, query: str, k: int = 3) -> List[Dict]:
        """Search for content similar to the query"""
        try:
            if self.vectors is None:
                self.logger.error("No vectors available for search")
                return []
                
            # Create query vector
            query_vector = self.vectorizer.transform([query])
            
            # Calculate similarity scores
            similarity_scores = cosine_similarity(query_vector, self.vectors)[0]
            
            # Get top k results
            top_indices = similarity_scores.argsort()[-k:][::-1]
            
            # Format results
            results = []
            for idx in top_indices:
                results.append({
                    'content': self.chunk_texts[idx],
                    'score': float(similarity_scores[idx])
                })
                
            return results
            
        except Exception as e:
            self.logger.error(f"Error searching similar content: {str(e)}")
            return []