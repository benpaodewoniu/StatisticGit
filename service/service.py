import re
import subprocess

from config.config import git_paths, git_command, git_command_type, dir_path
from data_parse.git_data_parse import get_person_data, get_person_push_count
from xlms.xlms import get_xls


def clone_update_git():
    for project, git_path in git_paths.items():
        git_dir_path = dir_path + project
        f = subprocess.Popen(
            f"git clone {git_path} {git_dir_path}",
            text=True,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        out, err = f.communicate()
        if f.returncode:
            print(f"项目{project}  clone 出现错误")
        else:
            print(f"项目{project}  clone 成功")
        print(f"\t开始初始化全部分支")
        f = subprocess.Popen(
            """for b in `git branch -r | grep -v -- '->'`; do git branch --track ${b##origin/} $b; done""",
            text=True,
            shell=True,
            cwd=git_dir_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        out, err = f.communicate()
        if f.returncode:
            # print(f"项目{project}  clone 全部分支 出现错误 {err}")
            pass
        else:
            print(f"\t初始化全部分支 成功")

        f = subprocess.Popen(
            """git fetch --all""",
            text=True,
            shell=True,
            cwd=git_dir_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        out, err = f.communicate()
        if f.returncode:
            print(f"\tfetch 全部分支 出现错误 {err}")
            pass
        else:
            print(f"\tfetch 全部分支 成功")

        f = subprocess.Popen(
            """git pull --all""",
            text=True,
            shell=True,
            cwd=git_dir_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        out, err = f.communicate()
        if f.returncode:
            print(f"\tpull 全部分支 出现错误 {err}")
            pass
        else:
            print(f"\tpull 全部分支 成功")


def statis_data():
    all_project_code_statis = {}
    all_project_push_count = {}
    all_person_code_statis = {}
    all_person_push_count = {}

    for project, git_path in git_paths.items():
        print(f"统计项目 {project}")
        project_path = dir_path + project
        branches = get_all_branch(project_path)
        for branch in branches:
            print(f"\t开始切换分支\t{branch}")

            f = subprocess.Popen(
                f"git checkout {branch}",
                text=True,
                shell=True,
                cwd=project_path,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
            out, err = f.communicate()
            if f.returncode:
                print(f"\t切换分支错误 {err}")
                pass
            else:
                print(f"\t切换分支 成功")

            keys = ["person_code_line", "person_push_count"]
            for key in keys:
                print(f"\t开始统计 {git_command_type.get(key)}")
                f = subprocess.Popen(
                    git_command.get(key),
                    text=True,
                    shell=True,
                    cwd=project_path,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE)
                out, err = f.communicate()
                if f.returncode:
                    print(f"\t项目{project} 在 {git_command_type.get(key)} 中出现错误")
                else:
                    if key == "person_code_line":
                        data = get_person_data(project, key, out, all_person_code_statis)
                        all_project_code_statis[project] = data
                    elif key == "person_push_count":
                        data = get_person_push_count(project, key, out, all_person_push_count)
                        all_project_push_count[project] = data
    # 排列 dict
    # sort_dict(all_project_code_statis)
    get_xls(all_project_code_statis, all_project_push_count, all_person_code_statis, all_person_push_count)
    print("生成 xls 成功")


def get_all_branch(project_path):
    f = subprocess.Popen(
        f"git branch --all",
        text=True,
        shell=True,
        cwd=project_path,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    out, err = f.communicate()
    branch_list = []
    if f.returncode:
        print(f"\t获取全部分支 错误")
    else:
        print(f"\t获取全部分支 成功")
        branches = out.split("\n")
        for branch in branches:
            if "/" not in branch and len(branch) > 0:
                branch_name = re.split(r'\s+', branch)[1].strip()
                branch_list.append(branch_name)
    return branch_list
