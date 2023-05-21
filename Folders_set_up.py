import os, sys, shutil


def create_dataset_directories(base_dir: str) -> None:
    print("Start creation of dataset directories...")

    if not os.path.exists(base_dir):
        os.mkdir(base_dir)

    directories = ["train", "validation", "test"]
    for directory in directories:
        sub_dir = os.path.join(base_dir, directory)
        os.mkdir(sub_dir)
        os.mkdir(os.path.join(sub_dir, "cats"))
        os.mkdir(os.path.join(sub_dir, "dogs"))

    print("Done")


def copy_data(
    src: str, dst: str, example_name: str, start: int, end: int
) -> None:
    fnames = [f"{example_name}.{i}.jpg" for i in range(start, end)]
    print("Copying...")
    for fname in fnames:
        print(f"Copying {fname} to {dst}")
        shutil.copyfile(
            os.path.join(src, fname),
            os.path.join(dst, fname)
        )


def main(argv):
    if len(argv) != 3:
        print("Bad arguments")
        sys.exit(-1)

    src, dst = argv[1], argv[2]

    create_dataset_directories(dst)

    copy_data(src, f"{dst}/train/cats/", "cat", 0, 1000)
    copy_data(src, f"{dst}/train/dogs/", "dog", 0, 1000)

    copy_data(src, f"{dst}/validation/cats/", "cat", 1000, 1500)
    copy_data(src, f"{dst}/validation/dogs/", "dog", 1000, 1500)

    copy_data(src, f"{dst}/test/cats/", "cat", 1500, 2000)
    copy_data(src, f"{dst}/test/dogs/", "dog", 1500, 2000)


if __name__ == "__main__":
    main(sys.argv)