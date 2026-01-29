# Product Requirements Document (PRD)
# Portfolio Analytics Platform for PHMS Real Estate

## TL;DR (Elevator Pitch)

A comprehensive portfolio analytics platform designed to transform PHMS's multifamily property data into actionable insights for strategic decision-making. The platform analyzes operational performance, geographic opportunities, and cost structures across the portfolio to identify acquisition targets and optimize existing assets, enabling data-driven real estate investment decisions through interactive dashboards and automated reporting.

---

## Goals

### Business Goals

1. **Improve Portfolio Performance** by identifying and implementing cost reduction opportunities and operational improvements across underperforming assets based on data-driven insights.

2. **Streamline Portfolio Analysis Process** by automating KPI calculations, geographic mapping, and comparative analyses through the platform, significantly reducing time spent on manual data processing.

3. **Enable Data-Driven Acquisition Decisions** by developing a validated acquisition framework that screens potential properties against portfolio performance benchmarks and provides actionable recommendations.

### User Goals

1. **Portfolio Managers** can quickly identify underperforming assets and prioritize intervention strategies through an intuitive stoplight ranking system that synthesizes performance, cost, and geographic data.

2. **Analysts** can generate comprehensive portfolio reports in minutes rather than hours, with automated data visualization and standardized metrics that significantly reduce manual data processing.

3. **Executives** can make informed acquisition decisions by accessing clear, data-backed recommendations that compare potential properties against proven portfolio benchmarks and success patterns.

### Non-Goals

1. **Property Management Operations**: The platform will not handle day-to-day property management tasks such as tenant communications, maintenance requests, or lease administration.

2. **Financial Transaction Processing**: The system will not process payments, handle accounting functions, or manage financial transactions beyond analysis and reporting.

---

## User Stories

### User Type 1: Portfolio Manager

**Story 1:** As a portfolio manager, I want to view a stoplight-ranked list of all properties so that I can immediately identify which assets need urgent attention versus which are performing well.

**Story 2:** As a portfolio manager, I want to drill down into specific underperforming properties to see detailed cost breakdowns and geographic context so that I can develop targeted improvement strategies.

### User Type 2: Data Analyst

**Story 1:** As a data analyst, I want to automatically generate standardized KPI reports across all properties so that I can spend more time on strategic analysis rather than manual data processing.

**Story 2:** As a data analyst, I want to create custom geographic opportunity maps that overlay performance metrics with market data so that I can identify location-based investment patterns.

### User Type 3: Executive/Investment Decision-Maker

**Story 1:** As an executive, I want to receive acquisition recommendations with clear comparison to current portfolio benchmarks so that I can evaluate new opportunities against proven success factors.

**Story 2:** As an executive, I want to access historical trend analysis and case studies so that I can understand how portfolio performance has evolved and validate strategic decisions.

---

## Functional Requirements

### 1. Automated Portfolio KPI Dashboard (Priority 1)

The platform must automatically calculate and display core performance metrics (NOI, occupancy rates, revenue per unit, expense ratios) for all properties in the portfolio. Users can filter by property, date range, and asset characteristics. Real-time updates reflect current portfolio status with visual indicators for variance from targets.

### 2. Geographic Analysis and Opportunity Mapping (Priority 2)

The system must generate interactive maps showing property locations with performance overlays (color-coded by profitability, occupancy, or other selected metrics). Users can identify geographic clusters, analyze submarket performance, and visualize spatial relationships between high and low performers. Map data integrates with market research APIs for contextual benchmarking.

### 3. Asset-Level Stoplight Ranking System (Priority 3)

The platform must rank all properties using a three-tier stoplight model (green/yellow/red) based on composite scores from performance metrics, cost efficiency, and geographic factors. Each property receives a detailed scorecard explaining its ranking with specific improvement opportunities. Rankings update automatically as underlying data changes.

### 4. Cost Structure Analysis Engine (Priority 4)

The system must decompose operating expenses across standardized categories (maintenance, utilities, administrative, etc.) and identify outliers. Users can benchmark individual property costs against portfolio averages and similar properties. The engine flags controllable versus structural costs and suggests efficiency opportunities.

### 5. Acquisition Screening and Recommendation Framework (Priority 5)

