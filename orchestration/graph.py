from langgraph.graph import StateGraph, END
from agents.planner_agent import PlannerAgent
from agents.rag_agent import RAGAgent
from agents.tool_agent import ToolAgent
from agents.synthesizer_agent import SynthesizerAgent

planner = PlannerAgent()
rag = RAGAgent()
tool = ToolAgent()
synth = SynthesizerAgent()

def planner_node(state):
    action = planner.plan(state["query"], state)
    state["next_action"] = action
    return state

def rag_node(state):
    docs, cites = rag.retrieve(state["query"])
    state["retrieved_docs"] = docs
    state["citations"] = cites
    return state

def tool_node(state):
    state["tool_output"] = tool.execute("calculator", "10+20")
    return state

def synth_node(state):
    context = "\n".join(state.get("retrieved_docs", []))
    state["final_answer"] = synth.synthesize(
        state["query"], context, state.get("tool_output")
    )
    return state

graph = StateGraph(dict)

graph.add_node("planner", planner_node)
graph.add_node("rag", rag_node)
graph.add_node("tool", tool_node)
graph.add_node("synth", synth_node)

graph.set_entry_point("planner")

graph.add_conditional_edges(
    "planner",
    lambda s: s["next_action"],
    {
        "retrieve": "rag",
        "tool": "tool",
        "synthesize": "synth"
    }
)

graph.add_edge("rag", "planner")
graph.add_edge("tool", "synth")
graph.add_edge("synth", END)

app = graph.compile()
