#!/bin/bash
# Quick start script for the project

echo "=========================================="
echo "Customer Churn Prediction System - Quick Start"
echo "=========================================="
echo ""

# Color codes
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check Python
echo -e "${YELLOW}Checking Python installation...${NC}"
if ! command -v python &> /dev/null; then
    echo "Error: Python is not installed"
    exit 1
fi
echo -e "${GREEN}✓ Python found$(python --version)${NC}"

# Check Node
echo -e "${YELLOW}Checking Node.js installation...${NC}"
if ! command -v node &> /dev/null; then
    echo "Error: Node.js is not installed"
    exit 1
fi
echo -e "${GREEN}✓ Node.js found: $(node --version)${NC}"

# Setup backend
echo ""
echo -e "${YELLOW}Setting up backend...${NC}"
cd backend
pip install -r requirements.txt
echo -e "${GREEN}✓ Backend dependencies installed${NC}"

# Run preprocessing
echo ""
echo -e "${YELLOW}Generating dataset and preprocessing...${NC}"
python ../notebooks/generate_dataset.py
python preprocessor.py
echo -e "${GREEN}✓ Data preprocessing completed${NC}"

# Train models
echo ""
echo -e "${YELLOW}Training models...${NC}"
python model_trainer.py
echo -e "${GREEN}✓ Models trained successfully${NC}"

# Setup frontend
echo ""
echo -e "${YELLOW}Setting up frontend...${NC}"
cd ../frontend
npm install
echo -e "${GREEN}✓ Frontend dependencies installed${NC}"

echo ""
echo -e "${GREEN}=========================================="
echo "Setup completed successfully!"
echo "=========================================="
echo ""
echo "To run the project, open two terminals:"
echo ""
echo "Terminal 1 (Backend):"
echo "  cd backend"
echo "  python app.py"
echo ""
echo "Terminal 2 (Frontend):"
echo "  cd frontend"
echo "  npm start"
echo ""
echo "Then open http://localhost:3000 in your browser"
echo "=========================================="
