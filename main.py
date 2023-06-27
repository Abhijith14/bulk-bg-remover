from pathlib import Path
from rembg import remove, new_session

session = new_session()

for file in Path('input').glob('*.jpg'):
    input_path = str(file)
    output_path = str(file.parent / (file.stem + ".out.png"))

    with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            input = i.read()
            print(input)
            output = remove(input, session=session)
            o.write(output)
