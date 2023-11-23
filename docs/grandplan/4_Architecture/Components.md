# Local Systems

The local systems within a Digital Hamlet are designed to operate independently and provide all necessary services for the Hamlet's functioning. These systems include:

## Holochain

For distributed data storage and peer-to-peer application logic.

## Local Database

A combination of SQL and NoSQL databases to store and manage local data efficiently.

## Agent Foundry

The development and maintenance hub for AI agents within the Hamlet.

## Geography

A geographical framework that will be used to model the Hamlet. This will also contribute to a geographical representation of connected hamlets and presumably the whole world wide network of hamlets.

## Agency Foundry

The basis of default local agencies and the abstract class for the creation of new agencies as required.

### Default Agencies 

#### Sovereign Institution

An agency that provides high-level management and governance over the hamlet. It contains the VeritasSuprema and AI agents that can interact with the sovereign user by default.

#### Central bank

Manages local and foreign currency. Issues currency to banks to loan out to resident agents to fulfil planned and approved projects. Also, manages inter-hamlet exchange and governance.
 
# External Systems

External systems facilitate interaction with the broader network of Hamlets and other external services. Key components include:

>[!NOTE]
>As mentioned in Architecture.md, it appears that Holochain will satisfy much of the requiremments of the project. At any cost ActivityPub will be redundant unless the chosen solution for a social platform also complies to ActivityPub protocol.

- **Flux / AD4M**: Flux is a social networking platform build on top off AD4M
  - **ActivityPub**: For social networking and communication between Hamlets. As per note, ActivityPub is probably suplerfluous and there will be a holochain native solution
- **IPFS**: For distributed file storage and sharing across the network.
  - An AD4M video showed how *languages* can bridge betwen things like IPFS
- **Digital Currency Protocols**: Standards like ERC-20 and ERC-721 for token interoperability and transactions.

# Bridging Systems

Bridging systems ensure seamless integration and communication between the local and external systems, maintaining the autonomy of the Hamlet while enabling collaboration and interoperability.

# Agent Foundry

The Agent Foundry is the cornerstone of the Digital Hamlet's development, responsible for creating and refining AI agents. It is the first system to be developed, setting the foundation for the Hamlet's growth and evolution.
