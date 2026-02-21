# Quick Deployment Checklist for Vercel

## Pre-Deployment Checklist

- [ ] **Generate a new SECRET_KEY**
  ```python
  from django.core.management.utils import get_random_secret_key
  print(get_random_secret_key())
  ```

- [ ] **Update `.env` file** with:
  - New `SECRET_KEY`
  - `DEBUG=False`
  - `ALLOWED_HOSTS=yourdomain.vercel.app`
  - Razorpay credentials
  - PostgreSQL database URL (if using PostgreSQL)

- [ ] **Test locally**
  ```bash
  python manage.py runserver
  ```

- [ ] **Push to GitHub**
  ```bash
  git add .
  git commit -m "Prepare for Vercel deployment"
  git push
  ```

## Vercel Deployment Steps

1. **Go to** https://vercel.com/dashboard
2. **Click** "Add New Project"
3. **Import** your GitHub repository
4. **Select** project settings:
   - Framework: Other
   - Build Command: `cd Mealmate && pip install -r ../requirements.txt && python manage.py collectstatic --noinput || true`
   - Install Command: `pip install -r requirements.txt`
   - Root Directory: `.` (mealpro folder)

5. **Add Environment Variables** in Vercel:
   - `DEBUG` = `False`
   - `SECRET_KEY` = Your generated key
   - `ALLOWED_HOSTS` = your-project.vercel.app
   - `RAZORPAY_KEY_ID` = Your Razorpay key
   - `RAZORPAY_KEY_SECRET` = Your Razorpay secret
   - If using PostgreSQL:
     - `USE_POSTGRESQL` = `True`
     - `DB_NAME` = your_db_name
     - `DB_USER` = your_db_user
     - `DB_PASSWORD` = your_db_password
     - `DB_HOST` = your_db_host
     - `DB_PORT` = 5432

6. **Click Deploy** and wait for completion

## Post-Deployment

### Database Migration (if using PostgreSQL)
1. Create database tables:
   - Use a database admin tool or connect locally: `python manage.py migrate`
   - OR create tables using Vercel's preview deployments

2. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```
   Then access admin at: `https://yourdomain.vercel.app/admin/`

### Testing
- Visit `https://yourdomain.vercel.app/`
- Test user signup/signin
- Test admin panel at `/admin/`

## Common Issues & Solutions

### 502 Bad Gateway
- Check Vercel build logs
- Ensure ALLOWED_HOSTS includes your domain
- Check runtime logs in Vercel dashboard

### Static files not loading
- Clear Vercel cache and redeploy
- Verify static files were collected during build

### Database connection error
- Test connection locally first
- For PostgreSQL, check IP whitelist on database server
- Verify credentials in Vercel environment variables

## Support Resources
- [Vercel Python Documentation](https://vercel.com/docs/runtimes/python)
- [Django Deployment](https://docs.djangoproject.com/en/6.0/howto/deployment/)
- [Razorpay Integration](https://razorpay.com/docs/)
