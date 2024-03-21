# 目录结构: 按照分类建立文件夹
#          |--- 身份证
# images---|--- 银行卡
#          |--- 合同
#
# 1. 便利images文件夹下所有的文件夹
# 2. 每个文件夹的名称就是分类的名称
# 3. 遍历每个分类文件夹下的所有图片，组装成 label studio Object Detection with Bounding Boxes 所导出的json
#
import json
import os
import shutil
import uuid
from generate_random import generate_random_id, generate_number


def _generate_document_cls_json(case_id, annotation_id, result_id, cls_name, img_name):
    project = 39
    user_id = 22

    _id = case_id
    _annotation_id = annotation_id
    _result_id = result_id

    _img = f"/data/upload/{project}/{img_name}"

    template = \
        {
            "id": _id,
            "annotations": [{
                "id": _annotation_id,
                "completed_by": user_id,
                "result": [{
                    "value": {
                        "choices": [cls_name]
                    },
                    "id": _result_id,
                    "from_name": "choice",
                    "to_name": "image",
                    "type": "choices",
                    "origin": "manual"
                }],
                "was_cancelled": False,
                "ground_truth": False,
                "created_at": "2024-01-22T08:30:48.884113Z",
                "updated_at": "2024-01-22T08:30:48.884113Z",
                "draft_created_at": None,
                "lead_time": 3.021,
                "prediction": {},
                "result_count": 0,
                "unique_id": str(uuid.uuid4()),
                "import_id": None,
                "last_action": None,
                "task": _id,
                "project": project,
                "updated_by": user_id,
                "parent_prediction": None,
                "parent_annotation": None,
                "last_created_by": None
            }],
            "file_upload": img_name,
            "drafts": [],
            "predictions": [],
            "data": {
                "image": _img
            },
            "meta": {},
            "created_at": "2024-01-22T08:15:36.957253Z",
            "updated_at": "2024-01-22T08:30:48.937112Z",
            "inner_id": 1,
            "total_annotations": 1,
            "cancelled_annotations": 0,
            "total_predictions": 0,
            "comment_count": 0,
            "unresolved_comment_count": 0,
            "last_comment_updated_at": None,
            "project": project,
            "updated_by": user_id,
            "comment_authors": []
        }
    return template


def generate_document_cls_train(base_path, save_path):
    """
    生成文档分类json数据
    """
    train_dir = os.path.join(save_path, 'train', 'images')
    os.makedirs(train_dir, exist_ok=True)
    # 遍历目标目录
    directories = [name for name in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, name))]

    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg']  # Common image file extensions
    image_files = {}

    for directory in directories:
        dir_path = os.path.join(base_path, directory)
        for file in os.listdir(dir_path):
            if os.path.isfile(os.path.join(dir_path, file)) and any(file.endswith(ext) for ext in image_extensions):
                # copy文件
                shutil.copy(os.path.join(dir_path, file), os.path.join(train_dir, file))
                if directory not in image_files:
                    image_files[directory] = []
                image_files[directory].append(file)

    number_id_generator = generate_number(start_num=50000)
    annotation_id_generator = generate_number(start_num=20000)

    result = []
    for directory, files in image_files.items():
        print(f"Directory: {directory}")
        for file in files:
            print(f" - File: {file}")
            number_id = next(number_id_generator)
            annotation_id = next(annotation_id_generator)
            result_id = generate_random_id()
            result.append(_generate_document_cls_json(number_id, annotation_id, result_id, directory, file))

    write_json = json.dumps(result, ensure_ascii=False)

    with open(os.path.join(save_path, 'train', 'label_studio.json'), 'w', encoding='utf-8') as file:
        file.write(write_json)

    _train_path = os.path.join(save_path, 'train')
    print(f'label studio 分类训练文件创建成功, 训练文件在 {_train_path} 目录下')


if __name__ == '__main__':
    _base_path = r'C:\Users\Desktop\大分类\未标注'
    _save_path = r'C:\Users\Desktop\大分类'
    generate_document_cls_train(_base_path, _save_path)
