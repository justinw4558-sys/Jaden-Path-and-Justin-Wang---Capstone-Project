# Quickstart: Portfolio Analytics Platform (P1 - KPI Dashboard)

This guide walks through setting up and running the Portfolio KPI Dashboard locally.

## Prerequisites

- Python 3.11+
- Node.js 18+ and npm
- Git

## Project Setup

### 1. Clone and Navigate

```bash
git clone <repository-url>
cd Jaden-Path-and-Justin-Wang---Capstone-Project
git checkout 001-portfolio-analytics-platform
```

### 2. Backend Setup

```bash
# Create and activate virtual environment
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Initialize database (creates SQLite file)
python -m src.db.init

# Run backend server
uvicorn src.main:app --reload --port 8000
```

Backend will be available at `http://localhost:8000`
- API docs: `http://localhost:8000/docs` (Swagger UI)
- Health check: `http://localhost:8000/health`

### 3. Frontend Setup

```bash
# In a new terminal
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

Frontend will be available at `http://localhost:5173`

## First Use

### 1. Login

Default development credentials:
- Username: `admin`
- Password: `admin123`

### 2. Upload Property Data

1. Click "Upload Data" in the dashboard
2. Select your Excel (.xlsx) or CSV file
3. Wait for processing to complete (status shown)

**Required spreadsheet format** (see `specs/001-portfolio-analytics-platform/research.md` for details):

Property columns: `Property ID`, `Property Name`, `Address`, `City`, `State`, `ZIP`, `Total Units`, `Property Type`, `Submarket`, `Acquisition Date`

Financial columns: `Property ID`, `Period`, `Rental Income`, `Other Income`, `Maintenance`, `Utilities`, `Administrative`, `Insurance`, `Property Tax`, `Occupied Units`

### 3. View Dashboard

After upload completes:
- Portfolio summary shows at top
- Properties listed with KPIs
- Click any property for details
- Click any metric for 12-month trend chart
- Use filters to narrow by submarket or property type

## Running Tests

### Backend Tests

```bash
cd backend
source venv/bin/activate
pytest
```

### Frontend Tests

```bash
cd frontend
npm test
```

## Development Workflow

1. Backend changes auto-reload with `--reload` flag
2. Frontend changes hot-reload with Vite
3. Database is SQLite file at `backend/data/portfolio.db`
4. To reset database: delete the file and re-run init script

## Common Issues

**Upload fails with "Invalid format"**
- Ensure columns match expected names exactly
- Check that Property ID values are unique
- Verify all financial values are numbers (no currency symbols)

**KPIs show as 0 or null**
- Check that financial data includes the Property ID
- Ensure period format is YYYY-MM (e.g., 2026-01)
- Verify occupied units does not exceed total units

**Login fails**
- Ensure backend is running on port 8000
- Check browser console for CORS errors
- Clear cookies and retry

## API Quick Reference

| Action | Method | Endpoint |
|--------|--------|----------|
| Login | POST | `/api/v1/auth/login` |
| Upload file | POST | `/api/v1/uploads` |
| List properties | GET | `/api/v1/properties` |
| Get property KPIs | GET | `/api/v1/properties/{id}/kpis` |
| Get KPI trend | GET | `/api/v1/properties/{id}/kpis/trend?metric=noi` |
| Dashboard summary | GET | `/api/v1/dashboard/summary` |

Full API documentation: `http://localhost:8000/docs`

## Next Steps

After P1 validation with stakeholders:
- P2: Stoplight Ranking System
- P3: Geographic Opportunity Mapping
- P4: Cost Structure Analysis
- P5: Acquisition Screening
