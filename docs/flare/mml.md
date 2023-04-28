What is MML
Why adopt MML?
Challenges that MML can solve
Key considerations for MML
What all scenarios where you consider using MML
Best Use case
How MML works?
    Components
    What you require to set up MML
    How to set up MML




Stand alone related.

Canarying is a process whereby you partially deploy your service (in this case, the pipeline application) and monitor the results. For a more detailed discussion of canarying, see Canarying Releases. Canarying is tied to the entire pipeline rather than a single process. During a canary phase, you may choose to process the same real production data as the live pipeline but skip writes to production storage; techniques such as two-phase mutation can help (see Idempotent and Two-Phase Mutations). Often, you’ll have to wait for the complete cycle of processing to finish before you can discover any customer-impacting issues. After your dry run (or two-phase mutation), compare the results of your canary pipeline with your live pipeline to confirm their health and check for data differences.


A semantic layer is a business representation of corporate data that helps end users access data autonomously using common business terms. A semantic layer maps complex data into familiar business terms such as product, customer, or revenue to offer a unified, consolidated view of data across the organization.

I’ve seen implementations try to deliver BI without a semantic layer. They end up building lots of indexes, views, and aggregate tables, just to get their solution to perform. They also write complex SQL to emulate calculated measures and hierarchies. These issues are solved, out of the box, with a good semantic layer. My advice is to definitely include a semantic layer in your solution, even if its unfamiliar to you.

The biggest downside of a Semantic Layer is you have to build, maintain and manage it. The layer must be kept in sync with any database changes that occur. 

Within a cloud environment, compute nodes form a core of resources. They supply the processing, memory, network, and storage that virtual machine instances need. When an instance is created, it is matched to a compute node with the available resources.
