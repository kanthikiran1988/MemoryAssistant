# AI Memory Assistant with LangChain

A smart AI assistant that uses LangChain and OpenAI's function calling to store and retrieve information using semantic search. Built with Chroma vector database for persistent memory storage.

## 🌟 Features

- Natural language interface for storing and retrieving information
- Semantic search using Chroma vector database
- OpenAI function calling for structured interactions
- Persistent memory storage
- Detailed logging for debugging and monitoring

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenAI API key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-memory-assistant.git
cd ai-memory-assistant
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

### Running the Application

1. Start the memory assistant:
```bash
python memory_assistant.py
```

2. Interact with the assistant using natural language:
```
You: Remember that John likes pizza
Assistant: I've stored that information about John

You: What do you know about John?
Assistant: Here's what I know about John:
On 2024-03-14T15:30:00: John likes pizza
```

## 📁 Project Structure

```
ai-memory-assistant/
├── memory_assistant.py      # Main application with LangChain function calling
├── vector_store.py         # Vector database implementation using Chroma
├── requirements.txt        # Project dependencies
├── .env                   # Environment variables (not in git)
├── .gitignore            # Git ignore rules
└── README.md             # Documentation
```

## 💡 Usage Examples

### Storing Information
```
You: Remember that Sarah's birthday is on March 15th
You: Note that Tom is a software engineer at Google
You: Remember that Sarah loves chocolate cake
```

### Retrieving Information
```
You: What do you know about Sarah?
You: Tell me about Tom's job
You: When is Sarah's birthday?
```

## 🛠️ Technical Details

- Uses LangChain's ChatOpenAI for natural language processing
- Implements function calling with store_memory and retrieve_memory functions
- Stores embeddings in Chroma vector database for semantic search
- Includes system prompts to guide AI behavior
- Provides detailed logging for debugging

## 📝 Environment Variables

Required environment variables in `.env`:
- `OPENAI_API_KEY`: Your OpenAI API key

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Important Notes

- Keep your `.env` file secure and never commit it to version control
- The memory database is stored locally in the `memory_db` directory
- The system uses GPT-4 by default for optimal performance

## 🐛 Troubleshooting

Common issues and solutions:

1. **OpenAI API Key Error**
   - Ensure your API key is correctly set in the `.env` file
   - Verify the API key has sufficient credits

2. **Memory Database Issues**
   - Delete the `memory_db` directory to start fresh
   - Ensure proper write permissions in the project directory

3. **Package Installation Issues**
   - Upgrade pip: `pip install --upgrade pip`
   - Install packages one by one if requirements.txt fails

## 📞 Support

For issues and feature requests, please use the GitHub Issues section of this repository.
