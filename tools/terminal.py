# Shell command execution
import subprocess
from tool_registry import registry


def run_terminal(command: str, timeout: int = 30) -> str:
    """Execute a shell command and return stdout + stderr."""
    try:
        result = subprocess.run(
            command, shell=True, capture_output=True,
            text=True, timeout=timeout
        )
        output = result.stdout + result.stderr
        return output.strip() or "(no output)"
    except subprocess.TimeoutExpired:
        return "Error: command timed out"


registry.register(
    name="terminal",
    description="Execute a shell command and return stdout + stderr.",
    parameters={
        "type": "object",
        "properties": {
            "command": {"type": "string", "description": "Shell command to execute"},
            "timeout": {"type": "integer", "description": "Timeout in seconds", "default": 30}
        },
        "required": ["command"],
    },
    handler=run_terminal,
    category="execution",
)