"""
Configuration settings for Resume Relevance Check System
"""
import os
from pathlib import Path

# Try importing Streamlit secrets
try:
    import streamlit as st
    SECRETS = st.secrets
except Exception:
    SECRETS = {}

class Config:
    """Application configuration"""

    # Project paths
    PROJECT_ROOT = Path(__file__).parent.parent
    DATA_DIR = PROJECT_ROOT / "data"
    UPLOADS_DIR = DATA_DIR / "uploads"
    RESUMES_DIR = UPLOADS_DIR / "resumes"
    JD_DIR = UPLOADS_DIR / "job_descriptions"
    PROCESSED_DIR = DATA_DIR / "processed"
    VECTOR_DB_DIR = DATA_DIR / "vector_db"

    # API Keys (check st.secrets first, fallback to os.environ)
    GOOGLE_API_KEY = SECRETS.get("GOOGLE_API_KEY") or os.getenv("GOOGLE_API_KEY")
    LANGCHAIN_API_KEY = SECRETS.get("LANGCHAIN_API_KEY") or os.getenv("LANGCHAIN_API_KEY", "")

    # App settings
    APP_NAME = os.getenv("APP_NAME", "Resume Relevance Check System")
    APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
    DEBUG_MODE = os.getenv("DEBUG_MODE", "true").lower() == "true"

    # File upload settings
    MAX_FILE_SIZE_MB = int(os.getenv("MAX_FILE_SIZE_MB", "10"))
    ALLOWED_EXTENSIONS = os.getenv("ALLOWED_EXTENSIONS", "pdf,docx").split(",")

    # Scoring config
    KEYWORD_WEIGHT = float(os.getenv("KEYWORD_WEIGHT", "0.4"))
    SEMANTIC_WEIGHT = float(os.getenv("SEMANTIC_WEIGHT", "0.6"))
    MIN_RELEVANCE_SCORE = int(os.getenv("MIN_RELEVANCE_SCORE", "30"))

    # LangChain settings
    LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2", "false").lower() == "true"

    @classmethod
    def validate_config(cls):
        """Check API key availability"""
        if not cls.GOOGLE_API_KEY:
            print("⚠️ WARNING: GOOGLE_API_KEY is missing! The app may not work correctly.")
            return False
        return True

# Don’t crash the app — just warn
Config.validate_config()
