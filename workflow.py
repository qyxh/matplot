import argparse
import json
import re

from tqdm import tqdm
from agents.query_expansion_agent import QueryExpansionAgent
from agents.plot_agent import PlotAgent
from agents.visual_refine_agent import VisualRefineAgent
import logging
import os
import shutil
import glob
import sys
from agents.utils import is_run_code_success, run_code, get_code,csv_to_json
parser = argparse.ArgumentParser()
parser.add_argument('--workspace', type=str, default='./workspace')
parser.add_argument('--model_type', type=str, default='deepseek-reasoner')
parser.add_argument('--visual_refine', type =bool, default=True)
args = parser.parse_args()

def mainworkflow(expert_instruction, simple_instruction, workspace, json_csv='', max_try=3):
    # Query expanding
    logging.info('=========Query Expansion AGENT=========')  
    config = {'workspace': workspace}
    query_expansion_agent = QueryExpansionAgent(expert_instruction, simple_instruction,model_type=args.model_type,json_csv=json_csv)
    expanded_simple_instruction = query_expansion_agent.run('simple')
    logging.info('=========Expanded Simple Instruction=========')
    logging.info(expanded_simple_instruction)
    logging.info('=========Plotting=========')

    # GPT-4 Plot Agent
    # Initial plotting
    action_agent = PlotAgent(config, simple_instruction, expanded_simple_instruction)
    logging.info('=========Novice 4 Plotting=========')
    novice_log, novice_code = action_agent.run_initial(args.model_type, 'novice.png')
    logging.info(novice_log)
    logging.info('=========Original Code=========')
    logging.info(novice_code)

    if args.visual_refine and os.path.exists(f'{workspace}/novice.png'):
        print('Use original code for visual feedback ')
        visual_refine_agent = VisualRefineAgent('novice.png', config, '', simple_instruction)
        visual_feedback = visual_refine_agent.run('gpt-4', 'novice', 'novice_final.png')
        logging.info('=========Visual Feedback=========')
        logging.info(visual_feedback)
        logging.info('================================================================================================================================')
        final_instruction = '' + '\n\n' + visual_feedback
        
        action_agent = PlotAgent(config, simple_instruction, final_instruction,novice_code)
        novice_log, novice_code = action_agent.run_vis(args.model_type, 'novice_final.png')
        logging.info(novice_log)


def check_refined_code_executable(refined_code, model_type, query_type, workspace):
    file_name = f'code_action_{model_type}_{query_type}_refined.py'
    with open(os.path.join(workspace, file_name), 'w',encoding='utf-8') as f1:
        f1.write(refined_code)
    log = run_code(workspace, file_name)

    return is_run_code_success(log)


if __name__ == "__main__":

    workspace_base = args.workspace
    data_path = 'D:/MatPlotAgent-main/benchmark_data'
    # open the json file 
    data = json.load(open(f'{data_path}/benchmark_instructions.json'))
    
    for item in tqdm(data):
        novice_instruction = item['simple_instruction']
        expert_instruction = item['expert_instruction']
        example_id = item['id']
        directory_path = f'{workspace_base}/example_{example_id}'

        # Check if the directory already exists
        if not os.path.exists(directory_path):
            # If it doesn't exist, create the directory
            os.mkdir(directory_path)
            print(f"Directory '{directory_path}' created successfully.")
            input_path = f'{data_path}/data/{example_id}'
            json_csv = ''
            if os.path.exists(input_path):
                #全部copy到f"Directory '{directory_path}'
                # os.system(f'cp -r {input_path}/* {directory_path}')
                os.system(f'xcopy "{input_path}\\*" "{directory_path}" /e /i')
            # 确保 input_path 是目录且存在
                if os.path.isdir(input_path):
                    for filename in os.listdir(input_path):
                        print(f"当前文件: {filename}")
                        if filename.endswith(".csv"):
                            # 正确拼接路径
                            file_path = os.path.join(input_path, filename)
                            file_path = file_path.replace('\\','/')
                            print(f"完整路径: {file_path}")
                            
                            try:
                                # 假设 csv_to_json 返回字符串，累加到 json_csv
                                json_csv += csv_to_json(file_path)+'\n'
                            except Exception as e:
                                print(f"处理文件 {file_path} 时出错: {e}")
            else:
                print(f"路径 {input_path} 不是目录或不存在")
                json_csv = file_path.read()
        
                # json_csv = csv_to_json(input_path+'/data.csv')
        else:
            print(f"Directory '{directory_path}' already exists.")
            continue
        logging.basicConfig(level=logging.INFO, filename=f'{directory_path}/workflow.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        mainworkflow(expert_instruction, novice_instruction, workspace=directory_path, json_csv=json_csv)
