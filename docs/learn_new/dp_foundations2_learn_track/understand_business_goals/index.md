# Understanding Business Goals

!!! info "Overview"
    This topic provides a structured approach to identify the **North Star Metric** for your business and develop a consumer-aligned Data Product by working backward from business goals to source data. Each step builds on the previous one, ensuring a clear alignment between business objectives and technical execution.

## Quick Concepts

Consumer-aligned Data Products, also known as Model-first Data Products, are designed by prioritising the end-user's needs and desired business outcomes. The process begins by defining these outcomes, with a strong emphasis on semantics and context. Rather than starting with raw data, development focuses on the logical semantic model which becomes the primary way users will access and understand the data.  This ensures that all data efforts directly support predefined business goals.

So, you start by clearly defining the desired outcome or goal of your data analysis before gathering and processing the necessary data.


## Step 1: Define the vision and goals

Vision is a single, concise statement representing the high-level value the Data Product aims to deliver.

- Define the vision and with stakeholders ensure alignment and agreement.

Goals is specific targets that deliver on the vision, with measurable success indicators.

- Conduct a collaborative session to define clear, quantifiable goals and associated measures.

**Questions to ask:**

What business problems are we solving with this Data Product?
Who are the key stakeholders, and what insights do they need?
How will this Data Product support decision-making processes?

## Step 2: Define hypotheses and initiatives

Hypotheses is a statements linking initiatives to goals such as  “We believe that `<initiative>` will help achieve `<goal>`.”

- Brainstorm and finalize the most promising hypotheses with stakeholders.

Initiatives are approaches to realize the goals. Multiple initiatives might support one goal.

- Define and evaluate different initiatives to determine feasibility and relevance.

## Step 3: Prioritize use cases and Data Products

Use Cases are practical applications of the chosen hypothesis.

- Identify and prioritize use cases based on business needs.
- Map each use case to relevant Data Products.

Data Products are components interacting to fulfill use cases.

- Identify data producers (sources) and consumers (stakeholders, systems).
- Define dependencies across domains if applicable.

## Step 4: Identify Usage Patterns

Try to ask questions to find the following:

**Frequency**: How often will the Data Product be used?

**Users**: Who are the end-users or systems?

**Requirements**: Completeness, freshness, and accuracy expectations?

**Update Cadence**: What’s the schedule for data updates?

- Define architectural expectations based on consumer behavior and objectives.

## Step 5: Define Service Level Objectives (SLOs)

**Key Metrics:**

- **Architecture**: Performance, scalability, and reliability.
- **Data Quality**: Completeness, freshness, and accuracy.
- **Governance**: Compliance with regulations like GDPR, HIPAA, etc.

**Action**:

- Document target metrics and map them to goals to guide development.

## Closing the Loop: North Star Metric Identification

1. **Start with the North Star Metric:**
    - Define what success looks like for your business in terms of measurable outcomes.
    - Document target metrics and map them to goals to guide development.
    - Align all goals and initiatives to this metric.
2. **Work backward:**
    - Identify the measures, dimensions, and data sources required to track progress.
    - Ensure every step ties back to achieving the North Star Metric.
3. **Build with purpose:**
    - Use the right-to-left approach to design a Data Product that directly serves the defined goals.

## Next step

Let us understand the above steps in action with the example of the *‘Product Affinity’ Data Product. We will design this Data Product* to analyze customer purchasing patterns to identify product affinities and opportunities for cross-selling. This Data Product is aimed to help marketing and sales teams create targeted campaigns, enhance customer experience, and increase revenue through strategic product recommendations.

Refer to the next topic:

👉 [Designing Data Products](/learn_new/dp_foundations2_learn_track/design_dp/)