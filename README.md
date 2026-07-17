# Multi-Agent Deep Research Application

An autonomous, multi-agent research application that takes a user query, plans and executes concurrent web investigations, synthesizes a comprehensive report, and emails the final product directly to the user. Powered by the **OpenAI Agents SDK**, **Pydantic**, and **Gradio**.

<div align="center">
  <h3>Planner ➔ Search ➔ Writer ➔ Email</h3>
</div>

---

## Features

* **Multi-Agent Architecture:** Leverages 4 specialized agents (Planner, Search, Writer, Email) to decouple planning, execution, synthesis, and communication.
* **Asynchronous Execution:** Utilizes `asyncio` to run planned web searches concurrently, minimizing end-to-end latency.
* **Strict Schema Validation:** Employs Pydantic structures to ensure reliable tool use, search plans, and structured report data outputs from the language model.
* **Real-Time UI Traces:** Yields status updates and live execution traces over a custom-styled Gradio frontend interface.
* **Automated Delivery:** Compiles 1000+ word deep-dive Markdown reports and routes them instantly via secure SMTP email.

---

## System Architecture

1. **Planner Agent:** Dissects the user query into a targeted 3-part web search strategy.
2. **Search Agent:** Executes searches concurrently and condenses findings into tightly scoped summaries.
3. **Writer Agent:** Combines search context to generate an exhaustive, publication-ready Markdown report.
4. **Email Agent:** Converts the final document into standard HTML and dispatches it via SMTP.

---

## Installation & Setup

### 1. Prerequisites
Ensure you have Python 3.10+ installed.

### 2. Create requirements.txt
Save the following lines as `requirements.txt` in your project folder:

```text
openai-agents==0.15.1
pydantic==2.13.3
gradio==6.14.0
python-dotenv==1.2.2
```

### 3. Environment Variables
Create a local `.env` file in the root directory and add your credentials:

```env
OPENAI_API_KEY=your_openai_api_key
EMAIL_ADDRESS=your_email@example.com
EMAIL_SMTP_SERVER=smtp.example.com
EMAIL_APP_PASSWORD=your_secure_app_password
```

## Running the Application

To install the dependencies and launch the web interface with the custom theme, run the following commands in your terminal:

```bash
pip install -r requirements.txt
python app.py
```
Open the local URL provided in your terminal (typically http://127.0.0.1:7860) to begin running investigations.
