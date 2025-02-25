import logging
import random
import re
from typing import List, Dict

class FinancialAdvisorRAG:
    """Financial Advisory Chatbot using RAG architecture with simplified components"""
    
    def __init__(self, document_processor):
        self.document_processor = document_processor
        self.logger = logging.getLogger(__name__)
        self.conversation_history = []
        
    def generate_response(self, query: str) -> str:
        """Generate dynamic responses to financial queries"""
        try:
            # Store query in conversation history
            self.conversation_history.append({"role": "user", "content": query})
            
            # Retrieve relevant content
            relevant_content = self.document_processor.search_similar_content(query, k=3)
            
            if not relevant_content:
                return "I don't have enough information to answer that question."
            
            # Generate response using retrieved content
            response = self._create_dynamic_response(query, relevant_content)
            
            # Add to conversation history
            self.conversation_history.append({"role": "assistant", "content": response})
            
            return response
            
        except Exception as e:
            self.logger.error(f"Error generating response: {str(e)}")
            return "I apologize, but I encountered an error processing your question."
            
    def _create_dynamic_response(self, query: str, relevant_content: List[Dict]) -> str:
        """Create a dynamic, contextual response based on query and relevant content"""
        
        # Introduction templates
        introductions = [
            "Based on my analysis of financial data, ",
            "According to financial best practices, ",
            "When it comes to financial advice, ",
            "Looking at relevant financial information, ",
            "From an investment perspective, "
        ]
        
        # Customize intro based on query topic
        query_lower = query.lower()
        if "portfolio" in query_lower or "diversification" in query_lower:
            introductions.extend([
                "For effective portfolio management, ",
                "When constructing a diversified portfolio, "
            ])
        elif "risk" in query_lower:
            introductions.extend([
                "To properly manage investment risk, ",
                "When considering risk factors in your investments, "
            ])
        elif "strategy" in query_lower or "approach" in query_lower:
            introductions.extend([
                "For a sound investment strategy, ",
                "When developing your financial approach, "
            ])
            
        # Select a random introduction
        introduction = random.choice(introductions)
        
        # Extract key information from relevant content
        content_parts = []
        for item in relevant_content:
            # Extract sentences that might be relevant
            content = item['content']
            sentences = re.split(r'(?<=[.!?])\s+', content)
            for sentence in sentences:
                if sentence and len(sentence) > 30:  # Skip very short fragments
                    content_parts.append(sentence)
        
        # Remove duplicates while preserving order
        unique_parts = []
        seen = set()
        for part in content_parts:
            if part.lower() not in seen:
                seen.add(part.lower())
                unique_parts.append(part)
        
        # Construct the response
        if unique_parts:
            response = introduction + unique_parts[0]
            
            # Add some additional content with connectors if available
            connectors = ["Additionally, ", "Furthermore, ", "It's also important to note that ", "Keep in mind that "]
            for i, part in enumerate(unique_parts[1:3], 1):
                if i <= len(connectors):
                    response += " " + random.choice(connectors) + part
        else:
            response = introduction + "I would recommend consulting with a financial advisor for personalized advice on this topic."
            
        return response