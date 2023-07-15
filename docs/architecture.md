# Architecture

DataOS is a distributed cloud computing system based on micro-services architecture. This makes the services within its collection -

- Loosely coupled
- Independently deployable
- Work with different technologies and programming languages
- Independently scalable

Each service within DataOS is self-contained and implements a single business capability within a *bounded context*. So each data management capability, such as data cataloging, access control or data security, is governed by a different service.

---

These are some of the services of DataOS acting as a cohesive whole to form the unified architecture for data infrastructure:

### Heimdall

Heimdall is the decision engine for all access control within DataOS. Whether it is access to a dataset, an API path or other applications & services of the operating system, Heimdall acts as the Policy Decision Point (PDP) for all kinds of ingress and authorizations.

### Metis

Metis is the metadata manager of DataOS. It collates & curates operational metadata, technical & business metadata from various data sources, as well as DataOS Resources. Metis serves this metadata via a graphical user interface for consumption by data developers. Combined with Odin (service for Knowledge Graphs), it forms a semantic web to generate ontologies with specific business values. 

### Gateway

A service which runs on top of the query engine, Minerva, and is responsible for managing Minerva clusters, user authentication (via calls to Heimdall), as well as data policy decisions. It acts as the PDP for data filtering and masking so that the data is not masked/filtered at the source directly, but at the time of query parsing.

### Caretaker

It captures, stores & serves information related to pods (such as pod states & aggregates) or compute nodes. It maintains the historical data in blob storage while serving the current states of running pods via the Operations app.

---

The low coupling and high functional cohesion of the above services, and others, capacitate DataOS to support fault isolation, as well as polyglot programming while building new applications & features, as services do not need to share the same libraries or frameworks. This also makes DataOS flexible and future-proof, as new technologies & data management capabilities can be added rapidly and reliably.

These services persist their own data & state in a dedicated database. They communicate with one another via well-defined REST APIs, and any communication from outside DataOS’ private network must pass through a network gateway.

---

> The architecture of DataOS can be analysed & studied with different vistas. These are:
> 
> 
> > As micro-services architecture
> > 
> 
> > As a data infrastructure
> > 
> 
> > As an operating system
> > 
> 
> Each leads us to the same conclusion - a modular, composable, and interoperable data infrastructure which is built on open standards - making it extensible, future-proof, and flexible enough to be used with your existing tools and infrastructure while also allowing implementation of new data management patterns, such as Data Developer Platform, Data Mesh or Data-first Stack. 
> 

---

Let us look at it from the perspective of data infrastructure.

## Data-management Architecture

![dataos architecture .jpg](Architecture%20bbe8f327ecc24a5990a4bb5a56961456/dataos_architecture_.jpg)

### Zero Trust Network

The communications between the microservices are based on a zero-trust principle. This means that access to pods, services, or applications requires explicit configurations in the form of Network Policies every time they are accessed.

### API Gateway

It acts as the ingress controller for traffic from outside the private network where DataOS is installed. It performs two important functions - that of reverse proxy and load balancer. Any ingress request from any user (application or person) passes through the API Gateway, from wherein they are forwarded to Heimdall. Heimdall authorizes the user, but authentication is federated to an external OIDC, like Azure AD or Google’s OpenID Connect.
