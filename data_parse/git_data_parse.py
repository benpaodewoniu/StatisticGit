from config.config import git_command_type


def get_person_data(project, key, out, all_person_code_statis):
    person_data = {}
    try:
        msgs = out.split("\n")
        name = ""
        for msg in msgs:
            t_count = msg.count("\t")
            if t_count == 1:
                # 名字
                name = msg.split("\t")[0]
                person_data[name] = {
                    "add": 0,
                    "remove": 0,
                    "all": 0
                }
                if name not in all_person_code_statis.keys():
                    all_person_code_statis[name] = {}
                if project not in all_person_code_statis.get(name).keys():
                    all_person_code_statis[name][project] = {
                        "add": 0,
                        "remove": 0,
                        "all": 0,
                    }
            else:
                # 是上传文件
                if len(msg) == 0 or msg.split("\t")[0] == "-":
                    continue
                add = int(msg.split("\t")[0])
                remove = int(msg.split("\t")[1])
                person_data.get(name)["add"] = person_data.get(name).get("add") + add
                person_data.get(name)["remove"] = person_data.get(name).get("remove") + remove
                person_data.get(name)["all"] = person_data.get(name).get("add") + person_data.get(name).get("remove")
                all_person_code_statis.get(name).get(project)["add"] = all_person_code_statis.get(name).get(
                    project).get("add") + add
                all_person_code_statis.get(name).get(project)["remove"] = all_person_code_statis.get(name).get(
                    project).get("remove") + remove
                all_person_code_statis.get(name).get(project)["all"] = all_person_code_statis.get(name).get(
                    project).get("add") + all_person_code_statis.get(name).get(project).get("remove")
    except Exception as e:
        print(f"项目{project} 在 {git_command_type.get(key)} 中出现错误")
    finally:
        return person_data


def get_person_push_count(project, key, out, all_person_push_count):
    person_data = {}
    try:
        msgs = out.split("\n")
        name = ""
        for msg in msgs:
            t_count = msg.count("\t")
            if t_count == 1:
                # 名字
                name = msg.split("\t")[0]
                person_data[name] = 0

                if name not in all_person_push_count.keys():
                    all_person_push_count[name] = {}
                if project not in all_person_push_count.get(name).keys():
                    all_person_push_count[name][project] = 0
            else:
                # 是上传文件
                if len(msg) == 0:
                    continue
                count = int(msg.strip())
                person_data[name] = count
                all_person_push_count[name][project] = count
    except Exception as e:
        print(f"项目{project} 在 {git_command_type.get(key)} 中出现错误")
    finally:
        return person_data
