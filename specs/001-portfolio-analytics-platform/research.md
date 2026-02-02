# Research: Portfolio Analytics Platform (P1 - KPI Dashboard)

**Date**: 2026-02-02
**Scope**: Technical decisions for MVP (P1 only)

## Technology Decisions

### 1. Backend Framework: FastAPI

**Decision**: Use FastAPI with Python 3.11

**Rationale**:
- Built-in OpenAPI/Swagger documentation (reduces separate API docs effort)
- Native async support for file upload processing
- Pydantic for data validation (catches spreadsheet format issues early)
- Strong typing improves maintainability
- Widely adopted, good ecosystem for data processing

**Alternatives Considered**:
- Flask: Simpler but requires more boilerplate for validation and docs
- Django: Overkill for API-only backend; ORM is heavier than needed
- Express.js: Would require team to context-switch between Python (Pandas) and Node

### 2. Frontend Framework: React with TypeScript

**Decision**: Use React 18 with TypeScript and Vite

**Rationale**:
- Component-based architecture suits dashboard with reusable cards/charts
- Large ecosystem for charting (Recharts integrates well)
- TypeScript catches type errors before runtime
- Vite provides fast development builds
- Team familiarity (common in modern web development)

**Alternatives Considered**:
- Vue.js: Good alternative, slightly smaller ecosystem for enterprise dashboards
- Vanilla JS: More boilerplate for reactive updates, harder to maintain
- Next.js: SSR not needed for internal dashboard tool

### 3. Database: SQLite

**Decision**: Use SQLite for PoC storage

**Rationale**:
- Zero configuration (no DB server to install/maintain)
- File-based (easy backup, easy to reset during development)
- Sufficient for 100 properties with 12 months of data (~1200 financial records)
- Can migrate to PostgreSQL later if needed (SQLAlchemy abstracts this)
- Reduces deployment complexity for PoC

**Alternatives Considered**:
- PostgreSQL: Production-ready but requires server setup, overkill for PoC
- JSON files: Harder to query, no relational integrity
- MongoDB: NoSQL unnecessary when data is clearly relational

### 4. Data Processing: Pandas

**Decision**: Use Pandas for spreadsheet parsing and KPI calculations

**Rationale**:
- Native Excel/CSV reading with `read_excel()` and `read_csv()`
- Vectorized operations for fast KPI calculations
- Industry standard for financial data processing
- Good handling of missing data (critical for incomplete property records)

**Alternatives Considered**:
- openpyxl alone: Lower level, more code for calculations
- Polars: Faster but less mature, fewer examples for real estate domain

### 5. Charting: Recharts

**Decision**: Use Recharts for dashboard visualizations

**Rationale**:
- React-native (components, not imperative API)
- Good defaults for line charts (historical trends) and bar charts (comparisons)
- Responsive out of the box
- Simpler than D3.js for standard chart types

**Alternatives Considered**:
- D3.js: More powerful but lower-level, overkill for standard KPI charts
- Chart.js: Canvas-based, less React-friendly
- Plotly: Heavier bundle size, more suited for scientific visualization

### 6. Authentication: Simple Session-Based

**Decision**: Basic session authentication for PoC

**Rationale**:
- Single-tenant (PHMS only), no multi-org complexity
- Session cookies are simple and well-understood
- Can upgrade to OAuth/SSO in future iterations if needed
- Reduces implementation time for MVP

**Alternatives Considered**:
- OAuth2/Auth0: Enterprise-ready but adds complexity for internal tool
- JWT: Stateless but adds token refresh complexity
- No auth: Rejected - spec requires authentication (FR-029)

## KPI Calculation Formulas

For reproducibility (Constitution Principle II), documenting exact formulas:

### Net Operating Income (NOI)
```
NOI = Total Revenue - Operating Expenses
    = (Rental Income + Other Income) - (Maintenance + Utilities + Administrative + Insurance + Taxes)
```

### Occupancy Rate
```
Occupancy Rate = (Occupied Units / Total Units) × 100%
```

### Revenue Per Unit
```
Revenue Per Unit = Total Revenue / Total Units
                 = (Monthly Rental Income × 12 + Other Annual Income) / Unit Count
```

### Expense Ratio
```
Expense Ratio = Operating Expenses / Total Revenue × 100%

By Category:
  Maintenance Ratio = Maintenance Expenses / Total Revenue × 100%
  Utilities Ratio = Utilities Expenses / Total Revenue × 100%
  Administrative Ratio = Administrative Expenses / Total Revenue × 100%
```

## Spreadsheet Format Requirements

Based on spec assumption that data follows "standard real estate accounting categories":

**Required Columns (Property Sheet)**:
- Property ID (unique identifier)
- Property Name
- Address (street, city, state, zip)
- Total Units
- Property Type (e.g., Apartment, Condo)
- Submarket
- Acquisition Date

**Required Columns (Financial Sheet)**:
- Property ID (foreign key)
- Reporting Period (YYYY-MM format)
- Rental Income
- Other Income
- Maintenance Expense
- Utilities Expense
- Administrative Expense
- Insurance Expense
- Property Tax
- Occupied Units

**Validation Rules**:
- Property ID must exist in Property sheet
- Reporting Period must be valid date format
- All financial values must be non-negative numbers
- Occupied Units cannot exceed Total Units

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Spreadsheet format varies | High | Medium | Provide template, validate on upload with clear error messages |
| KPI calculation errors | Medium | High | Unit tests with known values, manual spot-check before demo |
| SQLite performance at scale | Low | Low | Monitor query times, have PostgreSQL migration path |
| Auth bypass | Low | Medium | Session validation on all API routes, no sensitive data in URLs |

## Open Questions (Resolved)

All technical clarifications resolved. No blockers for Phase 1 design.
