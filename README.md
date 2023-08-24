<h1 align="center">
🎨 ColorFuse
</h1>

<img align="center" src="https://github.com/Axenide/ColorFuse/assets/66109459/9ba887ff-551f-450d-9d0c-492c698cd4c1">

<p align="center"><i>
A little CLI program written in Python for fusing colors in files that follow the same structure.
</i></p>

<p align="center"><small>
The example above shows Gruvbox (left) + Nord (right) resulting in Nordbox (heh...).
<br>
The program shown is <a href="https://github.com/neovim/neovim">Neovim</a> with <a href="https://github.com/Axenide/NvChad">my NvChad fork</a>.
</small></p>

#### Initial requirements
- Python 3.x
- Two files that follow the same structure but differ in their HEX colors. For example you can check [NvChad's base46 themes](https://github.com/NvChad/base46/tree/v2.0/lua/base46/themes).

## Usage
1. Run `main.py`
2. Input first file
3. Input second file
4. Input path to save the fused file
5. Enjoy 😎

It will return the fused file and a list with the colors it fused in order for you to reuse if needed.

## Roadmap
- [ ] Support for RRGGBBAA colors
- [ ] Support for RGBA colors
- [ ] GUI
- [ ] Proper install
