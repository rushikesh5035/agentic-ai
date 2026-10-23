# 🔬 LangChain Multi-Agent Research System

A multi-agent research assistant built with LangChain. It searches the web, gathers information, writes structured reports, and evaluates their quality using AI-powered agents.

**🔬 Research Automation • 🤖 Multi-Agent Orchestration • 📝 Intelligent Report Generation**

## 🌟 Features

- **Multi-Agent Architecture**: Separate agents for searching, reading, writing, and reviewing
- **Automated Web Research**: Web search powered by Tavily
- **Smart Content Extraction**: Multiple strategies for extracting readable web content
- **AI-Powered Reports**: Automatically generated, structured research reports
- **Quality Evaluation**: Critic chain that scores reports and suggests improvements
- **Interactive UI**: Streamlit interface for easy use
- **Pipeline Orchestration**: Clear coordination between all research stages

## 🏗️ Architecture

```text
┌─────────────────────────────────────┐
│      Streamlit UI (app.py)          │
└──────────────────┬──────────────────┘
                   │
┌──────────────────▼──────────────────┐
│    Research Pipeline (pipeline.py)  │
└──────────────────┬──────────────────┘
                   │
     ┌─────────────┼─────────────┐
     │             │             │
┌────▼────┐  ┌─────▼─────┐  ┌────▼─────┐
│ Search  │  │  Reader    │  │  Writer  │
│ Agent   │  │  Agent     │  │  Chain   │
└────┬────┘  └─────┬─────┘  └────┬─────┘
     │             │             │
     └─────────────▼─────────────┘
             Tools Layer
       web_search • scrape_url
                   │
           ┌───────▼───────┐
           │ Critic Chain  │
           └───────────────┘
```

### Agent Responsibilities

- **Search Agent**: Finds relevant information across the web using Tavily
- **Reader Agent**: Extracts clean, readable content from selected URLs
- **Writer Chain**: Creates a structured and professional research report
- **Critic Chain**: Reviews the report and provides a score with feedback

## 🛠️ Technologies

| Technology           | Purpose                              |
| -------------------- | ------------------------------------ |
| **LangChain**        | Agent and chain orchestration        |
| **Groq**             | Language model provider              |
| **Streamlit**        | Interactive web interface            |
| **Tavily**           | Web search and information retrieval |
| **BeautifulSoup4**   | HTML parsing                         |
| **Trafilatura**      | Web content extraction               |
| **Readability-lxml** | Article content extraction           |
| **Python-dotenv**    | Environment configuration            |
| **Rich**             | Terminal output formatting           |

## 📋 Prerequisites

- Python 3.11 or higher
- Groq API key
- Tavily API key

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd LangChain-Multi-Agent-Research-System
```

### 2. Create a Virtual Environment

Using `venv`:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r ..\requirements.txt
```

If `requirements.txt` is copied into the project directory, use:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Get your keys from:

- [Groq API](https://console.groq.com/keys)
- [Tavily API](https://app.tavily.com/)

## 💡 Usage

### Run with Streamlit

```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser, enter a research topic, and run the pipeline.

### Run as a Script

```bash
python main.py
```

Edit the `topic` variable in `main.py` to research a different topic.

## 📁 Project Structure

```text
LangChain-Multi-Agent-Research-System/
├── app.py                         # Streamlit web interface
├── main.py                        # CLI entry point
├── demo.excalidraw                # Architecture diagram
└── src/
    ├── agents/
    │   └── agents.py              # Search, reader, writer, and critic logic
    ├── tools/
    │   └── tools.py               # web_search and scrape_url
    └── pipelines/
        └── pipeline.py            # Research orchestration
```

## 🔄 Workflow

1. **User Input**: Enter a topic through the UI or script.
2. **Search**: The search agent finds relevant web sources.
3. **Reading**: The reader agent extracts content from a selected URL.
4. **Writing**: The writer chain creates a structured report.
5. **Review**: The critic chain scores the report and provides feedback.
6. **Output**: The final report and review are displayed.

## 📊 Example Output

The generated report includes:

- Introduction and background
- Key findings
- Conclusion
- Source URLs
- Quality score and review feedback
