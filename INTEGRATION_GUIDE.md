# Integration & Setup Guide

## Project Setup Checklist

### 1. Prerequisites
- Python 3.8+
- Node.js 14+ and npm
- Git

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment (optional but recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Data Preparation

```bash
# From project root
cd notebooks

# Generate synthetic dataset
python generate_dataset.py

# This creates: ../data/customer_churn.csv
```

### 4. Preprocessing & Feature Engineering

```bash
# From backend directory
cd ../backend
python preprocessor.py

# This creates:
# - ../data/X_train.csv
# - ../data/X_test.csv
# - ../data/y_train.csv
# - ../data/y_test.csv
# - ../models/preprocessor.pkl
```

### 5. Model Training

```bash
# From backend directory
python model_trainer.py

# This creates:
# - ../models/churn_model.pkl
# - ../models/model_results.json
```

### 6. Start Flask API

```bash
# From backend directory
python app.py

# API will be available at http://localhost:5000
```

### 7. Test API (Optional)

```bash
# In a new terminal, from backend directory
python test_api.py
```

### 8. Frontend Setup

```bash
# Navigate to frontend directory
cd ../frontend

# Install dependencies
npm install

# Start development server
npm start

# Dashboard will open at http://localhost:3000
```

## Running the Complete Project

### Terminal 1: Backend
```bash
cd backend
python app.py
```

### Terminal 2: Frontend
```bash
cd frontend
npm start
```

### Terminal 3: Optional - Monitor (not required)
```bash
# You can keep this terminal ready for debugging
```

## Testing the System

### Manual Testing

1. **Health Check**
   ```bash
   curl http://localhost:5000/health
   ```

2. **Get Model Info**
   ```bash
   curl http://localhost:5000/model-info
   ```

3. **Get Model Results**
   ```bash
   curl http://localhost:5000/model-results
   ```

### Using Dashboard

1. Navigate to http://localhost:3000
2. Use "Load High Risk Sample" or "Load Low Risk Sample" buttons
3. Modify customer data as needed
4. Click "🚀 Predict Churn" button
5. View prediction results and recommendations

## Troubleshooting

### API Not Connecting
- Ensure Flask is running on `http://localhost:5000`
- Check firewall settings
- Verify CORS is enabled in Flask

### Model Files Not Found
- Ensure you've run all preprocessing and training scripts
- Check that files exist in `../models/` directory
- Verify file paths are correct

### Frontend Not Starting
- Delete `node_modules` folder
- Run `npm install` again
- Clear npm cache: `npm cache clean --force`

### Port Already in Use
- Flask: Change port in `app.py` (last line: `port=5000`)
- React: Set `PORT=3001` before `npm start`

## Performance Optimization

### Backend
- Use production WSGI server (Gunicorn) for deployment
- Implement caching for model predictions
- Use async processing for batch predictions

### Frontend
- Build for production: `npm run build`
- Use CDN for static assets
- Enable gzip compression

## Deployment Options

### Backend (Flask)
- Heroku
- AWS Elastic Beanstalk
- Google Cloud Run
- Azure App Service

### Frontend (React)
- Vercel
- Netlify
- AWS S3 + CloudFront
- GitHub Pages

## API Rate Limiting

To add rate limiting (install flask-limiter first):
```bash
pip install Flask-Limiter
```

Then modify `app.py` to include rate limiting for production.

## Data Privacy

- Never expose raw customer data in logs
- Hash sensitive information
- Implement proper authentication for production
- Use HTTPS for all communications

## Next Steps

1. Add database persistence (PostgreSQL/MongoDB)
2. Implement user authentication
3. Add batch processing capabilities
4. Create admin dashboard for model monitoring
5. Set up CI/CD pipeline
6. Add automated testing (pytest for backend, Jest for frontend)
7. Implement logging and monitoring
8. Create API documentation (Swagger)
