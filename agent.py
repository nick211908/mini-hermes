from openai import OpenAI
from tool_call import strategy_for_model

class Agent:

    def __init__(self,client,model,system_prompt,tools,tool_handler):
        self.client = client
        self.model = model
        self.tools=tools
        self.tool_handler=tool_handler
        self._strategy = strategy_for_model(model)
        self.msg=[{"role":"system","content":system_prompt}]


        def run(self,user_input):
            self.msg.append({"role":"user","content":user_input})
            max_iteration=15

            for _ in range(max_iteration+1):
                response=self._call_llm()

                message = response.choices[0].message.content

                content,tool_calls = self._strategy.parse_response(response)

                assitant_msg = self._strategy.build_assistant_msg(content,tool_calls)

                self.msg.append(assitant_msg)

                if not tool_calls:
                    return content

                for tc in tool_calls:
                    result = self._execute_tool(tc.name,tc.args)

                    result_msg = self._strategy.build_tool_result_msg(tc, result)
                    self.messages.append(result_msg)
            return f"{max_iteration} Reached. Task could not be accomplished"
        def _call_llm(self):
            kwargs={"model":self.model,"messages":self.msg,"max_tokens":4096}

            kwargs = self._strategy.prepare_kwargs(kwargs,self.tools)

            return self.client.chat.completions.create(**kwargs)

        def _execute_tool(self,name:str,args:dict)->str:

            handler=self.tool_handler.get(name)

            if not handler:
                return f"Unkwnon Tool Name {name}"

            try:

                result = handler(**args)

                return str(result)[:50000]
            except Exception as e:
                return f"Error executing tool {name}: {str(e)}"