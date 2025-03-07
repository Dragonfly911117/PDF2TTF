### PDF2TTF
> [!WARNING]
> This project is a WIP project, see [progress](https://github.com/Dragonfly911117/PDF2TTF/Progress) section for stuffs that is safe to use.

#### Brief
This is a mixture project of [01-2_crop_paper](https://github.com/Garvin2009/01-2_crop_paper) and [PngToTTF](https://github.com/chiaoooo/PngToTTF).

#### Prerequirements
- Python: 3.8+
- NodeJS: TODO: Find out what version is needed
- Poppler: Remember to add this to PATH if ur on Winodws

#### How 2 use
- Manaul run
    1. Clone the project
    ```shell
    git clone https://github.com/Dragonfly911117/PDF2TTF
    ```
    2. (Optional but recommanded) Active python virtual environment
    ```shell
    python -m venv venv

    # For bash-like shells
    source ./venv/bin/active

    # For Microsoft Command Prompt
    # venv/bin/active.bat
    ```
    3. Install dependencies
    ```shell
    pip install -r requirements.txt
    npm install
    ```
    4. Edit config.toml as needed
    5. Run scripts and check outputs
    ```shell
    python s1_pdf2png.py
    # This produces `${path.page_png}/${src.starting_page}.png` to `${path.page_png}/${src.ending_page}.png`(including).

    python s2_crop_page.py
    # This produces from the first characters in `${src.starting_page}.png` to the last one in`${src.ending_page}.png` in *both*`${path.rec_bound}` and `${path.cropped_png}`.

    node potrace.js
    # This produces `${path.svg}` and svg versions of characters from the last step.
    
    node run_pico.js
    # This produces `${path.pico}` and processed svgs.

    node readfile.js
    # This combines previous files to `${path.final}/${file_name}` with its font name as ${font_name}.
    ```

- Cool script that does every thing above
    ```shell
    ./auto.sh
    ```
  
#### Progress
- [s1_pdf2pdf2png.py](s1_pdf2png.py): Able to read config and run in a43fa42

