git_paths = {
    "gen_gps": "https://gitee.com/haee/gen_gps.git",
    "gen": "https://gitee.com/haee/gen_gps.git",
    "pose_dance": "https://gitee.com/haee/pose-your-dance.git",
}

dir_path = "./git/"

start_time = ""
end_time = ""

git_command = {
    "person_code_line": """git log --format='%aN' | sort -u | while read name; do echo "$name\t"; git log  --author="$name" --pretty=tformat: --numstat ; done""",
    "person_push_count": """git log --format='%aN' | sort -u | while read name; do echo "$name\t,"; git log --author="$name" --oneline | wc -l; done"""
}

git_command_type = {
    "person_code_line": "个人代码统计",
    "person_push_count": "个人提交次数"
}

statis_font = {
    "add": "增加 ",
    "remove": "减少 ",
    "all": "全部 "
}
