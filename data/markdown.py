import os

def merge_md_files_in_order(folder_path, file_order, output_file="README.md"):
    with open(output_file, "w", encoding="utf-8") as outfile:
        for filename in file_order:
            file_path = os.path.join(folder_path, filename)

            if not os.path.exists(file_path):
                print(f"警告：文件不存在，已跳过 -> {filename}")
                continue

            with open(file_path, "r", encoding="utf-8") as infile:
                outfile.write(infile.read())
    print(f"合并完成：{output_file}")

file_order = [
    "template1.md",
    "channel_change.md",
    "channels.md",
    "template2.md"
]

merge_md_files_in_order("data", file_order)