flowchart TD
    subgraph Strategic_Layer["Strategic Layer"]
        Vision["Project Vision/Mission"]
        Objectives["Strategic Objectives"]
        Epics["Epics/Features"]
    end
    
    subgraph Tactical_Layer["Tactical Layer"]
        Stories["User Stories/Requirements"]
        Milestones["Milestones"]
    end
    
    subgraph Implementation_Layer["Implementation Layer"]
        Tasks["Tasks"]
        Subtasks["Subtasks"]
        Tests["Test Cases"]
    end
    
    subgraph Execution_Environment["Execution Environment"]
        Agents["Agent Network"]
        Memory["Memory Systems"]
        Knowledge["Knowledge Base"]
        VersionControl["Git Integration"]
    end
    
    Vision --> Objectives
    Objectives --> Epics
    Epics --> Stories
    Stories --> Tasks
    Tasks --> Subtasks
    Stories --> Tests
    
    Agents <--> Memory
    Agents <--> Knowledge
    Agents <--> VersionControl
    
    Tasks <--> Agents
    Tests <--> Agents
    
    subgraph Human_Integration["Human Integration"]
        HITL["Human-in-the-Loop"]
    end
    
    HITL <--> Agents
    HITL <--> Milestones
    HITL <--> Objectives