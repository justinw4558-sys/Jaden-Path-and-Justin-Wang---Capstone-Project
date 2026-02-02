# Data Model: Portfolio Analytics Platform (P1 - KPI Dashboard)

**Date**: 2026-02-02
**Scope**: MVP entities for P1 (KPI Dashboard only)

## Entity Relationship Diagram

```
┌─────────────────┐       ┌─────────────────────┐       ┌─────────────────┐
│     Upload      │       │      Property       │       │  FinancialRecord│
├─────────────────┤       ├─────────────────────┤       ├─────────────────┤
│ id (PK)         │       │ id (PK)             │       │ id (PK)         │
│ filename        │──────<│ upload_id (FK)      │>──────│ property_id (FK)│
│ uploaded_at     │       │ external_id         │       │ period          │
│ uploaded_by     │       │ name                │       │ rental_income   │
│ row_count       │       │ address_*           │       │ other_income    │
│ status          │       │ total_units         │       │ maintenance_exp │
└─────────────────┘       │ property_type       │       │ utilities_exp   │
                          │ submarket           │       │ admin_exp       │
                          │ acquisition_date    │       │ insurance_exp   │
                          └─────────────────────┘       │ property_tax    │
                                    │                   │ occupied_units  │
                                    │                   │ created_at      │
                                    │                   └─────────────────┘
                                    │
                                    v
                          ┌─────────────────────┐
                          │      KPIMetric      │
                          ├─────────────────────┤
                          │ id (PK)             │
                          │ property_id (FK)    │
                          │ period              │
                          │ metric_type         │
                          │ value               │
                          │ calculated_at       │
                          └─────────────────────┘
```

## Entities

### Upload

Tracks each spreadsheet upload for data traceability (Constitution Principle II).

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | UUID | PK | Unique identifier |
| filename | String(255) | NOT NULL | Original filename |
| uploaded_at | DateTime | NOT NULL, DEFAULT NOW | Upload timestamp |
| uploaded_by | String(100) | NOT NULL | Username who uploaded |
| row_count | Integer | NOT NULL | Number of property rows processed |
| status | Enum | NOT NULL | 'processing', 'completed', 'failed' |
| error_message | Text | NULLABLE | Error details if status='failed' |

### Property

Core entity representing a multifamily residential asset.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | UUID | PK | Internal unique identifier |
| upload_id | UUID | FK → Upload.id, NOT NULL | Source upload for traceability |
| external_id | String(50) | UNIQUE, NOT NULL | ID from spreadsheet |
| name | String(255) | NOT NULL | Property name |
| address_street | String(255) | NOT NULL | Street address |
| address_city | String(100) | NOT NULL | City |
| address_state | String(2) | NOT NULL | State code (e.g., 'CA') |
| address_zip | String(10) | NOT NULL | ZIP code |
| total_units | Integer | NOT NULL, > 0 | Total unit count |
| property_type | String(50) | NOT NULL | e.g., 'Apartment', 'Condo' |
| submarket | String(100) | NULLABLE | Submarket classification |
| acquisition_date | Date | NULLABLE | Date property was acquired |
| created_at | DateTime | NOT NULL, DEFAULT NOW | Record creation time |
| updated_at | DateTime | NOT NULL, DEFAULT NOW | Last update time |

**Indexes**:
- `idx_property_external_id` on (external_id) - for spreadsheet lookups
- `idx_property_submarket` on (submarket) - for filtering

### FinancialRecord

Periodic financial data for a property (monthly granularity).

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | UUID | PK | Unique identifier |
| property_id | UUID | FK → Property.id, NOT NULL | Parent property |
| period | String(7) | NOT NULL | 'YYYY-MM' format |
| rental_income | Decimal(12,2) | NOT NULL, >= 0 | Monthly rental income |
| other_income | Decimal(12,2) | NOT NULL, DEFAULT 0 | Non-rental income |
| maintenance_exp | Decimal(12,2) | NOT NULL, DEFAULT 0 | Maintenance expenses |
| utilities_exp | Decimal(12,2) | NOT NULL, DEFAULT 0 | Utilities expenses |
| admin_exp | Decimal(12,2) | NOT NULL, DEFAULT 0 | Administrative expenses |
| insurance_exp | Decimal(12,2) | NOT NULL, DEFAULT 0 | Insurance expenses |
| property_tax | Decimal(12,2) | NOT NULL, DEFAULT 0 | Property taxes |
| occupied_units | Integer | NOT NULL, >= 0 | Units currently occupied |
| created_at | DateTime | NOT NULL, DEFAULT NOW | Record creation time |

**Constraints**:
- UNIQUE (property_id, period) - one record per property per month
- CHECK (occupied_units <= Property.total_units) - enforced at application layer

**Indexes**:
- `idx_financial_property_period` on (property_id, period) - for trend queries

### KPIMetric

Calculated KPI values (derived from FinancialRecord, stored for performance).

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | UUID | PK | Unique identifier |
| property_id | UUID | FK → Property.id, NOT NULL | Parent property |
| period | String(7) | NOT NULL | 'YYYY-MM' format |
| metric_type | Enum | NOT NULL | See Metric Types below |
| value | Decimal(15,4) | NOT NULL | Calculated value |
| calculated_at | DateTime | NOT NULL, DEFAULT NOW | Calculation timestamp |

**Metric Types** (enum values):
- `noi` - Net Operating Income (dollars)
- `occupancy_rate` - Occupancy percentage (0-100)
- `revenue_per_unit` - Revenue per unit (dollars)
- `expense_ratio` - Total expense ratio (0-100)
- `maintenance_ratio` - Maintenance expense ratio (0-100)
- `utilities_ratio` - Utilities expense ratio (0-100)
- `admin_ratio` - Administrative expense ratio (0-100)

**Constraints**:
- UNIQUE (property_id, period, metric_type) - one value per KPI per period

**Indexes**:
- `idx_kpi_property_type_period` on (property_id, metric_type, period DESC) - for trend charts

### User (Simplified for PoC)

Basic user for authentication. Full RBAC deferred to post-MVP.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | UUID | PK | Unique identifier |
| username | String(100) | UNIQUE, NOT NULL | Login username |
| password_hash | String(255) | NOT NULL | Hashed password |
| role | Enum | NOT NULL, DEFAULT 'analyst' | 'executive', 'portfolio_manager', 'analyst' |
| created_at | DateTime | NOT NULL, DEFAULT NOW | Account creation time |
| last_login | DateTime | NULLABLE | Last successful login |

## State Transitions

### Upload Status

```
[Created] → processing → completed
                      ↘ failed
```

- `processing`: File received, parsing/validation in progress
- `completed`: All rows processed, KPIs calculated
- `failed`: Validation error or processing failure (see error_message)

## Data Retention

- **Raw financial data**: Retained indefinitely (Constitution: preserve original values)
- **KPI metrics**: Recalculated on each upload; old metrics for same period replaced
- **Uploads**: Retained for audit trail; files not stored (only metadata)

## Migration Notes

For SQLite PoC:
- UUIDs stored as TEXT (36 characters)
- Decimals stored as REAL (sufficient precision for dollar amounts)
- Enums stored as TEXT with application-layer validation

Future PostgreSQL migration:
- Use native UUID type
- Use NUMERIC for decimals
- Use native ENUM types
