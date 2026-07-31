# MEMORY.md / USER.md management
from pathlib import Path


class PersistentMemory:
    MEMORY_LIMIT = 2200   # Hermes default for observations
    USER_LIMIT = 1375
    def __init__(self, data_dir:Path):

        self.meomory_path = data_dir/ "Memory.md"
        self.user_path = data_dir/ "User.md"
        self.meomory_path.touch(exist_ok=True)
        self.user_path.touch(exist_ok=True)

    def save_observation(self , text:str)->str:
        current = self.meomory_path.read_text()
        new_entry = f"\n- {text}"

        if len(current) + len(new_entry) > self.MEMORY_LIMIT:
            lines = current.strip().split("\n")
            while lines and len("\n".join(lines)) + len(new_entry) > self.MEMORY_LIMIT:
                lines.pop(0)
            current = "\n".join(lines)
        self.memory_path.write_text(current + new_entry)
        return f"Saved to memory: {text[:80]}"


    def load(self)->str:
        parts = []

        user = self.user_path.read_text().strip()

        memory = self.meomory_path.read_text().strip()

        if user:
            parts.append(f"## User Profile\n{user}")

        if memory:
            parts.append(f"## Observation\n{memory}")

        return "\n\n".join(parts)

    def update_user_profile(self,text : str)->str:
        self.user_path.write_text(text[:self.USER_LIMIT])
        return f"User profile updated ({len(text)} chars)"

    def read_memory(self)->str:
        return self.meomory_path.read_text().strip()

    def read_user(self)->str:
        return self.user_path.read_text().strip()


    



    