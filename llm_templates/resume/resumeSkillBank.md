# Skill Bank - Phillip Chuzhbinin

## Purpose

This is an exhaustive collection of all work accomplishments, organized by role. Use this bank to pull relevant bullets when tailoring resumes to specific job descriptions. Each bullet is descriptive and quantitative—shorten and adapt the language when creating actual resume bullets.

---

## QA Consultant (Contract), Coffee Meets Bagel WorldWide

**March 2025 - June 2025 | Richmond, VA (Remote)**

### Test Migration & Infrastructure

1. Migrated custom Python test library (Pytest, Selenium, Locust) containing 120+ tests into acquirer's AWS infrastructure, which was a copy of original infrastructure.
2. Adapted test frameworks for international geolocation requirements, reversing validation logic for phone number restrictions (allowing international numbers vs US-only).
3. Generated valid international test data using LLM-based tools with human validation, enabling automated tests across multiple geographic regions while ensuring numbers were valid and not existing users.
4. Configured test suite for local, staging, and production environments despite acquirer's lack of CI/CD infrastructure (they didn't believe in CI).
5. Began migration of 50+ Selenium tests to Playwright TypeScript framework before contract completion (unfinished due to contract end).
6. Built and migrated profile vending machine tool that would create new or existing profiles with custom info/preferences and location on request.

### Documentation & Knowledge Transfer

7. Created comprehensive testing playbooks covering test execution, custom tools, and release process strategies (tagging, cutting release candidates, etc).
8. Authored extensive technical product documentation covering: admin panel operations, algorithm validation, microservice architecture (which services matches are sourced from), Django model-to-API correlations, client call stacks, manual Xcode and Android Studio project builds, database migrations, and deployment procedures.
9. Delivered training to manual QA team and engineering leads of acquirer, transferring decade of proprietary product knowledge within 3-month contract.
10. Created documentation estimated to save every engineer approximately one month in terminology and distributed microservice understanding (the hardest part of new projects), saving hundreds of total hours.

### Tooling & Process Improvement

11. Enabled manual QA team to execute 120+ automated tests independently, compensating for reduction from 3 QA engineers to 1 manual QA for entire company.
12. Introduced monitoring and analysis tools (Postman, Sentry, PG Analyze) to engineering team for performance validation and debugging.

---

## QA Lead, Coffee Meets Bagel

**March 2022 - March 2025 | Richmond, VA (Remote)**

### Test Automation & Frameworks

1. Built Python test automation framework packaging 150+ tests (120 Pytest REST API tests, 50 Selenium admin UI tests, 25 Locust load tests) into versioned internal library distributed via Nexus.
2. Automated framework build in Jenkins CI within qa-testing repo, building inside Docker and pushing to ECR for backup and Nexus for internal distribution to any environment.
3. Unified mobile automation from fragmented XCUITest (Swift) and Espresso (Kotlin) suites into single custom Appium Python framework.
4. Created 50 new cross-platform mobile tests (previously had separate iOS/Android codebases requiring duplicate work).
5. Achieved 70% smoke test automation coverage (50 automated of 350 total acceptance test cases).
6. Integrated Firebase Test Lab and SauceLabs into Bitrise CI for nightly iOS/Android test execution in collaboration with QA team.

### Backend Development & Leanplum Integrations

7. Developed backend Leanplum integration for Table for Two feature: personalized QR codes served via S3/CloudFlare for Coffee Meets Bagel user discounts at local date spots.
8. Built QR code system with encoded and hashed user information, scanned by date spots using custom web app to track codes scanned together, ensuring no duplicate date discounts while protecting PII.
9. Validated subscription/free trial messaging campaigns in Leanplum based on user LTV (lifetime value).
10. Validated app-splitting email campaigns for AWS migration project (splitting apps into 2 infrastructures, 2 companies).
11. Reduced development time 60% for Table for Two by building backend-only solution without requiring iOS or Android mobile integration.
12. Implemented targeting through opt-in chained campaigns without special filtering requirements.

### Testing Infrastructure & Data Tools

13. Built profile vending machine generating test users with custom preferences, locations, and geolocation attributes (lat/long + phone number) on demand.
14. Created fake OTP (one-time password) authentication system unblocking mobile automation by bypassing SMS verification in test environments.
15. Developed 20+ ad-hoc scripts for test database setup and complex user scenario configuration.

### Performance & Load Testing

16. Executed Locust load tests simulating 2K concurrent users or 50K requests per second for AWS infrastructure migration validation.
17. Ran load tests that could complete within 5 minutes but enabled long runtimes to generate charts establishing median response times of 400ms.
18. Uncovered 98th percentile latency issues (1500ms) for high-matching users through extended load test analysis.

### Quality Dashboards & Automation

