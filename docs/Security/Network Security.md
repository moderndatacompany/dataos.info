# Network Security

DataOS is designed with security measures that are used to maintain the integrity, availability, authentication, and confidentiality of the information being transmitted. It provides network protection techniques to secure network communication within DataOS and for the requests coming from the public internet.

### Ingress Network Security

The DataOS compute tier can use virtual machines placed in a private network.
The virtual machines have their own private IP addresses. The private network has a firewall with highly restrictive ingress rules from public IP addresses on ports 80, 443, and 7432. Port 80 is required for public certificate creation and rotation from Letsencrypt. Port 443 is for all applications to talk with services using HTTPS. Port 7432 is for the Minerva query engine to expose its streaming services which use HTTPS.


> 🗣 Additionally, all ingress traffic goes through a policy enforcement point (Network Gateway), which validates with Heimdall if a request is allowed.

### Cluster Network Security

DataOS uses a zero-trust network perspective to implement internal security measures. All communication between applications and services is explicitly defined as a communication policy, reducing malicious access to internal services.

DataOS also implements a service mesh for applications and services. The mesh requires every application and service to have an envoy proxy sidecar. All communication is done through the envoy proxy, ensuring an explicitly allowed communication policy and creating a mutual TLS connection between envoys. DataOS is designed with security measures that are used to maintain the integrity, availability, authentication, and confidentiality of the information being transmitted. It provides network protection techniques to secure network communication within DataOS and for the requests coming from the public internet.