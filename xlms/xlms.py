import xlwt


def get_xls(all_project_code_statis, all_project_push_count, all_person_code_statis, all_person_push_count):
    style = xlwt.XFStyle()  # 创建一个样式对象，初始化样式
    al = xlwt.Alignment()
    al.horz = 0x02  # 设置水平居中
    al.vert = 0x01  # 设置垂直居中
    style.alignment = al

    workbook = xlwt.Workbook()
    get_sheet_5(workbook, "项目代码统计", ["项目", "人员", "增加", "减少", "全部"], all_project_code_statis, style)
    get_sheet_3(workbook, "项目提交统计", ["项目", "人员", "提交次数"], all_project_push_count, style)
    get_sheet_5(workbook, "个人代码统计", ["人员", "项目", "增加", "减少", "全部"], all_person_code_statis, style)
    get_sheet_3(workbook, "个人提交统计", ["人员", "项目", "提交次数"], all_person_push_count, style)
    workbook.save("./test.xls")


def get_sheet_5(workbook, sheet_name, sheet_head, sheet_data: dict, style):
    worksheet = workbook.add_sheet(sheet_name)
    for index, value in enumerate(sheet_head):
        worksheet.col(index).width = 256 * 40
        worksheet.write(0, index, value, style)

    index = 1
    project_index = 1
    for project, project_infos in sheet_data.items():
        for person, infos in project_infos.items():
            worksheet.write(index, 1, person, style)
            worksheet.write(index, 2, infos.get("add"), style)
            worksheet.write(index, 3, infos.get("remove"), style)
            worksheet.write(index, 4, infos.get("all"), style)
            index += 1

        worksheet.write_merge(project_index, index - 1, 0, 0, project, style)
        project_index = index


def get_sheet_3(workbook, sheet_name, sheet_head, sheet_data: dict, style):
    worksheet = workbook.add_sheet(sheet_name)
    for index, value in enumerate(sheet_head):
        worksheet.col(index).width = 256 * 40
        worksheet.write(0, index, value, style)

    index = 1
    project_index = 1
    for project, project_infos in sheet_data.items():
        for person, info in project_infos.items():
            worksheet.write(index, 1, person, style)
            worksheet.write(index, 2, info, style)
            index += 1
        worksheet.write_merge(project_index, index - 1, 0, 0, project, style)
        project_index = index
