
# SYSTEM_PROMPT = '''According to the user query, expand and solidify the query into a step by step detailed instruction (or comment) on how to write python code to fulfill the user query's requirements. Import the appropriate libraries. Pinpoint the correct library functions to call and set each parameter in every function call accordingly.'''

# EXPERT_USER_PROMPT = '''Here is the user query: [User Query]:
# """
# {{query}}
# """
# You should understand what the query's requirements are, and output step by step, detailed instructions on how to use python code to fulfill these requirements. Include what libraries to import, what library functions to call, how to set the parameters in each function correctly, how to prepare the data, how to manipulate the data so that it becomes appropriate for later functions to call etc,. Make sure the code to be executable and correctly generate the desired output in the user query. 
#  '''

SYSTEM_PROMPT = '''Based on the user's query, expand and clarify it into a series of high - level instructions to guide how to write Python code to meet the requirements of the user's query. Only summarize the core steps and do not need to elaborate on specific library function calls and parameter settings.'''

EXPERT_USER_PROMPT = '''Here is the user's query: [User Query]:
"""
{{query}}
"""
You need to understand the requirements of the query and output a series of high - level instructions on how to use Python code to meet these requirements. Focus on clarifying the core steps to ensure that the code can correctly generate the output expected in the user's query.
 ''' 


EXPERT_USER_PROMPT_CSV = '''Here is the user's query: [User Query]:
"""
{{query}}
"""
Here is the structure of the CSV file:
"""
{{csv_structure}}
"""
You need to understand the requirements of the query and output a series of high - level instructions on how to use Python code to meet these requirements. Focus on clarifying the core steps to ensure that the code can correctly generate the output expected in the user's query.
 ''' 