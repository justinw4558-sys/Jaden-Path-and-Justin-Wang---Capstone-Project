# Jaden-Path-and-Justin-Wang---Capstone-Project
Product Requirements Document 
Project Title: Strategic Residential Property Assessment 
Prepared for: Professor Lontok 
Prepared by: Justin Wang and Jaden Path 
TL;DR 
This capstone project aims to create a repeatable, data-driven framework to assess and rank 
residential real estate investment opportunities across Los Angeles County. We will combine 
structured market analysis, a custom-built scoring model, and localized insights to deliver a 
ranked portfolio of high-potential properties and a reusable assessment tool for future 
acquisitions. 
Goals 
Business Goals 
1. Create a unified, scalable property assessment tool capable of analyzing at least 90% of 
available property data by project completion. 
2. Deliver a shortlist of 5–8 investment-ready properties with detailed acquisition strategy 
by Week 24. 
3. Ensure at least 85% stakeholder satisfaction (via post-project feedback) with decision
readiness of the tool. 
User Goals 
1. Help real estate investors prioritize high-growth submarkets using consistent comparative 
metrics. 
2. Enable analysts to efficiently evaluate and rank properties with an Excel-based scoring 
tool. 
3. Allow clients to reuse the tool quarterly for portfolio planning and strategic acquisitions. 
Non-Goals 
 Executing actual property purchases or legal/brokerage work. 
 Expanding outside Los Angeles County or tracking real-time market shifts. 
User Stories 
Persona 1: Real Estate Investor 
 As a real estate investor, I want to identify top-performing neighborhoods so I can focus 
my capital where growth is expected. 
 As a real estate investor, I want a clear ranked list of property opportunities so I can make 
faster investment decisions. 
Persona 2: Real Estate Analyst 
 As a real estate analyst, I want a centralized spreadsheet of property data so I can run my 
models easily. 
 As a real estate analyst, I want to apply a customizable evaluation framework so I can 
tailor it to different investment scenarios. 
Functional Requirements 
Ranked by Priority: 
1. Unified Property Spreadsheet: Combines consultant and client data into a consistent 
format for evaluation. 
2. Scoring Model: Custom tool that weights key factors (zoning, financials, growth trends). 
3. Submarket Mapping: Visual and data-based identification of emerging LA submarkets. 
4. Property Overview Packets: Briefs with in-depth analysis (rent comps, entitlement 
reviews, scenarios). 
5. Strategic Roadmap Document: Outlines recommended acquisitions and 
hold/development strategies. 
User Experience 
Users begin with a spreadsheet containing a mix of known and new properties across LA 
County. From this unified data entry point, analysts can filter by submarket, property type, and 
financial criteria. 
The first interaction is data integration: uploading internal and consultant spreadsheets. Once 
integrated, the system supports automated calculations via the scoring tool, which evaluates 
properties on inputs such as rent potential, zoning restrictions, location trends, and financial ROI. 
Users can interact through: 
 Manual updates to Excel or Google Sheets 
 Drop-down menus for customizing scoring weights 
 Built-in conditional formatting to flag standout properties 
Investors then receive a shortlist of top-scoring properties with accompanying one-page briefs. 
These include: comps, visual maps, and recommendations on development vs. acquisition 
timing. 
For repeat usability, the scoring model is modular. Users can tweak weights, refresh data, and 
generate updated rankings quarterly. 
This structured yet flexible UX keeps analysts productive while providing investor stakeholders 
with decision-ready outputs. The deliverables are optimized for PDF presentation, Excel 
manipulation, and verbal discussion. 
Narrative 
Danny, an investor looking to expand his residential real estate portfolio, currently sifts through 
disorganized property spreadsheets and inconsistent advice from brokers. He's frustrated by the 
lack of a reliable, repeatable way to evaluate new investment opportunities. 
Our project solves this by delivering a structured assessment framework that ranks properties 
based on zoning, financial potential, and location-specific trends. With this tool, Danny can now 
quickly identify the most promising submarkets, focus his research, and act confidently. 
By project end, he’s not just armed with vetted property briefs — he has a system he can reuse 
and adapt as the market evolves. 
Success Metrics 
User Metrics 
 ≥ 85% stakeholder satisfaction in final feedback survey 
 Tool reused independently by client within 3 months post-handoff 
Business Metrics 
 ≥ 5–8 ranked properties delivered with investor briefs 
 ≥ 90% completeness in final property data fields 
Technical Metrics 
 Scoring tool error rate < 2% on weighted inputs 
 < 5 min load time for spreadsheet with 100+ properties 
Technical Considerations 
The tool will be developed in Microsoft Excel, with Google Sheets as a collaborative fallback. 
Data will be stored in tabular format with custom formulas, conditional formatting, and scoring 
macros. 
Tech stack and infrastructure: 
 Frontend: Excel UI with protected fields and dropdowns 
 Backend logic: Embedded formulas, weighted scoring models 
 Data sources: Public records (LA County), stakeholder spreadsheets, broker input 
 Analytics: Manual scenario analysis; future-ready for PowerBI or Tableau upgrade 
 Security: Local storage with optional Google Drive versioning 
 Deployment: Delivered as downloadable Excel workbook and client-facing PDF packets 
Performance and scalability are optimized for batch uploads of 50–100 properties with negligible 
latency. 
Milestones & Sequencing 
Team Composition 
 Justin Wang – Co-lead Analyst 
 Jaden Path – Co-lead Analyst 
Project Phases 
Phase 1: Data Integration & Submarket Targeting (Weeks 1–5) 
 Kickoff, spreadsheet merge, submarket scan 
 Deliverables: Unified Spreadsheet, Submarket Map, Alignment Deck 
Phase 2: Framework Build & Property Evaluation (Weeks 6–14) 
 Define scoring model, deep dive property analysis 
 Deliverables: Overview Packets, Stakeholder Summary, Midpoint Deck 
Phase 3: Roadmap & Final Handoff (Weeks 15–24) 
 Final rankings, strategic insights, tool delivery 
 Deliverables: Final Spreadsheet, Target Briefs, Strategic Roadmap, Final Deck 
