import os
import json
from datetime import datetime
from typing import List, Dict, Any, Optional
from mempalace.layers import MemoryStack
from mempalace.searcher import search_memories

class MemPalaceClient:
    def __init__(self, data_path: str = "mempalace_data"):
        self.data_path = os.path.abspath(data_path)
        os.makedirs(self.data_path, exist_ok=True)
        self.stack = MemoryStack()

    def get_wake_up_context(self) -> str:
        try:
            return self.stack.wake_up()
        except Exception:
            return "No prior identity context found."

    def recall_topic(self, wing: str, room: str = None) -> str:
        try:
            return self.stack.recall(wing=wing, room=room)
        except Exception:
            return ""

    def get_status(self) -> Dict[str, Any]:
        try:
            return self.stack.status()
        except Exception:
            return {"status": "disconnected"}

# Tools to be used by Agno Agents
def mempalace_diary_write(agent_name: str, entry: str, topic: str = "general") -> Dict[str, Any]:
    """
    Writes an entry to an agent's personal diary for persistent memory across sessions.
    
    Args:
        agent_name: The name of the agent.
        entry: The diary entry content (recommended format: action|finding|impact).
        topic: The topic of the diary entry.
    """
    data_path = "mempalace_data"
    diary_path = os.path.join(data_path, f"{agent_name}_diary.md")
    os.makedirs(os.path.dirname(diary_path), exist_ok=True)
    
    timestamp = datetime.now().isoformat()
    with open(diary_path, "a") as f:
        f.write(f"\n## {topic} | {timestamp}\n{entry}\n")
    
    return {
        "success": True,
        "agent": agent_name,
        "topic": topic,
        "timestamp": timestamp
    }

def mempalace_search(query: str, wing: Optional[str] = None, room: Optional[str] = None) -> Dict[str, Any]:
    """
    Performs a semantic search within the palace to retrieve past experiences or knowledge.
    
    Args:
        query: The search query.
        wing: Optional filter for a specific wing (agent name).
        room: Optional filter for a specific room (topic).
    """
    data_path = "mempalace_data"
    try:
        results = search_memories(query, palace_path=data_path)
        # Filter manually if results doesn't handle wing/room well in mock
        filtered_results = results.get("results", [])
        if wing:
            filtered_results = [r for r in filtered_results if r.get("wing") == wing]
        if room:
            filtered_results = [r for r in filtered_results if r.get("room") == room]
            
        return {
            "query": query,
            "results": filtered_results[:5]
        }
    except Exception as e:
        return {"error": str(e), "results": []}
