import os
import subprocess
import sys

def deploy_bot():
    """Deployment script for the binary signals bot"""
    
    print("🚀 Deploying Binary Signals Bot...")
    
    # Check if required files exist
    required_files = ['bot.py', 'requirements.txt', '.env']
    for file in required_files:
        if not os.path.exists(file):
            print(f"❌ Missing required file: {file}")
            return False
    
    # Install requirements
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        return False
    
    # Start the bot
    print("🤖 Starting the bot...")
    try:
        subprocess.check_call([sys.executable, "bot.py"])
    except KeyboardInterrupt:
        print("⏹️ Bot stopped by user")
    except Exception as e:
        print(f"❌ Error running bot: {e}")
        return False
    
    return True

if __name__ == "__main__":
    deploy_bot()