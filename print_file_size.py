import os

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size

def main():
    start_path = f"D:\\Coding\\NFT\\HashLipsTutorial\\hashlips_art_engine-1.0.6_update\\build-saved\\"
    for dirpath, dirnames, filenames in os.walk(start_path):
        print(f'{dirpath}: {get_size(dirpath)} bytes')

if __name__ == '__main__':
    main()