19. Built incident analytics dashboard tracking CX-reported issues with deep links, showing leaderboard of open issues per QA, QA responsiveness, average response times, and outstanding/overdue issues.
20. Reduced issue response time by 83% (72 hours to under 12 hours) through daily dashboard that decluttered Slack messaging and provided single tracking source.
21. Built separate Zendesk-to-Asana bug tracking integration that automatically created problem tickets, synced cases, set priorities and descriptions.
22. Eliminated manual context switching for CX team and streamlined tracking for weekly reproduction meetings through automated bug sync.

### CI/CD & Code Quality

23. Implemented CI quality gates including type checking (mypy), linting, and end-to-end tests in Jenkins pipelines.
24. Enabled and maintained 8 daily backend releases with automated quality validation through improved CI/CD processes.

### Algorithm & Data Validation

25. Validated graph-weighting algorithms and DNN (deep neural network) match models using baseline CSV comparisons from previously established green releases.
26. Implemented fuzzy validation (similar but not exact matching) for model scores between -1 and +1 range.
27. Ensured specific models had non-null values while others remained empty depending on profile eligibility requirements.
28. Established automated test pipelines for ML model releases working directly with data team.

### Geolocation & Edge Case Testing

29. Designed comprehensive geolocation test suite validating lat/long coordinates, phone number formats, and edge cases (e.g., international number for US-based user).
30. Validated AWS migration requirements ensuring international phone number handling logic reversed from US-only restrictions.

### Team Leadership & Monitoring

31. Mentored 2 QA engineers through Appium proof-of-concept and Python/Pytest test development.
32. Promoted both mentored engineers to senior roles within 1 year through technical pairing and automation tool training.
33. Used Datadog and Grafana for performance monitoring during deployments and PostgreSQL query analysis.

---

## Senior Backend QA Engineer, Coffee Meets Bagel

**July 2019 - March 2022 | Seattle, WA (Remote)**

### Infrastructure & CI/CD

1. Migrated backend QA tests from Jenkins/Docker to Kubernetes-based QA service, scaling from 4 parallel builds to 12+ parallel builds with no performance issues or scaling problems.
2. Built Jenkci (Jenkins-CI queuer) reducing build costs 60% by only allowing PRs to trigger builds and preventing commits from constantly triggering builds.
3. Created Ottobot (Jenkins-Slack integration) enabling staging deployments, PagerDuty on-call schedule reporting, and test execution via Slack commands.
4. Designed bash deployment playbooks that opened deployment step pages, migration commands, and necessary monitoring pages/apps in correct order.
5. Reduced repeated deployment errors by 90% through playbooks ensuring QA followed all necessary steps in order and could rollback when needed.

### Release Automation & Tooling

6. Built GitHub-Asana release orchestration application with FastAPI automating: RC (release candidate) branch cutting, commit distribution, release notes generation by identifying and tagging connected Asana tickets.
7. Extended GitHub-Asana app to report necessary backend migrations, back up notes in Redis, report to Slack, and after verification send release email with tickets.
8. Automated updating of release tracking sheets and Git tags, eliminating 80% of manual tracking overhead.
9. Enabled multi-platform release automation (backend, Android, iOS) through GitHub-Asana app—initially backend-focused but eventually triggerable for any client.
10. Won hackathon for GitHub-Asana initial feature: syncing GitHub PR descriptions and statuses to Asana tickets on PR open.

### Backend Development & Integrations

11. Developed Coffee Club Leanplum integration (pandemic-related) enabling targeting and grouping of 100 users based on different admin-provided parameters.
12. Built campaign that invited users via Leanplum messaging, then sent email with custom Zoom link for Coffee Club meeting date if they accepted.
13. Implemented Zoom integration separating users into smaller groups to discuss marketing-chosen topics, followed by automated feedback requests.
14. Created feature enabling authentic connections during COVID through collaboration primarily between marketing and myself, reducing manual overhead of targeting, tracking, campaign creation, and Zoom handling.
15. Built entire Coffee Club feature without mobile development support (filtering, Leanplum integration, Zoom integration, campaign and email rendering, follow-up).
16. Developed backend Admin UI tooling for 10+ new features enabling QA to test without engineering dependencies.
17. Created 50+ ad-hoc scripts for complex user scenario setup and feature testing automation.

### Performance & Database Optimization

18. Collaborated with SRE using PG Analyze and New Relic to identify high-latency queries and determine root causes.
19. Planned backend development tasks (pagination, sharding) that would address performance issues.
20. Reduced database query latency to under 200ms through optimization recommendations and backend task coordination.

### Security & Compliance

21. Performed PII (personally identifiable information) security audits of REST APIs ensuring GDPR and CCPA compliance across all endpoints.

### Internal Tools

22. Built FrenchPress (Flask/SQLAlchemy Zoom archive app) that automatically backed up any recorded meeting/tech talk to S3.
23. Created internal video hosting and viewing site bypassing Zoom's 90-day deletion policy, serving as permanent company knowledge base.

### Knowledge Transfer & Collaboration

