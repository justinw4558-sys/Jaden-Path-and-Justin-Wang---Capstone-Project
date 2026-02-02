# Tasks: Portfolio Analytics Platform (P1 - KPI Dashboard)

**Input**: Design documents from `/specs/001-portfolio-analytics-platform/`
**Prerequisites**: plan.md, spec.md, data-model.md, contracts/openapi.yaml, research.md

**Scope**: MVP only - User Story 1 (KPI Dashboard). Stories P2-P5 deferred per clarification.

**Tests**: Not explicitly requested - test tasks omitted per spec.

## Format: `[ID] [P?] [Story?] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[US1]**: User Story 1 (KPI Dashboard)
- All paths relative to repository root

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Initialize backend and frontend project structures

- [ ] T001 Create backend directory structure: backend/src/{models,services,api}/, backend/tests/
- [ ] T002 [P] Initialize Python project with requirements.txt (FastAPI, SQLAlchemy, Pandas, python-multipart, uvicorn)
- [ ] T003 [P] Initialize frontend with Vite + React + TypeScript in frontend/
- [ ] T004 [P] Add frontend dependencies (axios, recharts, react-router-dom) to frontend/package.json

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure required before User Story 1 implementation

**⚠️ CRITICAL**: No US1 work can begin until this phase is complete

- [ ] T005 Create SQLite database connection and session management in backend/src/db.py
- [ ] T006 Create base SQLAlchemy model class in backend/src/models/base.py
- [ ] T007 [P] Create User model with password hashing in backend/src/models/user.py
- [ ] T008 [P] Create session-based auth middleware in backend/src/api/auth.py
- [ ] T009 Implement login/logout/me endpoints in backend/src/api/auth.py
- [ ] T010 Create FastAPI app with CORS and route mounting in backend/src/main.py
- [ ] T011 [P] Create API client service in frontend/src/services/api.ts
- [ ] T012 [P] Create auth context and login page in frontend/src/pages/LoginPage.tsx
- [ ] T013 Create protected route wrapper in frontend/src/components/ProtectedRoute.tsx
- [ ] T014 Setup React Router with auth flow in frontend/src/App.tsx

**Checkpoint**: Auth working - can login and access protected routes

---

## Phase 3: User Story 1 - Portfolio KPI Dashboard (Priority: P1) 🎯 MVP

**Goal**: Portfolio managers upload spreadsheets and view KPIs (NOI, occupancy, revenue/unit, expense ratio) with filtering and 12-month trends

**Independent Test**: Upload a property spreadsheet, verify KPIs display on dashboard, apply filters, click metric to see trend chart

### Backend Models (US1)

- [ ] T015 [P] [US1] Create Upload model in backend/src/models/upload.py
- [ ] T016 [P] [US1] Create Property model in backend/src/models/property.py
- [ ] T017 [P] [US1] Create FinancialRecord model in backend/src/models/financial_record.py
- [ ] T018 [P] [US1] Create KPIMetric model with MetricType enum in backend/src/models/kpi_metric.py
- [ ] T019 [US1] Create database init script that creates all tables in backend/src/db_init.py

### Backend Services (US1)

- [ ] T020 [US1] Implement spreadsheet parser (Excel/CSV) with validation in backend/src/services/file_parser.py
- [ ] T021 [US1] Implement KPI calculation service (NOI, occupancy, revenue/unit, expense ratios) in backend/src/services/kpi_calculator.py
- [ ] T022 [US1] Implement upload processing service (parse → save → calculate KPIs) in backend/src/services/upload_service.py

### Backend API Endpoints (US1)

- [ ] T023 [US1] Implement POST /uploads and GET /uploads/{id} in backend/src/api/uploads.py
- [ ] T024 [US1] Implement GET /properties with filters and GET /properties/{id} in backend/src/api/properties.py
- [ ] T025 [US1] Implement GET /properties/{id}/kpis and GET /properties/{id}/kpis/trend in backend/src/api/kpis.py
- [ ] T026 [US1] Implement GET /dashboard/summary and GET /dashboard/filters in backend/src/api/dashboard.py

### Frontend Components (US1)

