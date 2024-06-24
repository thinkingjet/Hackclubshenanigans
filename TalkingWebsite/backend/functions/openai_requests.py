import  os
from functions.database import get_recent_messages

# TODO: The 'openai.organization' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(organization=os.getenv("OPEN_AI_ORG"))'
