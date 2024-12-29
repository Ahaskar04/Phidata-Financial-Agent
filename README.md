## **Phidata Financial Agent**

This project demonstrates the implementation of two AI agents using Groq models:
1. **Web Search Agent**: Searches the web using DuckDuckGo.
2. **Finance AI Agent**: Provides stock-related insights using YFinance.

Additionally, this project sets up an interactive Playground for testing the agents.

---

## **Setup Instructions**

### **Prerequisites**
- Python 3.9 or later.
- A working terminal (macOS/Linux/Windows Command Prompt).
- `pip` installed for managing Python dependencies.

---

### **Steps to Set Up**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Ahaskar04/Phidata-Financial-Agent.git
   cd Phidata-Financial-Agent
   ```

2. **Install Dependencies**
   Install the required Python packages listed in the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Environment Variables**
   This project requires API keys for Groq and OpenAI. Set the environment variables as follows:

   **For macOS/Linux:**
   ```bash
   export GROQ_API_KEY=<your-groq-api-key>
   export OPENAI_API_KEY=<your-openai-api-key>
   ```

   **For Windows (Command Prompt):**
   ```cmd
   setx GROQ_API_KEY <your-groq-api-key>
   setx OPENAI_API_KEY <your-openai-api-key>
   ```

   Replace `<your-groq-api-key>` and `<your-openai-api-key>` with your actual API keys.

4. **Run the Playground**
   Start the interactive Playground:
   ```bash
   python3 playground.py
   ```
   The Playground server will start, and you can access it at:
   ```
   https://phidata.app/playground?endpoint=localhost%3A7777
   ```

5. **Verify Setup**
   - Visit `/docs` to check the API endpoints:
     ```
     http://127.0.0.1:7777/docs
     ```

---

## **Notes**

1. **API Key Usage**
   - The project unexpectedly asks for the OpenAI API key even though it's running on Groq. 
   - This behavior might be related to certain tools or models configured in the Playground. I'll explore the documentation further and update here (or feel free to contribute if you figure it out).

2. **Agent Details**
   - **Web Search Agent**: Searches the web and includes sources in its output.
   - **Finance AI Agent**: Provides stock prices, analyst recommendations, company news, and more.

---

## **Project Files**

- `financial_agent.py`: Defines the two AI agents and configures their capabilities.
- `playground.py`: Sets up and serves the interactive Playground for the agents.
- `groq_check.py`: Verifies accessibility of the Groq model.
- `requirements.txt`: Lists all the dependencies required to run the project.
