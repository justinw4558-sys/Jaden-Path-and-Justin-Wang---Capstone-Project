# Feature Specification: Portfolio Analytics Platform

**Feature Branch**: `001-portfolio-analytics-platform`
**Created**: 2026-02-02
**Status**: Draft
**Input**: User description: "PRD.md - Portfolio Analytics Platform for PHMS Real Estate"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Portfolio KPI Dashboard (Priority: P1)

A portfolio manager logs into the platform and immediately sees a dashboard displaying core
performance metrics (NOI, occupancy rates, revenue per unit, expense ratios) for all properties.
They can filter by property, date range, and asset characteristics to focus on specific segments
of the portfolio. Visual indicators highlight properties that deviate from targets.

**Why this priority**: This is the foundation of the platform. Without automated KPI calculations
and visualization, users cannot identify performance issues. This delivers immediate value by
replacing hours of manual spreadsheet work with instant insights.

**Independent Test**: Can be fully tested by uploading portfolio data and verifying that KPIs
calculate correctly and display in the dashboard. Delivers value as a standalone analytics tool.

**Acceptance Scenarios**:

1. **Given** a portfolio manager with uploaded property data, **When** they access the dashboard,
   **Then** they see all core KPIs (NOI, occupancy, revenue/unit, expense ratios) displayed for
   each property.

2. **Given** a dashboard with property data, **When** a user applies filters (property type, date
   range, location), **Then** only matching properties appear and aggregated metrics update
   accordingly.

3. **Given** properties with performance targets defined, **When** a property's metric deviates
   from target, **Then** a visual indicator (color-coded) highlights the variance.

4. **Given** a portfolio manager viewing the dashboard, **When** they click on any metric,
   **Then** they see historical trend data for that metric.

---

### User Story 2 - Stoplight Ranking System (Priority: P2)

A portfolio manager views all properties ranked using a three-tier stoplight model (green/yellow/
red) based on composite scores from performance, cost efficiency, and geographic factors. They
can quickly identify which properties need urgent attention versus which are performing well.

**Why this priority**: Builds on the KPI dashboard to provide actionable prioritization. Portfolio
managers need to know not just the numbers, but which properties deserve their attention first.

**Independent Test**: Can be tested by configuring ranking weights and verifying properties are
correctly categorized. Delivers value as a prioritization tool even without other features.

**Acceptance Scenarios**:

1. **Given** a portfolio with performance data, **When** a portfolio manager views the ranking,
   **Then** all properties display a stoplight indicator (green/yellow/red) based on composite
   score.

2. **Given** a property with a red or yellow ranking, **When** a user clicks on that property,
   **Then** they see a detailed scorecard explaining the ranking with specific factors that
   contributed to the score.

3. **Given** underlying property data changes, **When** new data is processed, **Then** the
   stoplight rankings update automatically to reflect current performance.

4. **Given** a stoplight-ranked list, **When** a portfolio manager sorts by ranking, **Then**
   red properties appear first, followed by yellow, then green.

---

### User Story 3 - Geographic Opportunity Mapping (Priority: P3)

A data analyst accesses an interactive map showing property locations with performance overlays.
They can toggle between different metrics (occupancy, NOI, expense ratios) to identify geographic
clusters and analyze submarket performance patterns.

**Why this priority**: Location context adds strategic insight beyond raw numbers. Helps identify
patterns that aren't visible in spreadsheets, such as submarket trends and geographic clusters.

**Independent Test**: Can be tested by plotting properties on a map and verifying overlay
accuracy. Delivers value as a geographic visualization tool.

**Acceptance Scenarios**:

1. **Given** portfolio property data with locations, **When** an analyst opens the map view,
   **Then** all properties appear as markers on an interactive map.

2. **Given** a map with property markers, **When** a user selects a metric overlay (occupancy,
   NOI, expense ratio), **Then** markers change color to reflect that metric's performance level.

3. **Given** an interactive map, **When** a user hovers over a property marker, **Then** a
   tooltip displays key property stats (name, units, selected metric value).

4. **Given** an interactive map, **When** a user clicks a property marker, **Then** they
   navigate to the full property profile with detailed information.

