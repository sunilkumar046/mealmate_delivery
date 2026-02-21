#!/bin/bash

# Mealmate Deployment Setup Script
# This script sets up the project for deployment to Vercel

echo "=== Mealmate Deployment Setup ==="

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run migrations
echo "Running database migrations..."
cd mealpro/Mealmate
python manage.py migrate

# Create superuser (optional)
echo "Would you like to create a superuser? (y/n)"
read -r response
if [ "$response" = "y" ]; then
    python manage.py createsuperuser
fi

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "=== Setup Complete ==="
echo "You can now deploy to Vercel!"
