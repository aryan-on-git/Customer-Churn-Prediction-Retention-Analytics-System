# Deployment Guide

## Pre-Deployment Checklist

- [ ] All tests passing
- [ ] Code reviewed
- [ ] Documentation updated
- [ ] Environment variables configured
- [ ] Database backups created
- [ ] Load testing completed

## Backend Deployment

### Option 1: Heroku Deployment

1. **Install Heroku CLI**
   ```bash
   curl https://cli.heroku.com/install.sh | sh
   ```

2. **Create Heroku App**
   ```bash
   heroku login
   heroku create your-app-name
   ```

3. **Add Procfile**
   ```
   web: gunicorn backend.app:app
   ```

4. **Deploy**
   ```bash
   git push heroku main
   ```

### Option 2: AWS Elastic Beanstalk

1. **Install EB CLI**
   ```bash
   pip install awsebcli
   ```

2. **Initialize**
   ```bash
   eb init -p python-3.9 churn-api
   ```

3. **Create environment**
   ```bash
   eb create production
   ```

4. **Deploy**
   ```bash
   eb deploy
   ```

### Option 3: Docker Deployment

1. **Create Dockerfile** (backend)
   ```dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY backend/requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   EXPOSE 5000
   CMD ["python", "backend/app.py"]
   ```

2. **Build and run**
   ```bash
   docker build -t churn-api .
   docker run -p 5000:5000 churn-api
   ```

## Frontend Deployment

### Option 1: Vercel (Recommended for React)

1. **Install Vercel CLI**
   ```bash
   npm i -g vercel
   ```

2. **Deploy**
   ```bash
   cd frontend
   vercel
   ```

### Option 2: Netlify

1. **Build**
   ```bash
   cd frontend
   npm run build
   ```

2. **Deploy**
   ```bash
   npm install -g netlify-cli
   netlify deploy --prod --dir=build
   ```

### Option 3: AWS S3 + CloudFront

1. **Build**
   ```bash
   cd frontend
   npm run build
   ```

2. **Create S3 bucket**
   ```bash
   aws s3 mb s3://your-bucket-name
   ```

3. **Upload build**
   ```bash
   aws s3 sync build/ s3://your-bucket-name/
   ```

4. **Create CloudFront distribution**
   - Point to S3 bucket
   - Enable HTTPS
   - Set index.html as default

## Environment Variables

### Backend (.env)
```
FLASK_ENV=production
FLASK_DEBUG=False
API_PORT=5000
DATABASE_URL=postgresql://user:pass@host/db
SECRET_KEY=your-secret-key
```

### Frontend (.env.production)
```
REACT_APP_API_URL=https://api.yourdomain.com
REACT_APP_ENV=production
```

## Database Setup

### PostgreSQL (Production Recommended)

```sql
CREATE DATABASE churn_db;
CREATE USER churn_user WITH PASSWORD 'secure_password';
GRANT ALL PRIVILEGES ON DATABASE churn_db TO churn_user;
```

### Connection String
```
postgresql://churn_user:password@localhost:5432/churn_db
```

## SSL/HTTPS

All production deployments must use HTTPS:

1. **AWS Certificate Manager**
   - Request free SSL certificate
   - Associate with CloudFront or ALB

2. **Let's Encrypt**
   ```bash
   sudo apt-get install certbot
   sudo certbot certonly -d yourdomain.com
   ```

## Monitoring & Logging

### Application Monitoring
```python
# Add to Flask app
from prometheus_client import Counter, Histogram
import time

request_count = Counter('requests_total', 'Total requests')
request_time = Histogram('request_duration_seconds', 'Request duration')
```

### Log Aggregation
- CloudWatch (AWS)
- Stackdriver (GCP)
- ELK Stack (self-hosted)

### Error Tracking
- Sentry
- New Relic
- Datadog

## Performance Optimization

### Backend
- Use caching (Redis)
- Implement async workers
- Database query optimization
- Load balancing (Gunicorn + Nginx)

### Frontend
- Code splitting
- Lazy loading
- Image optimization
- CDN caching

### API Rate Limiting
```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=lambda: request.remote_addr)

@app.route('/predict')
@limiter.limit("10 per minute")
def predict():
    pass
```

## Backup Strategy

### Database Backups
```bash
# Daily automated backups
pg_dump churn_db > backup_$(date +%Y%m%d).sql

# Restore
psql churn_db < backup_20240101.sql
```

### Model Backups
- Version control all models
- Archive to S3
- Test restore procedure

## Rollback Procedure

```bash
# If deployment fails
git revert <commit-hash>
git push heroku main

# Or restart previous version
docker run -d -p 5000:5000 churn-api:previous-version
```

## Security Checklist

- [ ] HTTPS enabled
- [ ] API keys secured
- [ ] Database credentials in environment variables
- [ ] No sensitive data in logs
- [ ] SQL injection prevention verified
- [ ] CORS properly configured
- [ ] Rate limiting enabled
- [ ] Regular security updates

## Scaling Strategy

### Horizontal Scaling
- Load balancer (Nginx, HAProxy)
- Multiple API instances
- Caching layer (Redis)

### Vertical Scaling
- Increase server resources
- Optimize database queries
- Use async processing

## Cost Optimization

- Use spot instances for non-critical tasks
- Implement request caching
- Compress API responses
- Optimize image sizes
- Clean up unused resources

## Support & Maintenance

- Monitor uptime (StatusPage.io)
- Regular security patches
- Dependency updates
- Performance benchmarking
- User feedback collection

## Contact & Support

For deployment issues, contact: devops@yourdomain.com
