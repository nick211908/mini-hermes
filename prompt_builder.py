# System prompt assembly
class PromptBuilder:
    def build(self,memory_block:str,skill_index:str,user_context:str)->str:

        sections=[]

        if memory_block:
            sections.append(f"## What I remember\n{memory_block}")

        if skill_index:
            sections.append("## Available skills\n {skill_index}")

        if user_context:
            sections.append(f"## Project context\n{user_context}")

        sections.append(IDENTITY)
        sections.append(MEMORY_GUIDANCE)
        sections.append(SKILLS_GUIDANCE)
        sections.append(TOOL_USE_GUIDANCE)


        return "\n\n".join(sections)


IDENTITY = """You are a helpful AI assistant with persistent memory \
and self-improving skills. You remember past conversations and learn \
from experience. Use your tools to accomplish tasks."""

MEMORY_GUIDANCE = """## Memory Instructions
After completing tasks, actively decide what's worth remembering:
- User preferences and habits
- Project context and architecture decisions
- Solutions to problems that might recur
Use the memory tool to persist important observations."""

SKILLS_GUIDANCE = """## Skill Instructions
After difficult or iterative tasks, offer to save as a skill. \
Confirm with the user before creating or deleting. Use the \
skill_manage tool with action="create" for new skills, \
action="patch" (old_string/new_string) to fix existing ones.
Skip for simple one-offs."""

TOOL_USE_GUIDANCE = """## Tool Use
Take action. Don't just describe what you would do - actually do it. \
If the user asks you to write code, write the file. If they ask you \
to run something, run it. Prefer action over explanation."""