- [ ] T027 [P] [US1] Create PropertyCard component displaying KPIs in frontend/src/components/PropertyCard.tsx
- [ ] T028 [P] [US1] Create KPITrendChart component using Recharts in frontend/src/components/KPITrendChart.tsx
- [ ] T029 [P] [US1] Create FilterBar component (submarket, property type dropdowns) in frontend/src/components/FilterBar.tsx
- [ ] T030 [P] [US1] Create PortfolioSummary component (aggregate stats) in frontend/src/components/PortfolioSummary.tsx
- [ ] T031 [P] [US1] Create FileUpload component with progress indicator in frontend/src/components/FileUpload.tsx

### Frontend Pages (US1)

- [ ] T032 [US1] Create DashboardPage with summary, filters, property list in frontend/src/pages/DashboardPage.tsx
- [ ] T033 [US1] Create UploadPage with file upload and status display in frontend/src/pages/UploadPage.tsx
- [ ] T034 [US1] Create PropertyDetailPage with KPIs and trend charts in frontend/src/pages/PropertyDetailPage.tsx
- [ ] T035 [US1] Add routes for dashboard, upload, and property detail to App.tsx

**Checkpoint**: P1 MVP complete - upload spreadsheet, view KPIs, filter, see trends

---

## Phase 4: Polish & Validation

**Purpose**: Final touches and validation before stakeholder demo

- [ ] T036 Add sample spreadsheet template to docs/sample-data.xlsx
- [ ] T037 Seed database with demo user (admin/admin123) in backend/src/db_init.py
- [ ] T038 Add loading states and error handling to all frontend pages
- [ ] T039 Validate against quickstart.md - ensure all steps work as documented
- [ ] T040 Manual end-to-end test: login → upload → view dashboard → filter → trend chart

---

## Dependencies & Execution Order

### Phase Dependencies

```
Phase 1 (Setup)
    ↓
Phase 2 (Foundational) ← BLOCKS all US1 work
    ↓
Phase 3 (User Story 1)
    ↓
Phase 4 (Polish)
```

### Task Dependencies Within Phases

**Phase 2**:
- T005 (db) → T006 (base model) → T007, T008 (can parallel)
- T009 depends on T007, T008
- T010 depends on T009
- T011-T14 (frontend) can parallel with T005-T10 (backend)

**Phase 3**:
- T015-T18 (models) can run in parallel → T019 (db init)
- T019 → T020-T22 (services, sequential)
- T22 → T23-T26 (API endpoints)
- T27-T31 (frontend components) can run in parallel
- T27-T31 → T32-T35 (pages depend on components)

### Parallel Opportunities

```bash
# Phase 1: All setup tasks can run in parallel
T002, T003, T004  # Python setup, React setup, frontend deps

# Phase 2: Backend and frontend can progress in parallel
T007, T008        # User model + auth middleware
T011, T012        # API client + login page

# Phase 3 Models: All models can be created in parallel
T015, T016, T017, T018  # Upload, Property, FinancialRecord, KPIMetric

# Phase 3 Frontend: All components can be built in parallel
T027, T028, T029, T030, T031  # PropertyCard, KPITrendChart, FilterBar, etc.
```

---

## Implementation Strategy

### MVP First (Recommended)

1. Complete Phase 1: Setup (T001-T004)
2. Complete Phase 2: Foundational (T005-T014)
3. Complete Phase 3: User Story 1 (T015-T035)
4. **STOP and DEMO** to stakeholders
5. If approved, complete Phase 4: Polish (T036-T040)
6. Collect feedback before starting P2 (Stoplight Ranking)

### Two-Person Team Strategy

With Justin and Jaden working together:

1. **Together**: Phase 1 setup
2. **Split**: Phase 2
   - Person A: Backend (T005-T010)
   - Person B: Frontend (T011-T014)
3. **Split**: Phase 3
   - Person A: Backend models + services + API (T015-T026)
   - Person B: Frontend components + pages (T027-T035)
4. **Together**: Phase 4 polish and demo prep

---

## Notes

- Total tasks: 40
- User Story 1 tasks: 21 (T015-T035)
- No test tasks (not explicitly requested)
- Per constitution: Tasks consolidated to reduce count while maintaining clarity
- Each task includes exact file path for implementation
- Commit after each task or logical group
- Stop at any checkpoint to validate independently
