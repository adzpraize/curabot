# CuraBot - AI-Powered Medical Advisory Chatbot

CuraBot is an intelligent chatbot application designed to provide preliminary health information and medicine suggestions based on user-described symptoms. Built with Flask, machine learning, and a comprehensive disease database, CuraBot helps users understand potential illnesses and recommended treatments.

⚠️ **DISCLAIMER**: CuraBot is NOT a substitute for professional medical advice. Always consult a qualified healthcare provider for accurate diagnosis and treatment.

## 🌟 Features

- **User Authentication**: Secure login and registration system with SQLite database
- **Symptom-Based Diagnosis**: AI model that matches user symptoms to potential diseases
- **Medicine Recommendations**: Suggests medications and treatments for identified conditions
- **Conversational Interface**: Chat-based interface for easy interaction
- **Disease Database**: Comprehensive database of 14+ common diseases with symptoms and treatments
- **Session Management**: Secure session handling for authenticated users
- **Responsive Design**: Web-based interface accessible from any device

## 🛠️ Tech Stack

- **Backend**: Flask 3.1.3 (Python web framework)
- **Database**: SQLite (user credentials and data)
- **ML/NLP**: 
  - scikit-learn 1.8.0 (machine learning)
  - NLTK 3.9.3 (natural language processing)
  - NumPy 2.4.3 (numerical computing)
  - SciPy 1.17.1 (scientific computing)
- **Server**: Gunicorn 25.1.0 (WSGI HTTP server)
- **Frontend Dependencies**: Jinja2 3.1.6 (templating), Werkzeug 3.1.6 (utilities)
- **Additional**: joblib, regex, tqdm

## 📋 Project Structure

```
curabot/
├── app.py              # Main Flask application with routes
├── model.py            # Prediction model and symptom matching
├── disease_db.py       # Comprehensive disease database
├── dataset.json        # Alternative dataset format
├── requirements.txt    # Python package dependencies
├── users.db           # SQLite database (generated)
├── templates/         # HTML templates
│   ├── login.html     # Login page
│   ├── register.html  # Registration page
│   └── index.html     # Chat interface
├── static/            # Static files (CSS, JavaScript, images)
└── venv/              # Virtual environment (not tracked)
```

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/adzpraize/curabot.git
   cd curabot
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   python app.py
   ```
   The application will be available at `http://localhost:5000`

## 📖 Usage

### Getting Started
1. **Register**: Create a new account with a username and password
2. **Login**: Sign in with your credentials
3. **Chat**: Describe your symptoms to CuraBot
4. **Get Results**: Receive disease predictions and medicine recommendations

### Example Interactions
- "I have high fever, chills, and I've been sweating a lot"
- "My head hurts and I'm feeling nauseous with sensitivity to light"
- "I have a persistent cough and chest discomfort"

### Supported Diseases
The CuraBot database includes information for:
- Malaria
- Typhoid Fever
- Peptic/Gastric Ulcer
- Common Cold
- Influenza (Flu)
- Dengue Fever
- Bronchitis
- Urinary Tract Infection (UTI)
- Hypertension (High Blood Pressure)
- Type 2 Diabetes
- Allergic Rhinitis
- Sinusitis
- Tonsillitis
- Appendicitis

## 🔧 API Endpoints

### Authentication
- `POST /register` - Register a new user
- `POST /` (Login) - Authenticate and login
- `GET /logout` - Logout and clear session

### Application
- `GET /chat` - Access the chat interface (requires authentication)
- `POST /get` - Send a message and get disease/medicine prediction
  - **Request**: `{\"message\": \"symptom description\"}`
  - **Response**: `{\"reply\": \"Possible illness: X\nSuggested medicine: Y, Z\n⚠️ This is not a medical diagnosis.\"}`

## 🧠 How It Works

### Prediction Model
The `predict()` function in `model.py`:
1. Converts user input to lowercase
2. Scores each disease based on keyword matches in the symptom database
3. Returns the disease with the highest match score
4. Provides associated medicine recommendations
5. Falls back to generic advice if no matches are found

### Disease Matching Algorithm
- Simple keyword-based matching
- Case-insensitive comparison
- Accumulative scoring system
- Fallback for unknown conditions

## 🔒 Security Considerations

- Passwords are stored in SQLite (consider using password hashing for production)
- Session-based authentication
- CSRF protection via Flask
- SQL parameterized queries to prevent SQL injection

## 📝 Configuration

Edit `app.py` to modify:
- Secret key (for session management)
- Debug mode (set to `False` for production)
- Database location
- Port and host settings

## 🚨 Important Disclaimers

**⚠️ MEDICAL DISCLAIMER**
- CuraBot provides **informational purposes only**
- CuraBot is **NOT a licensed medical professional**
- CuraBot **CANNOT provide diagnosis or prescription**
- **Always consult a qualified healthcare provider** before starting any treatment
- In emergencies, call emergency services (911 in the US, 112 in EU, etc.)
- Results should **NOT be used for self-medication without professional consultation**

## 🤝 Contributing

Contributions are welcome! To contribute:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is open source. Check the repository for license information.

## 👤 Author

CuraBot - Created by [adzpraize](https://github.com/adzpraize)

## 📞 Support

For issues, questions, or suggestions, please [open an issue](https://github.com/adzpraize/curabot/issues) on the GitHub repository.

---

**Last Updated**: 2026-03-25

Remember: **Health is wealth. Always prioritize professional medical consultation.**