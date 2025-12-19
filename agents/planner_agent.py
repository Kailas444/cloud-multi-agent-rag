# Planner Agent (ReAct Controller)

class PlannerAgent:
    def plan(self, query, state):
        """
        Decide next action based on query and current state
        """
        if not state.get("retrieved_docs"):
            return "retrieve"
        if "calculate" in query.lower():
            return "tool"
        return "synthesize"
