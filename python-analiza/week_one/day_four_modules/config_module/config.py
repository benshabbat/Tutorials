"""
Configuration module containing application constants and settings.
This module stores all configuration values in one place to avoid hardcoding
values throughout the application.
"""

# Database Configuration
DATABASE_HOST = "localhost"
DATABASE_PORT = 5432
DATABASE_NAME = "myapp_db"
DATABASE_USER = "admin"
DATABASE_PASSWORD = "secret123"
DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

# API Configuration
API_BASE_URL = "https://api.example.com/v1"
API_KEY = "your-secret-api-key-here"
API_TIMEOUT = 30  # seconds
API_RETRY_ATTEMPTS = 3

# Application Settings
APP_NAME = "My Python Application"
APP_VERSION = "1.0.0"
DEBUG_MODE = True
LOG_LEVEL = "INFO"
MAX_UPLOAD_SIZE = 10 * 1024 * 1024  # 10 MB in bytes

# Security Settings
SECRET_KEY = "your-super-secret-key-for-encryption"
TOKEN_EXPIRY_HOURS = 24
PASSWORD_MIN_LENGTH = 8

# Email Configuration
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USERNAME = "your-email@gmail.com"
EMAIL_PASSWORD = "your-email-password"
EMAIL_USE_TLS = True

# File Paths
UPLOAD_FOLDER = "./uploads"
LOG_FILE_PATH = "./logs/app.log"
TEMP_FOLDER = "./temp"

# External Service URLs
PAYMENT_GATEWAY_URL = "https://payment.provider.com/api"
WEATHER_API_URL = "https://api.weather.com/v1"
NOTIFICATION_SERVICE_URL = "https://notifications.service.com/send"

# Cache Settings
CACHE_TTL = 3600  # 1 hour in seconds
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0

# Feature Flags
ENABLE_EMAIL_NOTIFICATIONS = True
ENABLE_SMS_NOTIFICATIONS = False
ENABLE_ANALYTICS = True
ENABLE_CACHING = True

# Rate Limiting
MAX_REQUESTS_PER_MINUTE = 100
MAX_LOGIN_ATTEMPTS = 5
LOCKOUT_DURATION_MINUTES = 15