24. Delivered product overview, terminology, and admin tool training for all company new hires, reducing onboarding time by 1 week.
25. Supported cross-functional teams of 20+ engineers: 3 iOS, 3 Android, 7 backend, 3 SRE, 4 data team, plus marketing, CX, product, and finance.

### Team Management

26. Managed 2 backend QA engineers conducting 1:1s, assigning work, and guiding career growth.
27. Informally mentored 2 additional QA engineers (total 4 engineers unofficially managed before receiving Lead title).

---

## Backend QA Engineer, Coffee Meets Bagel

**July 2015 - July 2019 | San Francisco, CA**

### Test Automation Foundation

1. Built automated regression test suite reducing execution time from 30 minutes manual regression to 7 minutes automated through writing scripts and adding Jenkins jobs.
2. Developed initial test automation using Django Management Command scripts (before awareness of test frameworks—exit code 1 worked like failed test in Jenkins).
3. Transitioned test automation to Pytest framework and Dockerized tests for CI integration toward end of role.
4. Created 300+ foundational acceptance test cases in TestLodge during QA Generalist phase (March 2015 - July 2017), establishing comprehensive baseline.

### CI/CD & Infrastructure

5. Set up Jenkins CI integration with GitHub enabling automated test execution on every commit.
6. Built Ottobot (Jenkins-Slack integration) enabling Slack-triggered deployments, test runs, PagerDuty on-call schedules, and joke telling.
7. Removed need to configure complicated features and keys by having Jenkins jobs triggerable through Ottobot—primarily used for staging deployments, on-call schedules, and API tests for any environment.
8. Dockerized test suite enabling consistent execution across local and CI environments.
9. Configured Jenkins jobs and GitHub integrations supporting transition from weekly to daily backend releases.

### Release Process & Ownership

10. Shifted backend release ownership from developers to QA, becoming release manager to optimize developer time.
11. Trained 2 backend QA engineers on deployment processes, establishing single point of contact for release issues (makes sense having one release manager for consultation).
12. Scaled release cadence from weekly to 4x weekly (later daily) through automated testing and deployment processes.

### Tooling & Automation

13. Built initial GitHub-Asana integration syncing PR links to Asana tickets automatically, laying foundation for future release automation (later expanded significantly as Senior).
14. Developed ad-hoc testing scripts automating complex user scenario setup and test data generation.
15. Created internal test tooling leveraging Django codebase for API call chaining before Postman adoption—more extensible than Postman at the time.

### Team Building & Scaling

16. Scaled QA coverage from solo QA testing everything to 3-person team by training 2 CX (customer experience) agents to become Android/iOS QA engineers.
17. Assigned QA resources to projects, organized company-wide bug bashes, and established quality gate approval processes.
18. Managed 2 QA engineers unofficially (assigning work, conducting 1:1s, guiding career growth) 2+ years before receiving Lead title, showing unofficial management for much longer than title indicated.

### Process & Collaboration

19. Collaborated hands-on with developers to recreate test scenarios using internal code levers to reach states needed for testing.
20. Established post-mortem processes ensuring repeated issues addressed systematically—made mistakes only once because we post-mortemed and created processes to prevent recurrence.
21. Supported infrastructure team on upgrades, requirement updates, key management, and Jenkins-GitHub connectivity.
22. Defined and standardized QA processes used across all engineering teams company-wide.

### Manual Testing & Broad Coverage (2015-2017 Generalist Phase)

23. Performed comprehensive manual testing across backend, Android, iOS, and data systems as sole QA engineer.
24. Focused automation efforts on backend and data validation while scaling mobile coverage through team expansion.
25. Learned programming self-taught during this period, transitioning from manual-only to automation focus.

---

## Earlier Roles (Not Currently on Resume)

### QA Engineer Generalist, Coffee Meets Bagel

**March 2015 - July 2017 | San Francisco, CA**

_Note: Currently combined with Backend QA Engineer role (2015-2019) on resume. This represents the generalist phase before backend specialization._

-   Solo QA covering all platforms (backend, Android, iOS, data)
-   Created 300+ acceptance test cases in TestLodge
-   Trained 2 CX agents to become Android/iOS QA engineers
-   Primarily manual testing with self-taught programming learning
-   Foundation building for later automation work

### Android QA Intern, Coffee Meets Bagel

**November 2014 - March 2015 | San Francisco, CA**

_Note: Not included on resume—internship not relevant for senior roles._

-   Manual Android testing pre-launch
-   Beta program management (Google Play Beta with 500+ external testers)
-   Contributing to 99.9% crash-free release for 2015 Shark Tank debut
-   Device coverage expansion through tester triaging

---

## Projects

### QAKit (Open Source / Personal)

**Technologies:** Python, Flask, HTMX, Tailwind, JavaScript, Docker, GitHub Actions

-   Built Dockerized API testing client with request history, replay functionality, environment switching, and JSON validation.
-   Packaged as both Python library and Docker image to extend test coverage across teams.
-   Designed for low-effort exploratory REST API testing and rapid test development.
-   Available as open source project on GitHub.
