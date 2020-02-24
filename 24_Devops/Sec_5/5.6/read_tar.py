import tarfile
with tarfile.open('python.tar') as f:
    for member_info in f.getmembers():
        print(member_info)
    print("="*50)
    for i in f.getnames():
        print(i)
    print("=" * 50)
    print(f.extract('etc/ssh/ssh_config'))