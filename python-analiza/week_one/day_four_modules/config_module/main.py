"""
Main application script demonstrating the use of config module.
This script imports and uses configuration constants from config.py
instead of hardcoding values.
"""

# Import all constants from config module
import config

# Alternative import methods:
# from config import DATABASE_URL, API_KEY, APP_NAME  # Import specific constants
# import config as cfg  # Import with alias

def connect_to_database():
    """Simulate database connection using config constants."""
    print("🔗 Connecting to database...")
    print(f"   Host: {config.DATABASE_HOST}")
    print(f"   Port: {config.DATABASE_PORT}")
    print(f"   Database: {config.DATABASE_NAME}")
    print(f"   User: {config.DATABASE_USER}")
    print(f"   Full URL: {config.DATABASE_URL}")
    print("   ✅ Database connection established!\n")

def make_api_request():
    """Simulate API request using config constants."""
    print("🌐 Making API request...")
    print(f"   Base URL: {config.API_BASE_URL}")
    print(f"   API Key: {config.API_KEY[:8]}...")  # Show only first 8 characters for security
    print(f"   Timeout: {config.API_TIMEOUT} seconds")
    print(f"   Retry attempts: {config.API_RETRY_ATTEMPTS}")
    print("   ✅ API request completed!\n")

def setup_application():
    """Setup application using config constants."""
    print("⚙️  Setting up application...")
    print(f"   App Name: {config.APP_NAME}")
    print(f"   Version: {config.APP_VERSION}")
    print(f"   Debug Mode: {config.DEBUG_MODE}")
    print(f"   Log Level: {config.LOG_LEVEL}")
    print(f"   Max Upload Size: {config.MAX_UPLOAD_SIZE / (1024*1024):.1f} MB")
    print("   ✅ Application setup complete!\n")

def setup_email_service():
    """Setup email service using config constants."""
    print("📧 Setting up email service...")
    print(f"   SMTP Host: {config.EMAIL_HOST}")
    print(f"   SMTP Port: {config.EMAIL_PORT}")
    print(f"   Username: {config.EMAIL_USERNAME}")
    print(f"   Use TLS: {config.EMAIL_USE_TLS}")
    print("   ✅ Email service configured!\n")

def check_feature_flags():
    """Check feature flags from config."""
    print("🚩 Feature Flags Status:")
    print(f"   Email Notifications: {'✅ Enabled' if config.ENABLE_EMAIL_NOTIFICATIONS else '❌ Disabled'}")
    print(f"   SMS Notifications: {'✅ Enabled' if config.ENABLE_SMS_NOTIFICATIONS else '❌ Disabled'}")
    print(f"   Analytics: {'✅ Enabled' if config.ENABLE_ANALYTICS else '❌ Disabled'}")
    print(f"   Caching: {'✅ Enabled' if config.ENABLE_CACHING else '❌ Disabled'}")
    print()

def display_security_settings():
    """Display security-related settings."""
    print("🔒 Security Settings:")
    print(f"   Token Expiry: {config.TOKEN_EXPIRY_HOURS} hours")
    print(f"   Password Min Length: {config.PASSWORD_MIN_LENGTH} characters")
    print(f"   Max Login Attempts: {config.MAX_LOGIN_ATTEMPTS}")
    print(f"   Lockout Duration: {config.LOCKOUT_DURATION_MINUTES} minutes")
    print(f"   Max Requests/Minute: {config.MAX_REQUESTS_PER_MINUTE}")
    print()

def main():
    """Main function demonstrating config usage."""
    print("=" * 60)
    print("🐍 PYTHON CONFIG MODULE DEMONSTRATION")
    print("=" * 60)
    print()
    
    # Use config constants instead of hardcoded values
    connect_to_database()
    make_api_request()
    setup_application()
    setup_email_service()
    check_feature_flags()
    display_security_settings()
    
    print("💡 Benefits of using config module:")
    print("   ✅ Centralized configuration management")
    print("   ✅ Easy to modify settings without changing code")
    print("   ✅ Better security (config can be environment-specific)")
    print("   ✅ Improved maintainability")
    print("   ✅ No hardcoded values scattered throughout code")
    print()
    
    print("🔧 Best Practices:")
    print("   • Keep sensitive data in environment variables")
    print("   • Use different config files for different environments")
    print("   • Document all configuration options")
    print("   • Use meaningful constant names")
    print("   • Group related constants together")

if __name__ == "__main__":
    main()