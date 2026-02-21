#!/usr/bin/env python
"""
Utility script to generate configuration values for Vercel deployment
"""

import secrets
import string
from pathlib import Path


def generate_secret_key():
    """Generate a new Django SECRET_KEY"""
    chars = string.ascii_letters + string.digits + string.punctuation
    secret_key = ''.join(secrets.choice(chars) for _ in range(50))
    return secret_key


def generate_env_file():
    """Generate .env file from .env.example"""
    example_file = Path('.env.example')
    env_file = Path('.env')
    
    if example_file.exists():
        content = example_file.read_text()
        # Replace the placeholder with a real secret key
        content = content.replace(
            'your-secret-key-here',
            generate_secret_key()
        )
        env_file.write_text(content)
        print(f"✅ Created {env_file} from {example_file}")
        print("\n⚠️  IMPORTANT: Edit .env and fill in your actual values:")
        print("   - ALLOWED_HOSTS (your Vercel domain)")
        print("   - RAZORPAY_KEY_ID and RAZORPAY_KEY_SECRET")
        print("   - Database credentials (if using PostgreSQL)")
    else:
        print("❌ .env.example not found!")


def print_secret_key():
    """Print a new secret key"""
    secret_key = generate_secret_key()
    print("\n🔐 Generated Django SECRET_KEY:")
    print(f"   {secret_key}")
    print("\nCopy this value to your Vercel environment variables!")


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == '--generate-env':
            generate_env_file()
        elif sys.argv[1] == '--secret-key':
            print_secret_key()
    else:
        print("🚀 Mealmate Deployment Setup Utility\n")
        print("Usage:")
        print("  python deploy_setup.py --secret-key    # Generate SECRET_KEY")
        print("  python deploy_setup.py --generate-env   # Generate .env file")
        print("\nOR run without arguments for interactive setup:")
        print("\n1. Generate Secret Key? (y=yes, n=skip)")
        response = input().lower()
        if response == 'y':
            print_secret_key()
        
        print("\n2. Generate .env file? (y=yes, n=skip)")
        response = input().lower()
        if response == 'y':
            generate_env_file()
