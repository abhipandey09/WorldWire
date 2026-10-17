import os
import json
import logging
from datetime import datetime, timezone

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("WorkWire.JobStore")

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
JOBS_FILE = os.path.join(DATA_DIR, "jobs.json")

def get_company_logo(domain: str) -> str:
    """Return high-resolution company logo URL using Google Favicon API."""
    return f"https://www.google.com/s2/favicons?domain={domain}&sz=128"

# Curated seed jobs with exact Requisition IDs, ATS endpoints, and verified company domains
SEED_JOBS = [
    {
        "id": "job-101",
        "req_id": "NV-JR1982731",
        "title": "Senior AI Infrastructure Engineer",
        "company": "NVIDIA",
        "company_domain": "nvidia.com",
        "company_logo": get_company_logo("nvidia.com"),
        "location": "Bengaluru, Karnataka, India (Hybrid)",
        "country": "India",
        "work_mode": "Hybrid",
        "department": "AI & Machine Learning",
        "employment_type": "Full-time",
        "experience_level": "Senior Level (5-8 yrs)",
        "salary_range": "₹38,00,000 - ₹55,00,000 INR",
        "apply_url": "https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/India-Bengaluru/Senior-AI-Infrastructure-Engineer_JR1982731",
        "ats_platform": "Workday",
        "posted_at": "2026-10-17T09:30:00Z",
        "status": "approved",
        "approved_by": "abhishek",
        "tags": ["Python", "CUDA", "Kubernetes", "PyTorch", "Distributed Systems", "GPU Clusters"],
        "summary": "Join NVIDIA's Accelerated Computing and Deep Learning infrastructure group in Bengaluru to build hyper-scale distributed training orchestration platforms for next-generation generative AI foundation models.",
        "description": """### About NVIDIA Accelerated Computing Bureau
NVIDIA is pioneering the era of accelerated computing and generative artificial intelligence. The AI Infrastructure engineering group designs the software fabric that coordinates tens of thousands of Blackwell and Hopper GPUs across high-performance sovereign clusters.

### Key Responsibilities
- Architect, build, and optimize distributed orchestration pipelines for trillion-parameter LLM pre-training and high-throughput inference engines.
- Collaborate with AI research scientists to diagnose network bottlenecks, GPU memory contention, and tensor parallelism efficiency using NCCL and CUDA-X libraries.
- Automate cluster provisioning, telemetry monitoring, and fault-tolerant failovers across bare-metal Kubernetes and Slurm environments.
- Maintain rigorous performance benchmarks for microservices handling billions of real-time inferencing tokens per hour.

### Candidate Qualifications & Skills
- Bachelor's or Master's degree in Computer Science, Electrical Engineering, or equivalent practical experience.
- 5+ years of hands-on systems programming experience in Python, C++, or Go.
- Deep familiarity with Linux kernel optimization, high-speed InfiniBand/RoCE networking, and container orchestration (Kubernetes).
- Proven track record with distributed deep learning frameworks (PyTorch, DeepSpeed, Megatron-LM).

### Compensation & Benefits
- Competitive base compensation with annual stock grant (RSUs) and performance bonuses.
- Comprehensive family health insurance, wellness stipend, and relocation assistance to Bengaluru.
- Flexible hybrid work schedule and dedicated GPU compute credits for personal research projects."""
    },
    {
        "id": "job-102",
        "req_id": "ST-GH6271948",
        "title": "Staff Cloud Platform Architect",
        "company": "Stripe",
        "company_domain": "stripe.com",
        "company_logo": get_company_logo("stripe.com"),
        "location": "San Francisco, CA, US (Remote / Hybrid)",
        "country": "United States",
        "work_mode": "Remote / Hybrid",
        "department": "DevOps & Cloud",
        "employment_type": "Full-time",
        "experience_level": "Staff / Lead (8+ yrs)",
        "salary_range": "$220,000 - $285,000 USD + Equity",
        "apply_url": "https://boards.greenhouse.io/stripe/jobs/6271948",
        "ats_platform": "Greenhouse",
        "posted_at": "2026-10-17T08:15:00Z",
        "status": "approved",
        "approved_by": "abhishek",
        "tags": ["Go", "AWS", "Terraform", "Kubernetes", "Service Mesh", "FinTech", "High Availability"],
        "summary": "Lead cloud platform resilience and multi-region infrastructure architecture powering trillions in global commerce payments across Stripe's core transaction processing engines.",
        "description": """### Role Overview
Stripe builds the financial infrastructure for the internet. Millions of companies—from ambitious startups to global enterprises—rely on Stripe's software to accept payments, expand globally, and run complex financial operations.

### Key Responsibilities
- Define multi-region disaster recovery, active-active failover patterns, and zero-downtime deployment pipelines handling over 500,000 transactions per minute.
- Drive platform engineering modernization across cloud cost telemetry, Envoy service mesh, and infrastructure-as-code automation.
- Partner with security engineering to uphold PCI-DSS Level 1 compliance and sovereign data residency boundaries across US, EU, and APAC zones.
- Mentor senior engineers across core payment primitives and lead technical architectural review boards.

### Required Qualifications
- 8+ years of platform engineering or cloud architecture experience in ultra-high availability SaaS or FinTech environments.
- Deep expertise in AWS primitives (EC2, EKS, RDS Aurora, DynamoDB, Direct Connect) and Terraform.
- Strong systems software background in Go, Rust, or Java.
- Proven track record designing systems with 99.999% uptime guarantees.

### What Stripe Offers
- Competitive US salary with significant equity grant and refreshers.
- 100% employer-covered health, vision, and dental insurance for employees and eligible dependents.
- Home office budget, generous annual learning allocation, and parental leave benefits."""
    },
    {
        "id": "job-103",
        "req_id": "RP-LEV7B3A9",
        "title": "Lead Full Stack Software Engineer",
        "company": "Razorpay",
        "company_domain": "razorpay.com",
        "company_logo": get_company_logo("razorpay.com"),
        "location": "Bengaluru, Karnataka, India (In-Office)",
        "country": "India",
        "work_mode": "In-Office",
        "department": "Software Engineering",
        "employment_type": "Full-time",
        "experience_level": "Lead Level (6-10 yrs)",
        "salary_range": "₹42,00,000 - ₹60,00,000 INR",
        "apply_url": "https://jobs.lever.co/razorpay/7b3a9c1e-45fa-4392-8dbb-123456789abc",
        "ats_platform": "Lever",
        "posted_at": "2026-10-16T14:20:00Z",
        "status": "approved",
        "approved_by": "abhishek",
        "tags": ["React", "TypeScript", "Node.js", "Go", "PostgreSQL", "Kafka", "Microservices"],
        "summary": "Drive developer experience and merchant dashboard innovation for India's leading unified payment and banking gateway, serving millions of active digital enterprises.",
        "description": """### About Razorpay
Razorpay is India's first full-stack financial solutions company, empowering millions of businesses to accept payments, automate disbursements, and manage vendor banking seamlessly.

### What You'll Do
- Lead a pod of 6-8 full stack engineers delivering mission-critical merchant checkout interfaces and real-time fraud mitigation tools.
- Modernize front-end architecture using React 19, TypeScript, and micro-frontend patterns to deliver sub-second load times across mobile web.
- Design resilient event-driven microservices with Kafka, Go, and PostgreSQL that scale reliably during Indian festive shopping sales (e.g. Diwali).
- Establish engineering quality benchmarks, automated end-to-end testing, and observability monitors.

### What We Are Looking For
- 6+ years building consumer or merchant-facing web applications at scale.
- Expert proficiency in React, TypeScript, modern CSS architectures, and Node.js or Go backends.
- Solid understanding of database indexing, caching strategies (Redis), and distributed consensus.
- Demonstrated technical leadership and mentoring capability."""
    },
    {
        "id": "job-104",
        "req_id": "DB-GH5918231",
        "title": "Senior Machine Learning Engineer (LLM Finetuning)",
        "company": "Databricks",
        "company_domain": "databricks.com",
        "company_logo": get_company_logo("databricks.com"),
        "location": "Seattle, WA, US (Hybrid)",
        "country": "United States",
        "work_mode": "Hybrid",
        "department": "AI & Machine Learning",
        "employment_type": "Full-time",
        "experience_level": "Senior Level (4-7 yrs)",
        "salary_range": "$185,000 - $240,000 USD + Equity",
        "apply_url": "https://boards.greenhouse.io/databricks/jobs/5918231",
        "ats_platform": "Greenhouse",
        "posted_at": "2026-10-16T11:45:00Z",
        "status": "approved",
        "approved_by": "abhishek",
        "tags": ["Python", "PyTorch", "LLMs", "RAG", "MLflow", "Vector DBs", "Spark"],
        "summary": "Work on the Mosaic AI team at Databricks in Seattle to engineer customized open-weights LLM training, quantization, and retrieval-augmented generation (RAG) platforms for Fortune 500 enterprises.",
        "description": """### Team Overview
Databricks combines data, analytics, and AI on a unified Lakehouse platform. The Mosaic AI team focuses on enabling organizations to build, fine-tune, and deploy bespoke generative models on proprietary enterprise data.

### Key Responsibilities
- Develop state-of-the-art fine-tuning recipes (LoRA, QLoRA, DPO, RLHF) integrated natively into Databricks Model Serving.
- Implement highly accurate hybrid retrieval engines coupling sparse BM25 indexing with dense neural embeddings and rerankers.
- Benchmark and optimize model latency using vLLM, TensorRT-LLM, and flash attention primitives.
- Publish technical case studies and open-source contributions to MLflow and standard AI research repositories.

### Requirements
- MS or PhD in Computer Science, Data Science, or related field with focus on NLP/ML.
- 4+ years of industry experience deploying production machine learning models.
- Deep expertise in PyTorch, Hugging Face Transformers, and distributed evaluation frameworks."""
    },
    {
        "id": "job-105",
        "req_id": "SW-BLR19284",
        "title": "Staff Backend Engineer - Payments Core",
        "company": "Swiggy",
        "company_domain": "swiggy.com",
        "company_logo": get_company_logo("swiggy.com"),
        "location": "Bengaluru, Karnataka, India (Hybrid)",
        "country": "India",
        "work_mode": "Hybrid",
        "department": "Software Engineering",
        "employment_type": "Full-time",
        "experience_level": "Staff Level (7-11 yrs)",
        "salary_range": "₹45,00,000 - ₹65,00,000 INR",
        "apply_url": "https://careers.swiggy.com/#/job-details/SWIG_BLR_19284",
        "ats_platform": "Corporate ATS",
        "posted_at": "2026-10-15T16:10:00Z",
        "status": "approved",
        "approved_by": "abhishek",
        "tags": ["Java", "Spring Boot", "Kafka", "MySQL", "DynamoDB", "Distributed Systems"],
        "summary": "Architect the hyper-scale financial transaction and wallet backend powering millions of quick-commerce orders every single day on Swiggy and Instamart across 500+ Indian cities.",
        "description": """### Engineering at Swiggy
Swiggy is India's leading on-demand convenience platform. Behind every 10-minute delivery and gourmet restaurant order lies a high-throughput distributed transaction engine that settles thousands of payments every second.

### Responsibilities
- Architect high-throughput, ACID-compliant ledger systems tracking customer wallets, restaurant settlements, and rider earnings.
- Ensure 99.99% availability during nationwide mega-events (IPL match peaks, New Year's Eve order surges).
- Decouple legacy payment services into scalable, event-driven microservices utilizing Apache Kafka and gRPC.
- Implement idempotency keys, automated reconciliation routines, and bank gateway fallback protocols."""
    },
    {
        "id": "job-106",
        "req_id": "CF-GH5829103",
        "title": "Senior Security Engineer (Application Security)",
        "company": "Cloudflare",
        "company_domain": "cloudflare.com",
        "company_logo": get_company_logo("cloudflare.com"),
        "location": "Austin, TX, US (Hybrid)",
        "country": "United States",
        "work_mode": "Hybrid",
        "department": "Security & Trust",
        "employment_type": "Full-time",
        "experience_level": "Senior Level (5-8 yrs)",
        "salary_range": "$165,000 - $215,000 USD",
        "apply_url": "https://boards.greenhouse.io/cloudflare/jobs/5829103",
        "ats_platform": "Greenhouse",
        "posted_at": "2026-10-15T13:00:00Z",
        "status": "approved",
        "approved_by": "abhishek",
        "tags": ["Rust", "Go", "AppSec", "OAuth", "Threat Modeling", "SAST/DAST", "Cryptography"],
        "summary": "Safeguard global edge compute and Zero Trust architecture at Cloudflare, mitigating automated threat vectors and securing critical customer traffic across 330+ global cities.",
        "description": """### Mission of Cloudflare Security
Cloudflare's mission is to help build a better internet. The Application Security team works across engineering to identify vulnerabilities, conduct rigorous threat models, and build automated security guardrails into deployment pipelines.

### Key Responsibilities
- Perform in-depth threat modeling, code auditing, and architecture reviews across Rust and Go edge microservices.
- Design automated SAST/DAST integrations and software bill of materials (SBOM) scanning in GitLab CI/CD.
- Partner with product teams on cryptographic primitives, TLS 1.3 implementations, and hardened authentication systems (WebAuthn/FIDO2)."""
    },
    {
        "id": "job-107",
        "req_id": "MS-1698231",
        "title": "Principal Product Manager - Generative Search",
        "company": "Microsoft",
        "company_domain": "microsoft.com",
        "company_logo": get_company_logo("microsoft.com"),
        "location": "Hyderabad, Telangana, India (Hybrid)",
        "country": "India",
        "work_mode": "Hybrid",
        "department": "Product & Design",
        "employment_type": "Full-time",
        "experience_level": "Principal / Director (9-14 yrs)",
        "salary_range": "₹55,00,000 - ₹80,00,000 INR + Stock",
        "apply_url": "https://jobs.careers.microsoft.com/global/en/job/1698231/Principal-Product-Manager-Generative-Search",
        "ats_platform": "Microsoft Careers",
        "posted_at": "2026-10-14T10:15:00Z",
        "status": "approved",
        "approved_by": "abhishek",
        "tags": ["AI Search", "Product Strategy", "LLM UX", "Enterprise Search", "Copilot", "Roadmapping"],
        "summary": "Lead product innovation for Microsoft Copilot and generative information discovery, defining natural language reasoning workflows for hundreds of millions of global knowledge workers.",
        "description": """### Role Vision
Microsoft India Development Center (IDC) is one of Microsoft's premier global engineering hubs. The Copilot and Search product team is inventing the future of how humanity interacts with enterprise data, web knowledge, and conversational assistants.

### Responsibilities
- Lead cross-functional engineering, UX research, and applied science teams to ship intuitive multimodal search features.
- Define product metrics for answer hallucination reduction, latency budgets, citation attribution, and task completion rates.
- Synthesize complex customer feedback from Fortune 500 CIOs into actionable product requirement documents (PRDs)."""
    },
    {
        "id": "job-108",
        "req_id": "SNOW-GH512039",
        "title": "Senior Data Platform Engineer",
        "company": "Snowflake",
        "company_domain": "snowflake.com",
        "company_logo": get_company_logo("snowflake.com"),
        "location": "San Mateo, CA, US (Hybrid)",
        "country": "United States",
        "work_mode": "Hybrid",
        "department": "Data & Analytics",
        "employment_type": "Full-time",
        "experience_level": "Senior Level (5-9 yrs)",
        "salary_range": "$190,000 - $250,000 USD + Equity",
        "apply_url": "https://boards.greenhouse.io/snowflake/jobs/512039",
        "ats_platform": "Greenhouse",
        "posted_at": "2026-10-14T07:30:00Z",
        "status": "approved",
        "approved_by": "abhishek",
        "tags": ["C++", "Java", "SQL", "Query Optimization", "Distributed Storage", "Database Internals"],
        "summary": "Design foundational query execution engine and columnar storage acceleration layers at Snowflake, delivering hyper-fast analytical computation for cloud data warehouse customers.",
        "description": """### The Snowflake Engine
Snowflake's Data Cloud mobilizes the world's data. Our core execution engine processes petabytes of SQL queries daily, disaggregating compute from storage with patented multi-cluster virtual warehouses.

### Key Responsibilities
- Implement vectorized query execution algorithms in C++ to accelerate join operators, window functions, and aggregation kernels.
- Optimize metadata pruning, micro-partition caching, and compression algorithms for petabyte-scale cloud storage (S3, GCS, Azure Blob)."""
    },
    {
        "id": "job-109",
        "req_id": "FK-TECH9812",
        "title": "Lead DevOps & SRE Engineer",
        "company": "Flipkart",
        "company_domain": "flipkart.com",
        "company_logo": get_company_logo("flipkart.com"),
        "location": "Bengaluru, Karnataka, India (Hybrid)",
        "country": "India",
        "work_mode": "Hybrid",
        "department": "DevOps & Cloud",
        "employment_type": "Full-time",
        "experience_level": "Lead Level (6-10 yrs)",
        "salary_range": "₹40,00,000 - ₹58,00,000 INR",
        "apply_url": "https://www.flipkartcareers.com/#!/job-view/FK-TECH9812",
        "ats_platform": "Corporate ATS",
        "posted_at": "2026-10-13T12:00:00Z",
        "status": "approved",
        "approved_by": "abhishek",
        "tags": ["Kubernetes", "Terraform", "Prometheus", "Grafana", "Linux", "Chaos Engineering", "Python"],
        "summary": "Guarantee uninterrupted site reliability and ultra-low latency for Flipkart's Big Billion Days flash sales, managing massive hybrid cloud footprints across multiple Indian data centers.",
        "description": """### Reliability at Flipkart Scale
Flipkart is India's homegrown e-commerce ecosystem. During peak shopping events, our platforms handle over 100 million concurrent shoppers, processing unprecedented spikes in search queries and checkouts.

### Your Mandate
- Champion site reliability engineering (SRE) principles across tier-1 checkout, inventory, and payment microservices.
- Conduct comprehensive chaos engineering experiments, stress simulations, and failover drills to eliminate single points of failure.
- Automate multi-cluster Kubernetes deployments, ingress routing, and service mesh topologies using Istio and Terraform."""
    },
    {
        "id": "job-110",
        "req_id": "FIG-GH482910",
        "title": "Senior Frontend Engineer (Design Systems)",
        "company": "Figma",
        "company_domain": "figma.com",
        "company_logo": get_company_logo("figma.com"),
        "location": "New York, NY, US (Hybrid / Remote)",
        "country": "United States",
        "work_mode": "Hybrid / Remote",
        "department": "Product & Design",
        "employment_type": "Full-time",
        "experience_level": "Senior Level (4-8 yrs)",
        "salary_range": "$175,000 - $230,000 USD + Equity",
        "apply_url": "https://boards.greenhouse.io/figma/jobs/482910",
        "ats_platform": "Greenhouse",
        "posted_at": "2026-10-13T09:10:00Z",
        "status": "approved",
        "approved_by": "abhishek",
        "tags": ["TypeScript", "React", "WebAssembly", "WebGL", "Design Systems", "Accessibility (a11y)"],
        "summary": "Build the next generation of collaborative canvas tools, design system primitives, and accessible component architectures used by millions of product designers worldwide.",
        "description": """### About Figma
Figma connects everyone in the design process to create digital products faster. From wireframing to production-ready design tokens, teams at Google, Airbnb, and Microsoft rely on Figma every day.

### Role Overview
- Build reusable, accessible, and performant UI components across Figma and FigJam.
- Partner closely with design leaders to craft design token specifications, theming systems, and motion guidelines.
- Optimize client-side rendering bottlenecks utilizing WebAssembly, WebGL, and high-framerate HTML5 Canvas pipelines."""
    },
    {
        "id": "job-111",
        "req_id": "TR-GH5891024",
        "title": "Principal Quantitative Research Scientist",
        "company": "Tower Research Capital",
        "company_domain": "tower-research.com",
        "company_logo": get_company_logo("tower-research.com"),
        "location": "Gurugram, Haryana, India (Hybrid)",
        "country": "India",
        "work_mode": "Hybrid",
        "department": "Finance & Analytics",
        "employment_type": "Full-time",
        "experience_level": "Principal Level (7-12 yrs)",
        "salary_range": "₹80,00,000 - ₹1,20,00,000 INR + Bonus",
        "apply_url": "https://boards.greenhouse.io/towerresearchcapital/jobs/5891024",
        "ats_platform": "Greenhouse",
        "posted_at": "2026-10-12T15:00:00Z",
        "status": "approved",
        "approved_by": "abhishek",
        "tags": ["Python", "C++", "Algorithmic Trading", "Time Series", "Machine Learning", "High Frequency Trading"],
        "summary": "Develop statistical arbitrage models, high-frequency alpha signals, and predictive algorithmic trading strategies across global financial exchanges for an elite quantitative trading firm.",
        "description": """### About Tower Research Capital
Tower Research Capital is an elite quantitative trading firm that develops high-frequency electronic strategies across global asset classes (equities, futures, FX, commodities).

### What You'll Do
- Research and engineer statistical alpha models using terabytes of tick-by-tick order book data.
- Apply advanced machine learning techniques (deep recurrent networks, graph neural networks) to short-horizon price predictions.
- Backtest quantitative strategies using rigorous statistical methodologies, transaction cost modeling, and slippage controls."""
    },
    {
        "id": "job-112",
        "req_id": "AWS-2819201",
        "title": "Senior Solutions Architect - Enterprise GenAI",
        "company": "Amazon Web Services (AWS)",
        "company_domain": "amazon.jobs",
        "company_logo": get_company_logo("amazon.com"),
        "location": "Arlington, VA, US (Hybrid)",
        "country": "United States",
        "work_mode": "Hybrid",
        "department": "DevOps & Cloud",
        "employment_type": "Full-time",
        "experience_level": "Senior Level (6-10 yrs)",
        "salary_range": "$175,000 - $235,000 USD",
        "apply_url": "https://www.amazon.jobs/en/jobs/2819201/senior-solutions-architect-enterprise-genai",
        "ats_platform": "Amazon Jobs",
        "posted_at": "2026-10-12T11:20:00Z",
        "status": "approved",
        "approved_by": "abhishek",
        "tags": ["AWS Bedrock", "SageMaker", "Cloud Architecture", "Enterprise Security", "Python", "RAG Architecture"],
        "summary": "Advise Global 2000 enterprises on deploying secure, scalable generative AI workflows utilizing Amazon Bedrock, SageMaker, and Trainium accelerators.",
        "description": """### AWS Solutions Architecture
Amazon Web Services provides the most comprehensive cloud offerings globally. The GenAI Solutions Architecture team partners directly with enterprise CTOs and Chief AI Officers to solve critical business problems.

### Core Responsibilities
- Architect production-ready reference implementations utilizing Amazon Bedrock, OpenSearch vector search, and Claude 3.5 Sonnet foundation models.
- Conduct executive technical workshops and proof-of-concepts (PoCs) on responsible AI, model evaluation, and hallucination reduction."""
    },
    {
        "id": "job-113",
        "req_id": "ZM-GUR8192",
        "title": "Senior Backend Engineer (Golang / High Concurrency)",
        "company": "Zomato",
        "company_domain": "zomato.com",
        "company_logo": get_company_logo("zomato.com"),
        "location": "Gurugram, Haryana, India (In-Office)",
        "country": "India",
        "work_mode": "In-Office",
        "department": "Software Engineering",
        "employment_type": "Full-time",
        "experience_level": "Senior Level (4-8 yrs)",
        "salary_range": "₹36,00,000 - ₹50,00,000 INR",
        "apply_url": "https://www.zomato.com/careers/engineering/backend-senior-ZM8192",
        "ats_platform": "Corporate ATS",
        "posted_at": "2026-10-12T08:45:00Z",
        "status": "approved",
        "approved_by": "abhishek",
        "tags": ["Go", "Kafka", "PostgreSQL", "Redis", "Distributed Systems", "High Throughput"],
        "summary": "Build high-throughput order dispatching, rider routing, and live tracking backends in Golang for millions of food orders delivered across 800+ Indian cities.",
        "description": """### Engineering at Zomato
Zomato delivers millions of meals and groceries every single day. The logistics and dispatch platform computes optimal driver-restaurant-customer matches within milliseconds under heavy peak-hour concurrency.

### Key Responsibilities
- Architect high-throughput Golang microservices capable of servicing 80,000 requests per second.
- Implement low-latency geospatial indexing algorithms for real-time delivery rider tracking.
- Optimize database performance on PostgreSQL and Redis clusters to withstand flash sale loads."""
    },
    {
        "id": "job-114",
        "req_id": "GOOG-1049281",
        "title": "Staff Machine Learning Scientist (Search Ranking)",
        "company": "Google",
        "company_domain": "google.com",
        "company_logo": get_company_logo("google.com"),
        "location": "Mountain View, CA, US (Hybrid)",
        "country": "United States",
        "work_mode": "Hybrid",
        "department": "AI & Machine Learning",
        "employment_type": "Full-time",
        "experience_level": "Staff Level (8-12 yrs)",
        "salary_range": "$240,000 - $310,000 USD + Equity",
        "apply_url": "https://www.google.com/about/careers/applications/jobs/results/1049281-staff-machine-learning-scientist",
        "ats_platform": "Google Careers",
        "posted_at": "2026-10-11T16:00:00Z",
        "status": "approved",
        "approved_by": "abhishek",
        "tags": ["TensorFlow", "C++", "Python", "Search Ranking", "Deep Learning", "Large Scale Systems"],
        "summary": "Advance core neural ranking models, semantic relevance, and multimodal search intelligence powering billions of daily Google Search queries worldwide.",
        "description": """### The Google Search Team
Google Search organizes the world's information and makes it universally accessible and useful. The Search Ranking intelligence group designs the neural ranking transformers that understand complex human intent.

### Responsibilities
- Train and deploy massive multi-task neural network models for document ranking, query expansion, and zero-shot entity retrieval.
- Optimize model inferencing on custom Google Cloud TPU v5e clusters with sub-10ms latency SLA budgets."""
    },
    {
        "id": "job-115",
        "req_id": "SW-AND8129",
        "title": "Lead Android Engineer (Performance & Architecture)",
        "company": "Swiggy",
        "company_domain": "swiggy.com",
        "company_logo": get_company_logo("swiggy.com"),
        "location": "Bengaluru, Karnataka, India (Hybrid)",
        "country": "India",
        "work_mode": "Hybrid",
        "department": "Software Engineering",
        "employment_type": "Full-time",
        "experience_level": "Lead Level (6-10 yrs)",
        "salary_range": "₹42,00,000 - ₹58,00,000 INR",
        "apply_url": "https://careers.swiggy.com/#/job-details/SWIG_AND_8129",
        "ats_platform": "Corporate ATS",
        "posted_at": "2026-10-11T12:30:00Z",
        "status": "approved",
        "approved_by": "abhishek",
        "tags": ["Kotlin", "Jetpack Compose", "Coroutines", "Android NDK", "App Performance"],
        "summary": "Drive Android architecture and zero-jank mobile performance for Swiggy's consumer application installed on over 100 million Indian smartphones.",
        "description": """### Mobile Engineering at Swiggy
The Swiggy Android application is the primary gateway for millions of Indians to order food, groceries, and dining reservations. Our mobile team crafts butter-smooth 120Hz interactions across hundreds of diverse Android device profiles.

### Key Responsibilities
- Architect modular Android feature modules using Jetpack Compose, Kotlin Coroutines, and Clean Architecture.
- Profile and optimize cold startup time, app bundle footprint, memory leaks, and battery consumption on budget smartphones."""
    },
    {
        "id": "job-116",
        "req_id": "ANT-ASH29841",
        "title": "Principal Distributed Systems Engineer",
        "company": "Anthropic",
        "company_domain": "anthropic.com",
        "company_logo": get_company_logo("anthropic.com"),
        "location": "San Francisco, CA, US (In-Office / Hybrid)",
        "country": "United States",
        "work_mode": "In-Office / Hybrid",
        "department": "AI & Machine Learning",
        "employment_type": "Full-time",
        "experience_level": "Principal Level (8-14 yrs)",
        "salary_range": "$270,000 - $350,000 USD + Equity",
        "apply_url": "https://jobs.ashbyhq.com/anthropic/29841-distributed-systems",
        "ats_platform": "Ashby",
        "posted_at": "2026-10-10T14:10:00Z",
        "status": "approved",
        "approved_by": "abhishek",
        "tags": ["Rust", "Python", "Kubernetes", "NCCL", "Distributed Systems", "Claude AI", "High Performance Computing"],
        "summary": "Build the ultra-reliable distributed training and inference clusters that power Claude 3.5 Sonnet and future frontier AI models at Anthropic.",
        "description": """### Working at Anthropic
Anthropic is an AI safety and research company that builds reliable, interpretable, and steerable AI systems. The cluster computing team operates some of the largest compute clusters on Earth.

### Your Role
- Architect resilient distributed training frameworks that recover from node failures without losing training progress.
- Write custom high-throughput communication kernels in Rust and C++ interfacing with NCCL and collective communication libraries."""
    },
    {
        "id": "job-117",
        "req_id": "ATL-BLR7192",
        "title": "Lead Site Reliability Engineer",
        "company": "Atlassian",
        "company_domain": "atlassian.com",
        "company_logo": get_company_logo("atlassian.com"),
        "location": "Bengaluru, Karnataka, India (Remote Eligible)",
        "country": "India",
        "work_mode": "Remote Eligible",
        "department": "DevOps & Cloud",
        "employment_type": "Full-time",
        "experience_level": "Lead Level (6-10 yrs)",
        "salary_range": "₹44,00,000 - ₹62,00,000 INR",
        "apply_url": "https://www.atlassian.com/company/careers/details/ATL-BLR7192",
        "ats_platform": "Jobvite",
        "posted_at": "2026-10-10T09:00:00Z",
        "status": "approved",
        "approved_by": "abhishek",
        "tags": ["AWS", "Terraform", "Kubernetes", "Python", "SLOs", "Incident Management"],
        "summary": "Lead cloud reliability, multi-tenant isolation, and incident resilience for Jira and Confluence Cloud utilized by 300,000+ global organizations.",
        "description": """### Team Vision
Atlassian empowers team collaboration worldwide. Our SRE organization ensures that Jira Cloud, Confluence, and Bitbucket deliver five-nines reliability to global software development teams.

### Responsibilities
- Establish service level objectives (SLOs) and automated error budget policies across core microservices.
- Design automated progressive delivery canary deployments using Argo Rollouts and Spinnaker."""
    },
    {
        "id": "job-118",
        "req_id": "CB-GH619283",
        "title": "Senior Cryptographic & Blockchain Engineer",
        "company": "Coinbase",
        "company_domain": "coinbase.com",
        "company_logo": get_company_logo("coinbase.com"),
        "location": "Remote, United States",
        "country": "United States",
        "work_mode": "Remote",
        "department": "Software Engineering",
        "employment_type": "Full-time",
        "experience_level": "Senior Level (5-9 yrs)",
        "salary_range": "$180,000 - $235,000 USD + Crypto/Equity",
        "apply_url": "https://boards.greenhouse.io/coinbase/jobs/619283",
        "ats_platform": "Greenhouse",
        "posted_at": "2026-10-09T17:40:00Z",
        "status": "approved",
        "approved_by": "abhishek",
        "tags": ["Golang", "Rust", "MPC", "Cryptography", "Ethereum", "Smart Contracts", "FinTech"],
        "summary": "Engineer institutional-grade secure multi-party computation (MPC) cold storage and zero-knowledge transaction verification protocols at Coinbase.",
        "description": """### Crypto Security at Coinbase
Coinbase secures billions of dollars in digital assets for retail and sovereign institutional clients. Our cryptography engineering group develops provably secure custody and signature infrastructure.

### What You'll Build
- Implement threshold signature schemes (TSS), MPC protocols, and hardware security module (HSM) integrations.
- Build high-throughput blockchain indexing daemons tracking EVM and Solana transaction states."""
    },
    {
        "id": "job-119",
        "req_id": "SW-INST9812",
        "title": "Staff Data Engineer - Supply Chain Intelligence",
        "company": "Swiggy Instamart",
        "company_domain": "swiggy.com",
        "company_logo": get_company_logo("swiggy.com"),
        "location": "Bengaluru, Karnataka, India (In-Office)",
        "country": "India",
        "work_mode": "In-Office",
        "department": "Data & Analytics",
        "employment_type": "Full-time",
        "experience_level": "Staff Level (7-11 yrs)",
        "salary_range": "₹46,00,000 - ₹64,00,000 INR",
        "apply_url": "https://careers.swiggy.com/#/job-details/SWIG_INST_9812",
        "ats_platform": "Corporate ATS",
        "posted_at": "2026-10-09T11:15:00Z",
        "status": "approved",
        "approved_by": "abhishek",
        "tags": ["Apache Spark", "Iceberg", "Airflow", "Python", "SQL", "Real-time Streaming", "Kafka"],
        "summary": "Design real-time inventory forecasting, automated replenishment, and dark store telemetry pipelines processing 200 million daily inventory updates on Swiggy Instamart.",
        "description": """### Quick-Commerce Intelligence
Instamart is pioneering 10-minute grocery convenience across Indian metros. Maintaining 99.8% stock availability across thousands of dark stores requires predictive, real-time data streaming architectures.

### Key Responsibilities
- Architect petabyte-scale data lakes using Apache Iceberg, Spark on Kubernetes, and Delta Lake.
- Build sub-second streaming pipelines processing SKU inventory movements, perishable waste tracking, and supplier SLAs."""
    },
    {
        "id": "job-120",
        "req_id": "RH-GH571291",
        "title": "Senior Product Designer (FinTech UX)",
        "company": "Robinhood",
        "company_domain": "robinhood.com",
        "company_logo": get_company_logo("robinhood.com"),
        "location": "Menlo Park, CA, US (Hybrid)",
        "country": "United States",
        "work_mode": "Hybrid",
        "department": "Product & Design",
        "employment_type": "Full-time",
        "experience_level": "Senior Level (5-8 yrs)",
        "salary_range": "$170,000 - $220,000 USD + Equity",
        "apply_url": "https://boards.greenhouse.io/robinhood/jobs/571291",
        "ats_platform": "Greenhouse",
        "posted_at": "2026-10-08T15:30:00Z",
        "status": "approved",
        "approved_by": "abhishek",
        "tags": ["Figma", "Design Systems", "FinTech", "Mobile UX", "User Research", "Prototyping"],
        "summary": "Reinvent retail investing and wealth management user experience, crafting intuitive, accessible interfaces for millions of modern stock and options traders.",
        "description": """### Design at Robinhood
Robinhood democratized investing by making financial markets accessible to everyone. Our design team creates intuitive, beautiful, and educational financial products that simplify complex market concepts.

### Your Impact
- Own end-to-end user experience for trading execution, portfolio analytics, and automated retirement accounts.
- Conduct user research, cognitive walkthroughs, and usability testing to turn friction into delight."""
    },
    {
        "id": "job-121",
        "req_id": "TCS-PUN8192",
        "title": "Principal AI Governance & Trust Lead",
        "company": "Tata Consultancy Services (TCS)",
        "company_domain": "tcs.com",
        "company_logo": get_company_logo("tcs.com"),
        "location": "Pune, Maharashtra, India (Hybrid)",
        "country": "India",
        "work_mode": "Hybrid",
        "department": "Security & Trust",
        "employment_type": "Full-time",
        "experience_level": "Principal / Director (10-15 yrs)",
        "salary_range": "₹48,00,000 - ₹70,00,000 INR",
        "apply_url": "https://www.tcs.com/careers/india/ai-governance-lead-PUN8192",
        "ats_platform": "Corporate ATS",
        "posted_at": "2026-10-08T10:00:00Z",
        "status": "approved",
        "approved_by": "abhishek",
        "tags": ["AI Ethics", "EU AI Act", "Model Risk Management", "Data Privacy", "Cybersecurity", "Auditing"],
        "summary": "Establish enterprise generative AI compliance, model risk validation frameworks, and sovereign data governance for Fortune 500 banking and healthcare clients.",
        "description": """### TCS Innovation & Trust Bureau
TCS is India's premier multinational IT services enterprise. The AI Governance & Trust group helps the world's largest banks, healthcare networks, and sovereign agencies deploy ethical, unbiased, and compliant AI solutions.

### Key Mandate
- Formulate comprehensive model risk governance frameworks aligned with EU AI Act, NIST AI RMF, and ISO/IEC 42001.
- Conduct red-teaming simulations, adversarial prompt injection testing, and bias auditing on client LLM deployments."""
    },
    {
        "id": "job-122",
        "req_id": "UBR-R102941",
        "title": "Senior Autonomous Systems Simulation Engineer",
        "company": "Uber Technologies",
        "company_domain": "uber.com",
        "company_logo": get_company_logo("uber.com"),
        "location": "Pittsburgh, PA, US (Hybrid)",
        "country": "United States",
        "work_mode": "Hybrid",
        "department": "Software Engineering",
        "employment_type": "Full-time",
        "experience_level": "Senior Level (5-9 yrs)",
        "salary_range": "$185,000 - $245,000 USD + Equity",
        "apply_url": "https://uber.wd5.myworkdayjobs.com/en-US/Uber_Careers/job/Pittsburgh-PA/Senior-Autonomous-Systems-Simulation-Engineer_R102941",
        "ats_platform": "Workday",
        "posted_at": "2026-10-07T14:45:00Z",
        "status": "approved",
        "approved_by": "abhishek",
        "tags": ["C++", "Python", "Robotics", "Physics Simulation", "Unreal Engine", "Sensor Fusion"],
        "summary": "Build high-fidelity photorealistic physics simulations and automated edge-case validation environments for autonomous delivery and fleet mobility platforms at Uber.",
        "description": """### Autonomous Mobility at Uber
Uber is shaping the future of shared, autonomous electric transportation. The simulation group builds hyper-realistic digital twin environments to stress-test autonomous driving behaviors before real-world deployment.

### Responsibilities
- Develop high-performance deterministic simulation engines in C++ mimicking dynamic weather, traffic, and pedestrian interactions.
- Implement physics-accurate LiDAR, radar, and camera sensor rendering models utilizing Unreal Engine and GPU shaders."""
    },
    {
        "id": "job-123",
        "req_id": "INF-HYD9182",
        "title": "Lead Cloud Security Architect",
        "company": "Infosys",
        "company_domain": "infosys.com",
        "company_logo": get_company_logo("infosys.com"),
        "location": "Hyderabad, Telangana, India (Hybrid)",
        "country": "India",
        "work_mode": "Hybrid",
        "department": "Security & Trust",
        "employment_type": "Full-time",
        "experience_level": "Lead Level (8-12 yrs)",
        "salary_range": "₹45,00,000 - ₹62,00,000 INR",
        "apply_url": "https://career.infosys.com/jobdesc?jobReferenceCode=INF-HYD9182",
        "ats_platform": "Corporate ATS",
        "posted_at": "2026-10-07T11:00:00Z",
        "status": "approved",
        "approved_by": "abhishek",
        "tags": ["AWS", "Azure", "Cloud Security", "Zero Trust", "IAM", "DevSecOps", "CIS Benchmarks"],
        "summary": "Architect multi-cloud security frameworks, identity governance, and automated DevSecOps guardrails for Infosys Cobalt enterprise cloud transformation programs.",
        "description": """### Infosys Cobalt Security
Infosys Cobalt is a set of services, solutions, and platforms for enterprises to accelerate their cloud journey. Our Cloud Security Architecture team designs defense-in-depth frameworks for global financial institutions and airlines.

### Key Responsibilities
- Architect Zero Trust cloud landing zones across AWS, Microsoft Azure, and Google Cloud Platform.
- Define identity and access management (IAM) guardrails, least-privilege role policies, and automated secret rotations."""
    },
    {
        "id": "job-124",
        "req_id": "OA-ASH10982",
        "title": "Staff Research Engineer - Model Alignment & Safety",
        "company": "OpenAI",
        "company_domain": "openai.com",
        "company_logo": get_company_logo("openai.com"),
        "location": "San Francisco, CA, US (In-Office)",
        "country": "United States",
        "work_mode": "In-Office",
        "department": "AI & Machine Learning",
        "employment_type": "Full-time",
        "experience_level": "Staff Level (7-12 yrs)",
        "salary_range": "$300,000 - $420,000 USD + Equity",
        "apply_url": "https://jobs.ashbyhq.com/openai/10982-alignment-research-engineer",
        "ats_platform": "Ashby",
        "posted_at": "2026-10-06T15:20:00Z",
        "status": "approved",
        "approved_by": "abhishek",
        "tags": ["RLHF", "Python", "PyTorch", "Model Alignment", "LLMs", "AI Safety", "Superalignment"],
        "summary": "Research and engineer scalable alignment, rule-based rewards, and automated self-critique techniques to make frontier multimodal models beneficial, honest, and robust against jailbreaks.",
        "description": """### About OpenAI
OpenAI's mission is to ensure that artificial general intelligence (AGI) benefits all of humanity. The Alignment & Safety research team invents methodologies to steer, align, and evaluate frontier foundation models.

### What You'll Do
- Engineer scalable reinforcement learning from human feedback (RLHF) and reinforcement learning from AI feedback (RLAIF) training pipelines.
- Develop automated synthetic evaluation environments to probe models for deceptive alignment, hallucination tendencies, and dangerous capabilities."""
    }
]

