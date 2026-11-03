import os
import shutil


print("\n")
print("SECTION B - os MODULE, CUSTOM MODULES AND PACKAGES \n")

''' 1st question. '''
log_dir = os.path.join("store_data", "logs")

os.makedirs(log_dir, exist_ok=True)
print(f"Directory created/verified: {log_dir}")

os.makedirs(log_dir, exist_ok=True)
print(f"Directory verified again without error: {log_dir}")


''' 2nd question. '''

log_dir = os.path.join("store_data", "logs")
os.makedirs(log_dir, exist_ok=True)
os.makedirs(log_dir, exist_ok=True)

p_txt_path = os.path.join(log_dir, "p.txt")
with open(p_txt_path, "w", encoding="utf-8") as f:
    f.write("red\ngreen\n")

q_txt_path = os.path.join(log_dir, "q.txt")
with open(q_txt_path, "w", encoding="utf-8") as f:
    f.write("blue\n")

r_csv_path = os.path.join(log_dir, "r.csv")
with open(r_csv_path, "w", encoding="utf-8") as f:
    f.write("x,y\n1,2\n")
    
''' 3rd question. '''

log_dir = os.path.join("store_data", "logs")
os.makedirs(log_dir, exist_ok=True)
os.makedirs(log_dir, exist_ok=True)

p_txt_path = os.path.join(log_dir, "p.txt")
with open(p_txt_path, "w", encoding="utf-8") as f:
    f.write("red\ngreen\n")

q_txt_path = os.path.join(log_dir, "q.txt")
with open(q_txt_path, "w", encoding="utf-8") as f:
    f.write("blue\n")

r_csv_path = os.path.join(log_dir, "r.csv")
with open(r_csv_path, "w", encoding="utf-8") as f:
    f.write("x,y\n1,2\n")
    
txt_files = sorted([f for f in os.listdir(log_dir) if f.endswith(".txt")])
print(txt_files)


''' 4th question. '''

log_dir = os.path.join("store_data", "logs")
os.makedirs(log_dir, exist_ok=True)
os.makedirs(log_dir, exist_ok=True)

p_txt_path = os.path.join(log_dir, "p.txt")
with open(p_txt_path, "w", encoding="utf-8") as f:
    f.write("red\ngreen\n")

q_txt_path = os.path.join(log_dir, "q.txt")
with open(q_txt_path, "w", encoding="utf-8") as f:
    f.write("blue\n")

r_csv_path = os.path.join(log_dir, "r.csv")
with open(r_csv_path, "w", encoding="utf-8") as f:
    f.write("x,y\n1,2\n")

txt_files = sorted([f for f in os.listdir(log_dir) if f.endswith(".txt")])
print(txt_files)

with open(p_txt_path, "r", encoding="utf-8") as f:
    lines = f.readlines()
    first_line = lines[0].strip() if lines else ""
    print(len(lines), first_line)
    
''' 5th question. '''


log_dir = os.path.join("store_data", "logs")
os.makedirs(log_dir, exist_ok=True)
os.makedirs(log_dir, exist_ok=True)

p_txt_path = os.path.join(log_dir, "p.txt")
with open(p_txt_path, "w", encoding="utf-8") as f:
    f.write("red\ngreen\n")

q_txt_path = os.path.join(log_dir, "q.txt")
with open(q_txt_path, "w", encoding="utf-8") as f:
    f.write("blue\n")

r_csv_path = os.path.join(log_dir, "r.csv")
with open(r_csv_path, "w", encoding="utf-8") as f:
    f.write("x,y\n1,2\n")

txt_files = sorted([f for f in os.listdir(log_dir) if f.endswith(".txt")])
print(txt_files)

with open(p_txt_path, "r", encoding="utf-8") as f:
    lines = f.readlines()
    first_line = lines[0].strip() if lines else ""
    print(len(lines), first_line)

archive_dir = os.path.join("store_data", "archive")
os.makedirs(archive_dir, exist_ok=True)

shutil.move(p_txt_path, os.path.join(archive_dir, "p.txt"))

print(sorted(os.listdir(log_dir)), sorted(os.listdir(archive_dir)))

''' 6th question. '''

log_dir = os.path.join("store_data", "logs")
os.makedirs(log_dir, exist_ok=True)
os.makedirs(log_dir, exist_ok=True)

p_txt_path = os.path.join(log_dir, "p.txt")
with open(p_txt_path, "w", encoding="utf-8") as f:
    f.write("red\ngreen\n")

q_txt_path = os.path.join(log_dir, "q.txt")
with open(q_txt_path, "w", encoding="utf-8") as f:
    f.write("blue\n")

r_csv_path = os.path.join(log_dir, "r.csv")
with open(r_csv_path, "w", encoding="utf-8") as f:
    f.write("x,y\n1,2\n")

txt_files = sorted([f for f in os.listdir(log_dir) if f.endswith(".txt")])
print(txt_files)

with open(p_txt_path, "r", encoding="utf-8") as f:
    lines = f.readlines()
    first_line = lines[0].strip() if lines else ""
    print(len(lines), first_line)

archive_dir = os.path.join("store_data", "archive")
os.makedirs(archive_dir, exist_ok=True)

shutil.move(p_txt_path, os.path.join(archive_dir, "p.txt"))

print(sorted(os.listdir(log_dir)), sorted(os.listdir(archive_dir)))

old_q_txt_path = os.path.join(log_dir, "old_q.txt")
os.replace(q_txt_path, old_q_txt_path)

print(os.path.exists(q_txt_path), os.path.isfile(old_q_txt_path))

''' 7th question. '''

log_dir = os.path.join("store_data", "logs")
os.makedirs(log_dir, exist_ok=True)
os.makedirs(log_dir, exist_ok=True)

p_txt_path = os.path.join(log_dir, "p.txt")
with open(p_txt_path, "w", encoding="utf-8") as f:
    f.write("red\ngreen\n")

q_txt_path = os.path.join(log_dir, "q.txt")
with open(q_txt_path, "w", encoding="utf-8") as f:
    f.write("blue\n")

r_csv_path = os.path.join(log_dir, "r.csv")
with open(r_csv_path, "w", encoding="utf-8") as f:
    f.write("x,y\n1,2\n")

txt_files = sorted([f for f in os.listdir(log_dir) if f.endswith(".txt")])
print(txt_files)

with open(p_txt_path, "r", encoding="utf-8") as f:
    lines = f.readlines()
    first_line = lines[0].strip() if lines else ""
    print(len(lines), first_line)

archive_dir = os.path.join("store_data", "archive")
os.makedirs(archive_dir, exist_ok=True)

shutil.move(p_txt_path, os.path.join(archive_dir, "p.txt"))

print(sorted(os.listdir(log_dir)), sorted(os.listdir(archive_dir)))

old_q_txt_path = os.path.join(log_dir, "old_q.txt")
os.replace(q_txt_path, old_q_txt_path)

print(os.path.exists(q_txt_path), os.path.isfile(old_q_txt_path))

base_dir = "store_data"
shutil.rmtree(base_dir)

print(os.path.exists(base_dir))




print("\n")