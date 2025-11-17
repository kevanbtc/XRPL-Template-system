from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Message:
    sender: str
    payload: Dict[str, Any]


class Agent:
    name: str = "agent"

    def step(self, state: Dict[str, Any]) -> Optional[Message]:
        raise NotImplementedError


class Orchestrator:
    def __init__(self, agents: List[Agent]) -> None:
        self.agents = agents

    def run(self, state: Optional[Dict[str, Any]] = None, max_rounds: int = 8) -> Dict[str, Any]:
        if state is None:
            state = {}
        rounds = 0
        while rounds < max_rounds:
            rounds += 1
            progressed = False
            for agent in self.agents:
                msg = agent.step(state)
                if msg is not None:
                    state.setdefault("log", []).append(msg)
                    progressed = True
            if not progressed:
                break
        state["rounds"] = rounds
        return state
