# AI Image Generator

An AI-powered Image Generator built using Python and Generative AI APIs. This project allows users to generate images through an AI-based image generation workflow.

## 🚀 Features

- AI-powered image generation
- Python-based implementation
- API integration for image generation
- Environment variable support for API key management
- Modular project structure

## 🛠️ Tech Stack

- Python
- Generative AI API
- REST API Integration
- Environment Variables

## 📁 Project Structure

```text
Image-Generator/
│
├── agent.py
├── image_api.py
├── runner.py
├── .env.example
├── .gitignore
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Purvi-Jain05/Image-Generator.git
```

### 2. Navigate to the project directory

```bash
cd Image-Generator
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure API Key

Create a `.env` file in the project root directory and add your API key:

```env
GEMINI_API_KEY=your_api_key_here
```

**Note:** Never upload your actual `.env` file or API keys to GitHub.

### 7. Run the project

```bash
python runner.py
```

## 🔐 Security

- API keys are stored in environment variables.
- `.env` files are excluded using `.gitignore`.
- `.env.example` is provided as a configuration template.

## 👩‍💻 Author

**Purvi Jain**

GitHub: [Purvi-Jain05](https://github.com/Purvi-Jain05)

---

⭐ If you find this project interesting, feel free to explore the repository!