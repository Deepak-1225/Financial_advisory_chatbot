import logging
from document_processor import SimpleDocumentProcessor
from chatbot import FinancialAdvisorRAG
from document_generator import create_comprehensive_financial_documents

def main():
    """Main entry point for Financial Advisory Chatbot demo"""
    # Setup logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    
    try:
        # Create financial documents (for demo purposes)
        create_comprehensive_financial_documents()
        
        # Initialize document processor
        processor = SimpleDocumentProcessor()
        
        # Process all documents
        document_paths = [
            'data/investment_strategies.pdf',
            'data/retirement_planning.pdf',
            'data/tax_optimization.pdf',
            'data/market_analysis.pdf'
        ]
        
        # Process each document
        all_chunks = []
        for doc_path in document_paths:
            success = processor.process_document(doc_path)
            if success:
                all_chunks.extend(processor.document_chunks)
                
        # Re-initialize with combined knowledge
        processor = SimpleDocumentProcessor()
        processor.document_chunks = all_chunks
        processor.chunk_texts = all_chunks
        processor.vectors = processor.vectorizer.fit_transform(all_chunks)
        
        # Initialize financial advisor chatbot
        advisor = FinancialAdvisorRAG(processor)
        
        # Interactive demo
        print("\n=== Financial Advisory Chatbot ===")
        print("Type 'exit' to quit\n")
        
        while True:
            query = input("What would you like to know about financial planning? ")
            if query.lower() in ['exit', 'quit', 'bye']:
                print("Thank you for using the Financial Advisory Chatbot!")
                break
                
            response = advisor.generate_response(query)
            print(f"\nResponse: {response}\n")
            
    except Exception as e:
        logger.error(f"Error in main application: {str(e)}")
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()