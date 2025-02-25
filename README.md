# Financial Advisory Chatbot with RAG Architecture

A sophisticated financial advisory chatbot that leverages Retrieval Augmented Generation (RAG) architecture to provide personalized financial guidance across multiple domains including investment strategies, retirement planning, tax optimization, and market analysis.

## Overview

This project implements a RAG-based chatbot that:

1. Processes financial documents into vector embeddings
2. Performs semantic search to retrieve relevant financial information
3. Generates context-aware responses to user queries about financial topics

The system demonstrates how AI can be used to augment financial advisory services by providing accurate, contextual information drawn from a diverse knowledge base.

## Features

- **Document Processing Pipeline**: Converts financial documents into searchable vector representations
- **Semantic Search**: Retrieves the most relevant information based on user queries
- **Dynamic Response Generation**: Creates natural, varied responses that combine information from multiple sources
- **Multi-domain Financial Knowledge**: Covers investment strategies, retirement planning, tax optimization, and market analysis

## Technical Implementation

The implementation uses:

- **TF-IDF Vectorization**: For creating document embeddings
- **Cosine Similarity**: For semantic search and retrieval
- **Natural Language Processing**: For query analysis and response generation
- **Document Chunking**: For efficient processing and retrieval of information

## Getting Started

### Prerequisites

Install the requirements.txt file for dependencies.


### Installation

1. Clone the repository

2. Install dependencies

3. Run the example


## Usage Example

```python
from document_processor import SimpleDocumentProcessor
from chatbot import FinancialAdvisorRAG

# Initialize document processor
processor = SimpleDocumentProcessor()

# Process financial documents
processor.process_document('data/investment_strategies.pdf')
processor.process_document('data/retirement_planning.pdf')
processor.process_document('data/tax_optimization.pdf')

# Initialize chatbot
advisor = FinancialAdvisorRAG(processor)

# Ask financial questions
response = advisor.generate_response("How should I diversify my investment portfolio?")
print(response)