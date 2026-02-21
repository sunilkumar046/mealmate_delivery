# Mealmate Delivery - Deployment Guide

## Prerequisites
- Vercel account (https://vercel.com)
- GitHub account (for version control)
- PostgreSQL database (recommended for production)

## Step 1: Prepare for Deployment

### 1.1 Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/your-username/mealmate-delivery.git
git branch -M main
git push -u origin main
```

### 1.2 Update Environment Variables
Copy `.env.example` to `.env` and update with your actual values:
```bash
cp .env.example .env
```

Edit `.env` and set:
- `DEBUG=False`
- `SECRET_KEY` - Generate a new secure key
- `ALLOWED_HOSTS` - Your Vercel domain
- Database credentials (if using PostgreSQL)
- Razorpay credentials

## Step 2: Deploy to Vercel

### 2.1 Connect to Vercel
1. Go to https://vercel.com/dashboard
2. Click "Add New Project"
3. Import your GitHub repository
4. Select the project root is `mealpro/`

### 2.2 Configure Build and Output Settings
- **Framework Preset**: Other
- **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
- **Output Directory**: (leave empty)
- **Install Command**: `pip install -r requirements.txt`

### 2.3 Add Environment Variables
In Project Settings → Environment Variables, add:
- `DEBUG` = `False`
- `SECRET_KEY` = Your secure secret key
- `ALLOWED_HOSTS` = Your Vercel domain
- `RAZORPAY_KEY_ID` = Your Razorpay key
- `RAZORPAY_KEY_SECRET` = Your Razorpay secret
- (Optional) PostgreSQL credentials if using PostgreSQL

### 2.4 Deploy
Click "Deploy" to start the deployment process.

## Step 3: Post-Deployment Setup

### 3.1 Run Migrations
After successful deployment, you can't directly run migrations. Instead:

**Option 1: Use a local script to create superuser**
```bash
python manage.py createsuperuser
```

**Option 2: Set up a PostgreSQL database**
Create a free PostgreSQL database on platforms like:
- Railway.app
- Render.com
- Supabase
- AWS RDS

Then set the database environment variables in Vercel.

## Important Notes

### Database
- SQLite (`db.sqlite3`) won't work on Vercel because it doesn't have persistent file storage
- Recommended: Use PostgreSQL
- Update `USE_POSTGRESQL=True` and set database credentials

### Static Files
- Django generates static files during the build process
- CSS and images are served from `Mealmate/static/`

### CSRF and Security
- For login/form submission, make sure CSRF is properly configured
- Update `ALLOWED_HOSTS` with your Vercel domain

### Razorpay Payment Gateway
- Make sure your Razorpay test keys are properly configured
- Test payment integration before going live

## Troubleshooting

### 502 Bad Gateway
- Check the deployment logs on Vercel dashboard
- Ensure `ALLOWED_HOSTS` includes your Vercel domain
- Verify environment variables are set correctly

### Static Files Not Loading
- Build command should include `python manage.py collectstatic`
- Check that static files are in `Mealmate/static/`

### Database Connection Issues
- Ensure PostgreSQL is accessible from Vercel (allow all IPs or whitelist Vercel IPs)
- Verify database credentials in environment variables

## Additional Resources
- [Vercel Django Documentation](https://vercel.com/docs)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/)
