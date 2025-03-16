flowchart LR
    subgraph SingleAgent["Traditional Single-Agent Approach"]
        direction TB
        SA[AI Agent]
        SA -->|Step 1| SA1[Planning]
        SA1 -->|Step 2| SA2[Coding]
        SA2 -->|Step 3| SA3[Testing]
        SA3 -->|Step 4| SA4[Documentation]
        SA4 -->|If issues| SA2
    end
    
    subgraph OtobottoSwarm["Otobotto Swarm Approach"]
        direction TB
        subgraph Agents["Specialized Agents"]
            A1[Planning Agent]
            A2[Coding Agent]
            A3[Testing Agent]
            A4[Documentation Agent]
        end
        subgraph SharedContext["Shared Context"]
            SC[(Memory & Knowledge)]
        end
        A1 <-->|"Concurrent<br>Communication"| A2
        A1 <-->|"Concurrent<br>Communication"| A3
        A1 <-->|"Concurrent<br>Communication"| A4
        A2 <-->|"Concurrent<br>Communication"| A3
        A2 <-->|"Concurrent<br>Communication"| A4
        A3 <-->|"Concurrent<br>Communication"| A4
        
        A1 <--> SC
        A2 <--> SC
        A3 <--> SC
        A4 <--> SC
    end
    
    classDef agentNode fill:#f9f,stroke:#333,stroke-width:1px;
    class A1,A2,A3,A4 agentNode;