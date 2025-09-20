# AI Data Chat

A Streamlit application that enables natural language interaction with CSV and Excel data files using Google Gemini AI.

## 🌟 Features

- **Natural Language Queries**: Ask questions about your data in plain English
- **Multiple File Formats**: Support for CSV, Excel (xlsx, xls) files
- **Interactive Chat Interface**: Conversational UI powered by Streamlit
- **AI-Powered Analysis**: Uses Google Gemini 2.0 Flash for intelligent data insights
- **Data Preview**: Visual preview of uploaded datasets
- **Session History**: Maintains conversation context throughout the session

## 📋 Prerequisites

- Python 3.8 or higher
- Google Gemini API key

## 🚀 Installation

### 1. Clone the repository
```bash
git clone https://github.com/hatieku-boateng/python-machine-learning-projects.git
cd projects/ai-data-chat
```

### 2. Create a virtual environment
```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root:
```env
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.0-flash
```

## 🎯 Usage

1. **Start the application:**
```bash
streamlit run src/app.py
```

2. **Upload your data:**
   - Click the file uploader
   - Select a CSV or Excel file

3. **Ask questions:**
   - Type questions in natural language
   - Examples:
     - "How many rows are in the dataset?"
     - "What is the average value of column X?"
     - "Show me summary statistics"
     - "How many unique values are in column Y?"

## 📁 Project Structure

```
ai-data-chat/
├── src/
│   └── app.py           # Main application file
├── tests/               # Test files (to be added)
├── docs/                # Documentation
├── config/              # Configuration files
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── .env                # Environment variables (not tracked)
```

## 🔧 Configuration

The application can be configured through environment variables:

- `GEMINI_API_KEY`: Your Google Gemini API key (required)
- `GEMINI_MODEL`: The Gemini model to use (default: gemini-2.0-flash)

## 🛠️ Development

### Running tests
```bash
pytest tests/
```

### Updating dependencies
```bash
pip install package_name
pip freeze > requirements.txt
```

### Code formatting
```bash
black src/
flake8 src/
```

## 📝 License

This project is licensed under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## ⚠️ Known Issues

- You may see a one-time ALTS warning when starting - this is normal and doesn't affect functionality
- Large datasets (>100MB) may take time to process

## 📧 Contact

For questions or feedback, please open an issue in the repository.