The platform must evaluate potential acquisition targets against portfolio-derived success criteria including location characteristics, asset size, cost structure benchmarks, and projected performance. Users can input property characteristics to receive automated screening results with comparative analysis to current portfolio. The system generates recommendation reports with supporting data visualizations.

---

## User Experience

The user journey begins with a comprehensive dashboard landing page displaying portfolio-wide summary statistics and performance trends. Upon login, portfolio managers immediately see their stoplight-ranked property list, with green (strong performers), yellow (moderate performers), and red (underperformers) clearly distinguished.

Entry points include direct login through web browser or mobile app, with role-based access controlling visibility of different features. Executives access high-level strategic views while analysts have granular data exploration capabilities.

Core functionalities center around three main modules: Portfolio Analytics, Geographic Intelligence, and Acquisition Planning. In Portfolio Analytics, users interact with dynamic charts and tables that update based on selected filters. Clicking any property card opens detailed views with historical performance graphs, peer comparisons, and drill-down capabilities into specific metrics.

The Geographic Intelligence module presents an interactive map interface where users can toggle between different overlay modes (occupancy, NOI, expense ratios). Hovering over properties reveals quick stats while clicking opens full property profiles. Users can draw custom regions to analyze submarket performance or identify clustering patterns.

Key interactions include intuitive filtering across all views, one-click report generation, and seamless navigation between related data points. For example, clicking an expense outlier in the cost analysis automatically filters to show similar properties and suggests benchmark comparisons.

UX/UI considerations prioritize clean, professional design with consistent color coding (red/yellow/green throughout), responsive layouts for desktop and tablet use, and accessible data visualization following WCAG 2.1 standards. The interface minimizes clicks to insights through intelligent defaults and progressive disclosure - showing summary data first with easy access to detailed analysis. Navigation uses familiar patterns with sidebar menu, breadcrumb trails, and contextual actions. Loading states and helpful error messages ensure users understand system status and can recover from issues independently.

---

## Narrative

Sarah, a portfolio manager at PHMS, starts her Monday morning facing a familiar challenge: understanding which of her 50+ properties need immediate attention. Previously, this meant hours of spreadsheet work, manually calculating metrics and cross-referencing data. She opens the Portfolio Analytics Platform and immediately sees her stoplight dashboard—three properties flash red, signaling underperformance.

Clicking the worst performer, a 120-unit complex in Riverside, she discovers that while occupancy looks acceptable, operating expenses are significantly above portfolio average. The platform's cost analysis highlights excessive maintenance spending and utilities that don't match similar properties. The geographic map reveals this property sits in a strong submarket where competitors achieve both lower costs and higher rents.

Armed with these insights in minutes rather than hours, Sarah schedules a site visit focused on the specific cost drivers flagged by the system. Within two weeks, she implements corrective measures that the platform now tracks automatically. Meanwhile, the platform has also identified a potential acquisition opportunity—a property profile that matches the characteristics of PHMS's top performers. Sarah shares the automated acquisition report with executives, who appreciate the clear comparison to proven portfolio benchmarks, leading to a strategic investment decision backed by comprehensive data analysis.

---

## Success Metrics

### User-Centric Metrics

1. **User Engagement Rate**: Track active users and session patterns to ensure the platform becomes a regular tool for portfolio management decision-making.

2. **Time-to-Insight**: Measure the time from login to actionable insight discovery, ensuring users can quickly identify portfolio issues or opportunities compared to manual processes.

### Business Metrics

1. **Cost Savings Identified**: Track the total value of cost reduction opportunities flagged by the platform across the portfolio.

2. **Acquisition Decision Quality**: Measure the success rate of platform-recommended acquisitions that proceed to closing and meet performance projections.

### Technical Metrics

1. **System Uptime**: Maintain high availability during business hours with minimal disruptions.

2. **Data Processing Speed**: Ensure portfolio KPI calculations and individual property analyses render quickly to support real-time decision-making.

---

## Technical Considerations

The platform will be built using a modern, scalable technology stack optimized for data processing and visualization. The frontend utilizes React with TypeScript for type safety and component reusability, styled with Tailwind CSS for responsive design. The dashboard leverages D3.js and Recharts for interactive data visualizations, while mapping functionality integrates Mapbox GL JS for geographic analysis. State management uses Redux Toolkit to handle complex data flows across the application.