---

### User Story 4 - Cost Structure Analysis (Priority: P4)

A data analyst reviews operating expense breakdowns across standardized categories (maintenance,
utilities, administrative) for individual properties. They can benchmark costs against portfolio
averages and identify outliers where controllable costs exceed expected ranges.

**Why this priority**: Cost efficiency is a primary driver of property performance. Understanding
cost structure enables targeted improvement strategies.

**Independent Test**: Can be tested by uploading expense data and verifying categorization and
benchmarking calculations. Delivers value as a cost analysis tool.

**Acceptance Scenarios**:

1. **Given** property expense data, **When** an analyst views cost structure, **Then** expenses
   display in standardized categories with subtotals and percentages.

2. **Given** a property's cost breakdown, **When** compared to portfolio average, **Then** each
   category shows variance from average with visual indicator for significant outliers.

3. **Given** expense outliers identified, **When** an analyst clicks an outlier, **Then** they
   see similar properties for comparison and suggested efficiency opportunities.

4. **Given** cost data, **When** the system processes expenses, **Then** it distinguishes
   between controllable and structural costs with appropriate labels.

---

### User Story 5 - Acquisition Screening (Priority: P5)

An executive inputs potential acquisition target characteristics into the screening tool and
receives an automated assessment comparing the property against portfolio-derived success
criteria. The system generates a recommendation report with supporting data visualizations.

**Why this priority**: Strategic growth capability that leverages all other analytics. Requires
established benchmarks from the portfolio analysis features.

**Independent Test**: Can be tested by entering hypothetical property data and verifying the
screening logic produces consistent, explainable results.

**Acceptance Scenarios**:

1. **Given** an executive with acquisition criteria, **When** they input property characteristics
   (location, units, price, projected financials), **Then** the system accepts the input and
   processes the screening.

2. **Given** a submitted acquisition target, **When** screening completes, **Then** the system
   displays a comparison to portfolio benchmarks for each success criterion.

3. **Given** screening results, **When** an executive requests a report, **Then** the system
   generates a recommendation report with data visualizations comparing the target to current
   portfolio properties.

4. **Given** historical acquisition data, **When** reviewing screening results, **Then** the
   system shows how similar past acquisitions have performed.

---

### Edge Cases

- What happens when a property has incomplete data (missing KPIs or expense categories)?
  System displays available data with clear indication of missing fields; property excluded
  from rankings until minimum required data is present.

- How does the system handle conflicting data from multiple sources?
  System flags discrepancies for user review; most recent data source is used as default
  until user resolves the conflict.

- What happens when no properties match filter criteria?
  System displays clear "No results" message with suggestions to broaden filter criteria.

- How does the system behave when processing large data uploads?
  System provides progress indicator; users can continue other tasks while upload processes
  in background.

## Requirements *(mandatory)*

### Functional Requirements

**Data Management**

- **FR-001**: System MUST ingest property data from uploaded spreadsheets (Excel, CSV formats)
- **FR-002**: System MUST validate uploaded data and flag inconsistencies before processing
- **FR-003**: System MUST persist all property and financial data with audit trail
- **FR-004**: System MUST support data updates without losing historical records
- **FR-005**: System MUST export reports and data in common formats (PDF, Excel)

**KPI Calculations**

- **FR-006**: System MUST calculate Net Operating Income (NOI) for each property
- **FR-007**: System MUST calculate occupancy rates from unit-level data
- **FR-008**: System MUST calculate revenue per unit metrics
- **FR-009**: System MUST calculate expense ratios by category
- **FR-010**: System MUST recalculate all KPIs immediately upon spreadsheet upload completion
  (no real-time sync or scheduled batch processing required for PoC)

**Dashboard & Visualization**

- **FR-011**: System MUST display portfolio-wide summary statistics on the landing page
- **FR-012**: System MUST provide filtering by property, date range, and asset characteristics
- **FR-013**: System MUST display visual indicators for variance from targets
- **FR-014**: System MUST show historical trends for selected metrics covering 12 months of data

**Stoplight Ranking**

- **FR-015**: System MUST assign green/yellow/red ranking to each property based on composite
  score
