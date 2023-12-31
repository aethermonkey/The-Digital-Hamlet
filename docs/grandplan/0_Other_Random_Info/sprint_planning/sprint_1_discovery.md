# Discovery Phase

## Defining the Tech Stack
The tech stack for the project is defined as follows:

1. Programming Languages: Python will be used for both backend and frontend development. The team has expertise in Python and it is versatile and easy to learn. Libraries that will be used include pyautogen, dotenv, flask, and SQL and vector database libraries.
2. Specific Requirements: The project requires prompting agents using Prompt Engineering. Python has libraries like `prompt-toolkit` that can help in building interactive command-line applications. Knowledge graphs and hypergraphs will be used for AI reasoning and understanding.
3. Technology Preferences: Open source technologies are preferred. Python, Flask/Django, and SQL databases are all open source. For the frontend, Flask and Svelte.js will be used along with a CSS framework that supports theme changes like dark mode.
4. Databases: SQL will be used for managing relational data. A specific SQL database like PostgreSQL or MySQL may be used.
5. Frameworks: Flask or Django may be used for building the frontend and APIs.
6. Testing: A simple and effective testing methodology will be chosen, including unit testing and integration testing.
7. CI/CD: A simple and effective CI/CD tool will be chosen.
8. Version Control: GitHub will be used for version control.
9. Project Management: An open source project management tool will be chosen.
10. Coding Standards: A simple and widely accepted coding standard will be chosen.
11. Documentation: Sphinx will be used for documentation.
12. Server Environment: The core codebase will be run locally. APIs like OpenAI will be sourced elsewhere.
13. Other Technologies: Knowledge graphs and hypergraphs for AI reasoning and understanding.

## Creating Detailed Agent Stories
Detailed user stories for the first sprint are as follows:

- As an Agent, I want to have an authorisation level that limits my access to information and abilities depending on various factors.
- As a Library Agent, I want to store and manage all knowledge in a structured and searchable format, so that other agents can easily access and use this knowledge.
- As a Towncenter Agent, I want to administer the central bulletin board for all resident agents, so that they can stay informed about hamlet news and changes, and interact with one another.

These stories will guide the development process for the first sprint. Each story clearly defines who the user is (the agent), what they want (their goal), and why they want it (the benefit). This format helps to keep the focus on the user's needs throughout the development process.

## Defining the Towncenter as a Geographical Entity
The Towncenter, like all other localities in the hamlet, is a GeoEntity. The `GeoEntity` class is a parent class that represents a geographical entity. It has attributes like `name` and `location`.

## Creating the Underlying Classes
The `Towncenter` class is a child class of `GeoEntity` and it inherits these attributes from the parent class. In addition to these inherited attributes, the `Towncenter` class also has its own attribute `bulletin_board`. These classes have been defined in the `src/hamlet/hamlet.py` and `src/hamlet/towncenter/towncenter.py` files respectively.

## Planning the Sprint
The sprint will involve developing the functionality for the Agent, Library Agent, and Towncenter Agent stories. The details of how the system will achieve these goals will be worked out during the development process, often during discussions between the developers and the product owner.
