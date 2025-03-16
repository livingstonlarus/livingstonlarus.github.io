# Otobotto: An Autonomous AI Swarm Architecture for Enterprise Software Development

**Jonathan Métillon**  
*Independent Researcher*  
jonathan@livingstonlarus.com

## Abstract

This paper presents **Ōtobotto**, a novel autonomous AI swarm architecture designed for enterprise-grade software development. While advancements in Large Language Models (LLMs) have fueled a new generation of AI coding assistants and multi-agent frameworks, industry leaders like Bret Taylor observe that we remain in an “*Autopilot Era*” where AI tools primarily assist human developers rather than achieving true autonomy. **Ōtobotto** aims to bridge the gap between current capabilities and the stringent requirements of enterprise software engineering through three key innovations: **(1)** a decentralized swarm coordination protocol enabling multiple specialized agents to collaborate in parallel (as peers rather than sequential hand-offs), **dynamically spawning new specialist agents on-the-fly** based on task needs (instead of relying on a fixed set of roles), **(2)** a hierarchical memory system with adaptive token optimization to maintain broad context without overwhelming model limits, and **(3)** an enterprise-grade verification workflow integrating Git-based version control and test-driven development from the outset. Unlike prior systems such as Runic or MetaGPT that rely on a single orchestrator or strictly sequential role pipelines, Otobotto proposes a **dynamic, peer-based swarm** of AI agents working concurrently – each agent a “virtual engineer” that self-configures for its assigned task, allowing essentially **unlimited scalability** in virtual engineering capacity. This approach enables continuous development with cross-verification while potentially reducing token consumption and overhead. We outline the architecture and theoretical framework of Otobotto and argue that it represents a concrete step toward Taylor’s vision of an “*Autonomous Era*” of software development. The architecture is positioned not as a competitor to existing tools, but as an integrative platform that could incorporate and enhance frameworks like LangChain, AgentKit, and emerging protocols such as Anthropic’s Model Context Protocol (MCP). We discuss how Otobotto’s swarm-based approach addresses current research gaps and enterprise challenges, and we invite the community to contribute to this ambitious yet feasible vision for AI-driven autonomous software engineering.

## CCS Concepts

- Computing methodologies → Artificial intelligence → Knowledge representation and reasoning (I.2.4)  
- Computing methodologies → Artificial intelligence → Planning and scheduling (I.2.8)  
- Computing methodologies → Artificial intelligence → Multi-agent planning (I.2.11)  
- Computing methodologies → Multi-agent systems → Multi-agent architectures (I.2.11)  
- Computing methodologies → Distributed artificial intelligence → Multi-agent systems (I.2.11)  
- Software and its engineering → Software organization and properties → Software system structures → Microservices (D.2.11)  
- Software and its engineering → Software creation and management → Software development process management → Agile software development (D.2.9)  
- Software and its engineering → Software creation and management → Software development process management → Software development productivity (D.2.9)  
- Software and its engineering → Software creation and management → Software development techniques → Cloud computing (D.2.m)  
- Software and its engineering → Software creation and management → Software verification and validation → Software defect analysis (D.2.4)  
- Software and its engineering → Software creation and management → Software verification and validation → Software testing and debugging (D.2.5)  
- Software and its engineering → Software creation and management → Maintaining software (D.2.7)  
- Human-centered computing → Collaborative and social computing systems and tools (H.5.3)  
- Security and privacy → Software and application security → Software security engineering (D.4.6)  

## Keywords

Autonomous software development; AI swarm architecture; Multi-agent systems; Enterprise software engineering; Test-driven development; Git-native workflows; Human-in-the-loop AI; Software agent coordination; Memory hierarchy; Progressive autonomy; Large language models; Code generation