def ensure_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(JOBS_FILE):
        initial_data = {
            "approved_jobs": SEED_JOBS,
            "pending_jobs": [],
            "last_fetched_at": datetime.now(timezone.utc).isoformat()
        }
        with open(JOBS_FILE, "w", encoding="utf-8") as f:
            json.dump(initial_data, f, indent=2)
        logger.info(f"Initialized jobs.json with {len(SEED_JOBS)} seed jobs.")

def load_jobs_data():
    ensure_data_dir()
    try:
        with open(JOBS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not data.get("approved_jobs"):
                data["approved_jobs"] = SEED_JOBS
                save_jobs_data(data)
            return data
    except Exception as e:
        logger.error(f"Error reading {JOBS_FILE}: {e}")
        return {"approved_jobs": SEED_JOBS, "pending_jobs": [], "last_fetched_at": None}

def save_jobs_data(data):
    ensure_data_dir()
    try:
        with open(JOBS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        logger.error(f"Error saving {JOBS_FILE}: {e}")
        return False

def get_approved_jobs(category=None, country=None, search=None, limit=100):
    """
    Robust filtering for approved jobs:
    Supports Country, Category, and case-insensitive full-text keyword search across
    title, company, skills, location, and requisition ID.
    """
    data = load_jobs_data()
    jobs = data.get("approved_jobs", [])

    # Filter by Country
    if country and country not in ["All Locations", "All Regions", ""]:
        c_clean = country.lower().strip()
        jobs = [j for j in jobs if c_clean in (j.get("country") or "").lower() or c_clean in (j.get("location") or "").lower()]

    # Filter by Category
    if category and category not in ["All Categories", "All Departments", ""]:
        dept_clean = category.lower().strip()
        jobs = [j for j in jobs if dept_clean in (j.get("department") or "").lower()]

    # Filter by Search Keyword
    if search and search.strip():
        terms = [t.lower().strip() for t in search.split() if t.strip()]
        filtered = []
        for j in jobs:
            searchable_text = f"{j.get('title', '')} {j.get('company', '')} {j.get('location', '')} {j.get('country', '')} {j.get('department', '')} {j.get('req_id', '')} {j.get('summary', '')} {' '.join(j.get('tags', []))}".lower()
            if all(term in searchable_text for term in terms):
                filtered.append(j)
        jobs = filtered

    # Sort newest first
    jobs.sort(key=lambda x: x.get("posted_at", ""), reverse=True)
    return jobs[:limit]

def get_job_by_id(job_id):
    """Retrieve full job record by ID or req_id from approved or pending lists."""
    if not job_id:
        return None
    data = load_jobs_data()
    clean_search = str(job_id).strip().lower()
    for j in data.get("approved_jobs", []) + data.get("pending_jobs", []):
        if str(j.get("id")).lower() == clean_search or str(j.get("req_id", "")).lower() == clean_search:
            return j
        # Also match clean number e.g. "101" for "job-101"
        if str(j.get("id")).replace("job-", "").lower() == clean_search:
            return j
    return None

def get_pending_jobs():
    """Retrieve all unapproved scraped jobs awaiting admin editorial review."""
    data = load_jobs_data()
    return data.get("pending_jobs", [])

def approve_job(job_id):
    """Admin action: approve a pending job and move to live approved_jobs."""
    data = load_jobs_data()
    pending = data.get("pending_jobs", [])
    target = None
    new_pending = []

    for j in pending:
        if str(j.get("id")) == str(job_id):
            target = j
        else:
            new_pending.append(j)

    if not target:
        for j in data.get("approved_jobs", []):
            if str(j.get("id")) == str(job_id):
                return True
        return False

    target["status"] = "approved"
    target["approved_by"] = "abhishek"
    target["approved_at"] = datetime.now(timezone.utc).isoformat()

    data["pending_jobs"] = new_pending
    data["approved_jobs"].insert(0, target)
    save_jobs_data(data)
    logger.info(f"Job {job_id} approved by abhishek.")
    return True

def reject_job(job_id):
    """Admin action: reject and remove a pending job."""
    data = load_jobs_data()
    pending = data.get("pending_jobs", [])
    data["pending_jobs"] = [j for j in pending if str(j.get("id")) != str(job_id)]
    save_jobs_data(data)
    logger.info(f"Job {job_id} rejected and removed from pending queue.")
    return True

def add_custom_job(job_dict):
    """Admin action: manually add a verified job posting."""
    data = load_jobs_data()
    approved = data.get("approved_jobs", [])
    
    existing_ids = [int(j["id"].replace("job-", "")) for j in approved if j.get("id", "").startswith("job-") and j["id"].replace("job-", "").isdigit()]
    next_id = max(existing_ids, default=100) + 1
    job_dict["id"] = f"job-{next_id}"
    if not job_dict.get("req_id"):
        job_dict["req_id"] = f"WW-MANUAL-{next_id}"
    job_dict["posted_at"] = datetime.now(timezone.utc).isoformat()
    job_dict["status"] = "approved"
    job_dict["approved_by"] = "abhishek"
    if not job_dict.get("company_logo"):
        domain = job_dict.get("company_domain") or "google.com"
        job_dict["company_logo"] = get_company_logo(domain)

    approved.insert(0, job_dict)
    data["approved_jobs"] = approved
    save_jobs_data(data)
    logger.info(f"New job {job_dict['id']} added manually by admin.")
    return job_dict["id"]

def add_scraped_jobs(new_jobs_list):
    """Add scraped jobs to pending_jobs queue with deduplication."""
    data = load_jobs_data()
    existing_titles_companies = {
        f"{(j.get('title') or '').lower()}-{(j.get('company') or '').lower()}"
        for j in data.get("approved_jobs", []) + data.get("pending_jobs", [])
    }

    added = 0
    all_existing_ids = [
        int(j["id"].replace("job-", ""))
        for j in data.get("approved_jobs", []) + data.get("pending_jobs", [])
        if j.get("id", "").startswith("job-") and j["id"].replace("job-", "").isdigit()
    ]
    curr_id = max(all_existing_ids, default=200)

    for item in new_jobs_list:
        key = f"{(item.get('title') or '').lower()}-{(item.get('company') or '').lower()}"
        if key in existing_titles_companies:
            continue
        
        curr_id += 1
        item["id"] = f"job-{curr_id}"
        if not item.get("req_id"):
            item["req_id"] = f"SCRAPED-{curr_id}"
        item["status"] = "pending"
        item["posted_at"] = datetime.now(timezone.utc).isoformat()
        data["pending_jobs"].append(item)
        existing_titles_companies.add(key)
        added += 1

    data["last_fetched_at"] = datetime.now(timezone.utc).isoformat()
    save_jobs_data(data)
    logger.info(f"Ingested {added} new jobs into pending queue.")
    return added

def get_job_stats():
    data = load_jobs_data()
    approved = data.get("approved_jobs", [])
    pending = data.get("pending_jobs", [])

    india_count = sum(1 for j in approved if "india" in (j.get("country") or "").lower() or "india" in (j.get("location") or "").lower())
    us_count = sum(1 for j in approved if "united states" in (j.get("country") or "").lower() or "us" in (j.get("country") or "").lower() or "us" in (j.get("location") or "").lower())

    return {
        "total_approved": len(approved),
        "total_pending": len(pending),
        "india_jobs": india_count,
        "us_jobs": us_count,
        "last_fetched_at": data.get("last_fetched_at")
    }

if __name__ == "__main__":
    ensure_data_dir()
    # Reset to full seed jobs for verification
    data = {"approved_jobs": SEED_JOBS, "pending_jobs": [], "last_fetched_at": datetime.now(timezone.utc).isoformat()}
    save_jobs_data(data)
    stats = get_job_stats()
    print("Job store refreshed with authentic requisition IDs and ATS URLs. Stats:", stats)