The backend architecture employs Node.js with Express for the API layer, providing RESTful endpoints for data access and manipulation. Python with Pandas and NumPy handles intensive data analysis tasks including KPI calculations, statistical analysis, and machine learning-based ranking algorithms. The analytics engine runs as microservices, allowing independent scaling of compute-intensive operations.

Data storage utilizes PostgreSQL for structured property and financial data, with PostGIS extensions enabling efficient geospatial queries. Time-series performance data is stored in TimescaleDB for optimized historical analysis. Redis provides caching for frequently accessed metrics and session management. All databases implement regular automated backups with point-in-time recovery capabilities.

Authentication and authorization leverage Auth0 for secure identity management with SSO support and role-based access control (RBAC). JWT tokens secure API communications with refresh token rotation. Sensitive data is encrypted at rest using AES-256 and in transit via TLS 1.3.

The application deploys on AWS infrastructure using ECS for containerized service orchestration. The frontend is delivered through CloudFront CDN with S3 bucket origin for global performance. Load balancers distribute traffic across multiple availability zones for high availability. Infrastructure as Code (Terraform) enables reproducible deployments and disaster recovery.

Analytics and monitoring integrate DataDog for application performance monitoring, error tracking, and custom business metrics. User behavior analytics through Mixpanel track feature adoption and usage patterns. Automated alerts notify the team of performance degradation or system anomalies.

Infrastructure considerations include horizontal scaling capabilities to accommodate portfolio growth. The database design supports multi-tenancy for potential future expansion to serve multiple real estate firms. API rate limiting and caching strategies ensure consistent performance under varying load conditions. Regular security audits and penetration testing validate data protection measures. The platform implements automated data quality checks to flag inconsistencies in uploaded property data before processing.

---

## Milestones & Sequencing

### Team Size and Composition

**Team:** 2-person team
- **Justin Wang** - Co-lead Analyst
- **Jaden Path** - Co-lead Analyst

### Phase 1: Foundation & Core Analytics (Weeks 1-4: Jan 19 - Feb 14)

**Duration:** 4 weeks

**Key Activities:**
- Set up development environment and project infrastructure
- Implement data ingestion pipeline for existing portfolio spreadsheets
- Build automated KPI calculation engine
- Develop initial portfolio dashboard with basic visualizations
- Create geographic mapping foundation with property location plotting

**Deliverables:**
- Functional portfolio KPI dashboard displaying core metrics
- Initial portfolio diagnostics summary
- Geographic scan with basic opportunity mapping
- Working prototype demonstrating end-to-end data flow

### Phase 2: Advanced Analytics & Ranking (Weeks 5-9: Feb 16 - Mar 28)

**Duration:** 5 weeks

**Key Activities:**
- Develop cost structure analysis engine with category decomposition
- Build stoplight ranking algorithm integrating performance, cost, and geographic factors
- Create detailed property scorecards with drill-down capabilities
- Develop case study framework for representative properties
- Implement comparative analysis module to reproduce and extend historical analysis

**Deliverables:**
- Cost structure findings with efficiency opportunity identification
- Portfolio stoplight ranking system with asset-level synthesis
- Detailed case studies for representative properties
- Updated comparative analysis validating/extending prior work

### Phase 3: Strategic Tools & Acquisition Framework (Weeks 10-15: Mar 30 - May 6)

**Duration:** 6 weeks

**Key Activities:**
- Build acquisition screening engine with customizable criteria
- Develop recommendation generation system
- Create executive reporting and presentation tools
- Conduct comprehensive testing and refinement
- Prepare final documentation and knowledge transfer materials
- Execute capstone presentation and project handoff

**Deliverables:**
- Acquisition framework with screening criteria and recommendations
- Finalized consulting-style presentation deck
- Complete platform with all functional requirements
- User documentation and training materials
- Final project submission and archived codebase for PHMS

---

## Submission Information

**GitHub Repository:** [To be created and shared with team]

**Collaborators:**
- gregory.lontok@lmu.edu (Project Advisor)
- sam.mukherjee@lmu.edu (Program Coordinator)
- [Team member GitHub usernames to be added]

**File Location:** This PRD is maintained as `PRD.md` in the root of the project repository.
