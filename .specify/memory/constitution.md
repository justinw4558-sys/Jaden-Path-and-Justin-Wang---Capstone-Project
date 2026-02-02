<!--
  SYNC IMPACT REPORT
  ==================
  Version change: N/A → 1.0.0

  Modified principles: (Initial version - no prior principles)

  Added sections:
    - Core Principles (4 principles)
    - Development Workflow
    - Task Governance
    - Governance

  Removed sections: None (initial version)

  Templates requiring updates:
    - .specify/templates/plan-template.md: ✅ Compatible (Constitution Check section exists)
    - .specify/templates/spec-template.md: ✅ Compatible (prioritized user stories align with PoC-First)
    - .specify/templates/tasks-template.md: ✅ Compatible (MVP-first strategy aligns with principles)

  Follow-up TODOs: None
-->

# Strategic Residential Property Assessment Constitution

## Core Principles

### I. Proof-of-Concept First

All features MUST begin as a minimal working prototype before expanding scope.

- Start with a functional Excel-based tool that demonstrates core value
- Validate each increment with stakeholders before adding complexity
- The first deliverable for any feature MUST be a working demonstration, not documentation
- Avoid building infrastructure for hypothetical future requirements

**Rationale**: Real estate investment decisions require confidence in the tool's output. A working
prototype provides tangible validation that theoretical designs cannot.

### II. Data Integrity

Property data MUST be accurate, traceable, and consistently formatted.

- All data sources MUST be documented with retrieval date and origin
- Scoring calculations MUST be reproducible given the same inputs
- Data transformations MUST preserve original values alongside derived fields
- Discrepancies between sources MUST be flagged, not silently resolved

**Rationale**: Investment recommendations based on flawed data can result in significant financial
loss. Traceability enables auditing and builds stakeholder trust.

### III. Iterative Simplicity

Add complexity only when validated by actual use, not anticipated need.

- Excel formulas and manual processes are acceptable until proven insufficient
- Features MUST solve a demonstrated problem, not a theoretical one
- Prefer fewer, well-tested properties over comprehensive but untested coverage
- Each iteration MUST deliver standalone value (5-8 ranked properties, not partial infrastructure)

**Rationale**: A 24-week timeline with a 2-person team requires focused execution. Premature
optimization delays delivery without proportional benefit.

### IV. User Validation Gates

Stakeholder confirmation is REQUIRED before expanding scope or creating additional tasks.

- New phases MUST NOT begin until prior phase deliverables are accepted
- Task lists MUST be reviewed and approved before implementation begins
- Scope additions require explicit stakeholder request, not developer inference
- When in doubt, ask before building

**Rationale**: Prevents wasted effort on features stakeholders do not need. Ensures the final
deliverable matches actual requirements rather than assumed ones.

## Development Workflow

### Phase Gate Requirements

Before advancing to the next project phase:

1. Current phase deliverables MUST be complete and functional
2. Stakeholder feedback MUST be collected and documented
3. Scope for next phase MUST be confirmed (not assumed)

### Deliverable Standards

- Unified Spreadsheet: All property records in consistent format with source attribution
- Scoring Model: Weighted calculations with documented formula logic
- Property Briefs: One-page summaries with comps, maps, and recommendations
- Strategic Roadmap: Ranked acquisition priorities with rationale

## Task Governance

### Task Creation Rules

- Tasks MUST be reviewed with stakeholders before implementation begins
- Maximum tasks per phase MUST be agreed upon before work starts
- Each task MUST map to a specific deliverable or user story
- Tasks without clear acceptance criteria MUST NOT be created

### Task Scope Limits

- Prefer fewer, well-defined tasks over comprehensive task breakdowns
- Group related work into single tasks rather than fragmenting into many small tasks
- If task count exceeds agreed limit, consolidate or defer lower-priority items

## Governance

This constitution establishes the non-negotiable rules for the Strategic Residential Property
Assessment project. All work MUST comply with these principles.

### Amendment Process

1. Propose amendment with rationale
2. Document impact on existing deliverables
3. Obtain stakeholder approval
4. Update constitution with version increment
5. Review dependent artifacts for consistency

### Versioning Policy

- MAJOR: Principle removal or fundamental redefinition
- MINOR: New principle added or significant guidance expansion
- PATCH: Clarifications, wording improvements, non-semantic changes

### Compliance

- All deliverables MUST pass Constitution Check before stakeholder review
- Violations MUST be documented and justified in Complexity Tracking
- Unjustified violations block phase completion

**Version**: 1.0.0 | **Ratified**: 2026-02-02 | **Last Amended**: 2026-02-02
