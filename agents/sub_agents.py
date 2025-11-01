from agents.tools import *
from agents.prompts import *


research_sub_agent = {
    "name": "research-agent",
    "description": "Used to research more in depth questions. Only give this researcher one topic at a time. Do not pass multiple sub questions to this researcher. Instead, you should break down a large topic into the necessary components, and then call multiple research agents in parallel, one for each sub question.",
    "system_prompt": SUB_RESEARCH_PROMPT,
    "tools": [internet_search, arxiv_search],
}


critique_sub_agent = {
    "name": "critique-agent",
    "description": "Used to critique the final report. Give this agent some information about how you want it to critique the report.",
    "system_prompt": SUB_CRITIQUE_PROMPT,
    "tools": [create_markdown_file]
}
