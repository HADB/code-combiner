import os
import sys
import getopt

CURRENT_PATH = os.getcwd()  # 当前目录


def run(project_path):
    g = os.walk(project_path)
    with open(os.path.join(CURRENT_PATH, "output.txt"), "w", encoding="utf-8") as file_write:
        for path, _, file_list in g:
            if "node_modules" in path or "dist" in path:
                continue
            sub_path = path[len(project_path) + 1 :]
            for file_name in file_list:
                extension = os.path.splitext(file_name)[-1]
                if extension in [
                    ".js",
                    ".jsx",
                    ".ts",
                    ".tsx",
                    ".vue",
                    ".css",
                    ".less",
                    ".scss",
                    ".java",
                    ".m",
                    ".h",
                    ".py",
                    ".json",
                    ".xml",
                    ".kt",
                ]:
                    print(os.path.join(sub_path, file_name))
                    with open(os.path.join(path, file_name), "r", encoding="utf-8") as file_read:
                        content = file_read.read()
                        file_write.write(f"File: {os.path.join(sub_path, file_name)}\n\n{content}\n\n\n")


if __name__ == "__main__":
    OPTS, ARGS = getopt.getopt(
        sys.argv[1:],
        "",
        [
            "path=",
        ],
    )
    for name, value in OPTS:
        if name == "--path":
            project_path = value
    print(project_path)
    if os.path.exists(project_path):
        run(project_path)
    else:
        print("项目目录不存在")
