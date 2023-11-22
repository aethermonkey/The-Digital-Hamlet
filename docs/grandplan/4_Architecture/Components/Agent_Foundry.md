# Agent Foundry

The Agent Foundry is the cornerstone of the Digital Hamlet's development, responsible for creating and refining AI agents. It is the first system to be developed, setting the foundation for the Hamlet's growth and evolution.

## SDKs / APIs

When choosing a platform to build agents it can be difficult to know which will stand the test of time. The rapid pace of development of various opensource packages has flooded the space with many options that may not be updated or maintained in the near future.

As a reliable platform, the Agent Foundry should be vigilant, flexible and willing to leverage more than just one system. Given this requirement, a database of packages, both current and expired should be maintained along with important details, like urls for documentation, and summarised sdk for ai agent reference.

A starting source of agent possibilities: https://github.com/e2b-dev/awesome-sdks-for-ai-agents

## The Foundry Agents

Foundry agents will need to build, monitor, and evaluate the performance of all agents built. Some roles include:

### Package Researcher and database maintainer

An agent that keeps track of current ai agent frameworks, maintains the database of what is useable and effective and what is not. This agent summarises sdk and api documentation, and populates database with important information pertaining to available packages.

### Agent Builder / Breaker

Self explanatory. This agent responds to director agent's request to get to work building or breaking.

### Director

The director takes requests from other agencies to build new ai agents or remove ineffective agents. The director liases with the researcher to know what the best options are, and then passes directions to the builder / breaker to get to work. The director is able to liase with various civic agents across the hamlet.