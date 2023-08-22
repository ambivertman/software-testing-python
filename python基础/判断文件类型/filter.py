def pic_filter(filepath):
    with open(filepath, 'rb', ) as f:
        content = f.read(8)
    if content == b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a':
        filepath = filepath + '.png'
    else:
        filepath = filepath + '.jpg'

    return filepath