- **FR-016**: System MUST generate property scorecards explaining ranking factors
- **FR-017**: System MUST update rankings automatically when data changes

**Geographic Analysis**

- **FR-018**: System MUST display properties on an interactive map
- **FR-019**: System MUST support metric overlays (color-coded by selected KPI)
- **FR-020**: System MUST show property details on hover and click

**Cost Analysis**

- **FR-021**: System MUST categorize expenses into standard categories
- **FR-022**: System MUST benchmark property costs against portfolio averages
- **FR-023**: System MUST identify and flag cost outliers
- **FR-024**: System MUST distinguish controllable from structural costs

**Acquisition Screening**

- **FR-025**: System MUST accept acquisition target inputs (location, units, financials)
- **FR-026**: System MUST compare targets against portfolio success criteria
- **FR-027**: System MUST generate acquisition recommendation reports

**Access Control**

- **FR-028**: System MUST support role-based access (Executive, Portfolio Manager, Analyst)
- **FR-029**: System MUST require authentication for all access
- **FR-030**: System MUST log user actions for security audit

### Key Entities

- **Property**: A multifamily residential asset; key attributes include location, unit count,
  acquisition date, current valuation, property type, and submarket classification

- **Financial Record**: Periodic financial data for a property; includes revenue, expenses by
  category, NOI, and reporting period

- **KPI Metric**: Calculated performance indicator; includes metric type, value, calculation
  date, and property reference

- **Stoplight Ranking**: Composite assessment of property performance; includes overall score,
  tier (green/yellow/red), contributing factors, and assessment date

- **Acquisition Target**: Prospective property for evaluation; includes input characteristics,
  screening score, benchmark comparisons, and recommendation status

- **User**: System user with role assignment; includes authentication credentials, role
  (Executive/Portfolio Manager/Analyst), and access permissions

## Success Criteria *(mandatory)*

### Measurable Outcomes

**User Efficiency**

- **SC-001**: Portfolio managers can identify underperforming properties within 2 minutes of
  login (vs. hours of manual spreadsheet analysis previously)
- **SC-002**: Analysts can generate standardized KPI reports in under 5 minutes per property
- **SC-003**: 90% of users successfully complete their primary task on first attempt

**Data Quality**

- **SC-004**: KPI calculations match manual verification with less than 2% error rate
- **SC-005**: System processes portfolios of 100+ properties without performance degradation
- **SC-006**: Data uploads of 50-100 properties complete within 5 minutes

**Business Value**

- **SC-007**: Platform identifies cost reduction opportunities totaling measurable savings
- **SC-008**: Acquisition recommendations align with portfolio success patterns (validated
  against historical performance of similar properties)
- **SC-009**: Stoplight rankings correctly prioritize properties (validated by portfolio
  manager review showing 85%+ agreement with manual assessment)

**Adoption**

- **SC-010**: Platform becomes regular tool for portfolio management (measured by weekly
  active usage by all portfolio managers)
- **SC-011**: Time-to-insight improves by at least 75% compared to manual processes

## Clarifications

### Session 2026-02-02

- Q: Which user stories constitute the MVP/PoC scope? → A: P1 only (KPI Dashboard)
- Q: How frequently should KPI calculations update? → A: On upload (recalculate when user uploads new spreadsheet)
- Q: How far back should historical trend data be available? → A: 12 months (full year for seasonal comparison)

## Assumptions

- **MVP Scope**: The proof-of-concept includes only User Story 1 (Portfolio KPI Dashboard).
  Stories P2-P5 are deferred to subsequent iterations after P1 is validated with stakeholders.
- Portfolio data is available in spreadsheet format (Excel/CSV) with consistent column
  structure across properties
- Users have modern web browsers (Chrome, Firefox, Safari, Edge - last 2 versions)
- Properties are located within the United States (LA County focus initially)
- Financial data follows standard real estate accounting categories
- Users have basic familiarity with portfolio management concepts and terminology
- Initial deployment serves a single organization (PHMS) with potential for multi-tenancy later
- Property location data includes street addresses or coordinates suitable for mapping
