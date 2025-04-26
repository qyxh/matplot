# INITIAL_SYSTEM_PROMPT = '''You are a cutting-edge super capable code generation LLM. You will be given a natural language query, generate a runnable python code to satisfy all the requirements in the query. You can use any python library you want. When you complete a plot, remember to save it to a png file.
# '''

# INITIAL_USER_PROMPT = '''Here is the original query:
# """
# {{original_query}}
# """

# Here is the expansive query:
# """
# {{expansive_query}}
# """

# If the query requires data manipulation from a csv file, process the data from the csv file and draw the plot in one piece of code.

# Once the runnable python code is generated, you must check that the runnable python code matches original query and expansive query.If the code doesn't satisfy all the requirements in the query, you must rebuild the code until it exactly matches all the requirements in the query

# When you complete a plot, remember to save it to a png file. The file name should be """{{file_name}}""".
# '''

INITIAL_SYSTEM_PROMPT = '''You are a cutting-edge super capable code generation LLM. Given a natural language query, generate a runnable Python code to meet all its requirements. You can use any Python library. When creating a plot, save it as an image file. By default, save it as a .png file, but if the query specifies a different format (e.g., .jpg, .pdf), use that format.

To check if the generated code matches the query, ensure that all the data processing, plot elements, and output requirements described in the query are correctly implemented in the code. For example, if the query asks for a specific line style or legend label, the code should reflect that. In case of a conflict between the original query and the expansive query, always follow the original query.
'''

INITIAL_USER_PROMPT = '''
### Original Query
"""
{{original_query}}
"""

### Expansive Query
"""
{{expansive_query}}
"""

If the query involves data manipulation from a CSV file, write a single piece of code to process the data and create the plot.

Generate the runnable Python code and check if it meets both the original and expansive queries. In case of a conflict between the two, prioritize the original query. If the code doesn't fully satisfy the requirements, rebuild the code until it meets all the requirements of the original query and non - conflicting parts of the expansive query.

Save the plot as an image file. The file name should be "{{file_name}}". If the query specifies a file format other than .png, use that format.

'''

INITIAL_USER_PROMPT_CSV = '''
### Original Query
"""
{{original_query}}
"""
### Expansive Query
"""
{{expansive_query}}
"""
###Here is the structure of the CSV file:
"""
{{csv_structure}}
"""

If the query involves data manipulation from a CSV file, write a single piece of code to process the data and create the plot.

Generate the runnable Python code and check if it meets both the original and expansive queries. In case of a conflict between the two, prioritize the original query. If the code doesn't fully satisfy the requirements, rebuild the code until it meets all the requirements of the original query and non - conflicting parts of the expansive query.

Save the plot as an image file. The file name should be "{{file_name}}". If the query specifies a file format other than .png, use that format.

'''



VIS_SYSTEM_PROMPT = '''You are a cutting-edge super capable code generation LLM. Given an original query, an existing piece of code, and natural language instructions on how to improve the code, generate a runnable Python code that meets all the instruction requirements while preserving the original code's functionality. You can use any Python library. When creating a plot, save it as an image file. By default, save it as a .png file, but if the query specifies a different format (e.g., .jpg, .pdf), use that format.
To check if the generated code matches the query and instructions, ensure that all the new requirements in the instructions are added to the code without breaking the original functionality described in the query. In case of a conflict between the original query and the natural language instruction, follow the original query.
'''

VIS_USER_PROMPT = '''Here is the original query:
"""
{{original_query}}
"""
Here is natural language instruction:
"""
{{instruction}}
"""
Here is the code:
"""
{{code}}
"""
Generate a runnable Python code that meets both the original query and the natural language instruction. In case of a conflict between them, prioritize the original query. Check if the code matches these requirements. If not, rebuild the code until it meets all the requirements of the original query and non - conflicting parts of the instruction.
Save the plot as an image file. The file name should be "{{file_name}}". If the query specifies a file format other than .png, use that format.

'''

VIS_USER_PROMPT_CSV = '''Here is the original query:
"""
{{original_query}}
"""
Here is natural language instruction:
"""
{{instruction}}
"""
Here is the code:
"""
{{code}}
"""
Here is the structure of the CSV file:
"""
{{csv_structure}}
"""
Generate a runnable Python code that meets both the original query and the natural language instruction. In case of a conflict between them, prioritize the original query. Check if the code matches these requirements. If not, rebuild the code until it meets all the requirements of the original query and non - conflicting parts of the instruction.
Save the plot as an image file. The file name should be "{{file_name}}". If the query specifies a file format other than .png, use that format.

'''


ERROR_PROMPT = '''There are some errors in the code you gave:
{{error_message}}
please correct the errors.
Then give the complete code and don't omit anything even though you have given it in the above code.'''

ZERO_SHOT_COT_PROMPT = '''
Here is the query:
"""
{{query}}
"""

Let's think step by step when you complete the query.

When you complete a plot, remember to save it to a png file. The file name should be """{{file_name}}"""'''