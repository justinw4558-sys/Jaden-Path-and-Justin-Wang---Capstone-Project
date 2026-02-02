# Implementation Plan: Portfolio Analytics Platform (P1 - KPI Dashboard)

**Branch**: `001-portfolio-analytics-platform` | **Date**: 2026-02-02 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-portfolio-analytics-platform/spec.md`

## Summary

Build a Portfolio KPI Dashboard that allows portfolio managers to upload property spreadsheets
and immediately view calculated performance metrics (NOI, occupancy, revenue/unit, expense
ratios) with filtering and 12-month historical trends. This is the P1 MVP - all other features
(stoplight ranking, maps, cost analysis, acquisition screening) are deferred to future iterations.

## Technical Context

**Language/Version**: Python 3.11 (backend), TypeScript 5.x (frontend)
**Primary Dependencies**: FastAPI (API), React (UI), Pandas (calculations), Recharts (charts)
**Storage**: SQLite (PoC - simple, no separate DB server needed)
**Testing**: pytest (backend), Vitest (frontend)
**Target Platform**: Web browser (modern Chrome, Firefox, Safari, Edge)
**Project Type**: Web application (frontend + backend)
**Performance Goals**: Dashboard loads in <3 seconds, upload processes 100 properties in <5 minutes
**Constraints**: Single-tenant (PHMS only), on-upload recalculation, 12-month historical depth
**Scale/Scope**: ~50-100 properties, ~5 concurrent users, single organization

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Requirement | Status | Evidence |
|-----------|-------------|--------|----------|
| I. PoC-First | Start with minimal working prototype | ✅ PASS | P1 only, deferred P2-P5 |
| I. PoC-First | Working demonstration before documentation | ✅ PASS | Dashboard is functional deliverable |
| II. Data Integrity | Data sources documented | ✅ PASS | Upload tracks source file + date |
| II. Data Integrity | Calculations reproducible | ✅ PASS | Same input → same KPI output |
| II. Data Integrity | Original values preserved | ✅ PASS | Raw data stored alongside derived |
| III. Iterative Simplicity | Solve demonstrated problem | ✅ PASS | Replaces manual spreadsheet analysis |
| III. Iterative Simplicity | Deliver standalone value | ✅ PASS | KPI dashboard usable alone |
| IV. User Validation Gates | Tasks reviewed before implementation | ⏳ PENDING | Will confirm with stakeholder |

**Gate Result**: PASS (pending task review per constitution)

## Project Structure

### Documentation (this feature)

```text
specs/001-portfolio-analytics-platform/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output (OpenAPI spec)
└── tasks.md             # Phase 2 output (/speckit.tasks)
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── models/          # SQLAlchemy models (Property, FinancialRecord, KPIMetric)
│   ├── services/        # Business logic (KPI calculations, file parsing)
│   ├── api/             # FastAPI routes
│   └── main.py          # Application entry point
├── tests/
│   ├── unit/            # Service unit tests
│   └── integration/     # API integration tests
└── requirements.txt

frontend/
├── src/
│   ├── components/      # React components (Dashboard, PropertyCard, KPIChart)
│   ├── pages/           # Page components (DashboardPage, UploadPage)
│   ├── services/        # API client
│   └── App.tsx          # Root component
├── tests/
└── package.json
```

**Structure Decision**: Web application (Option 2) - separate frontend and backend for clear
separation of concerns. Backend handles data processing and API; frontend handles visualization.

## Complexity Tracking

> No constitution violations requiring justification. Tech choices are minimal for PoC scope.

| Decision | Rationale | Simpler Alternative Considered |
|----------|-----------|-------------------------------|
| SQLite over PostgreSQL | No DB server setup, sufficient for 100 properties | File-based JSON (rejected: harder to query) |
| FastAPI over Flask | Built-in OpenAPI docs, async support | Flask (acceptable but less modern) |
| React over vanilla JS | Component reuse, ecosystem | Vanilla (rejected: more boilerplate for dashboards) |
