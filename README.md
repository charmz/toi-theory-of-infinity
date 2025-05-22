# Math and Philosophy Research Project

This project integrates **GitHub**, **AWS S3**, **Milvus**, and **OpenAI GPT-4o** to automate the generation of rigorous academic papers intersecting mathematics, philosophy, and science.

## Project Structure

- **input**: Store source documents, datasets, and LaTeX templates.
- **output**: Generated LaTeX documents for publication.
- **scripts**: Automation scripts (Python) leveraging OpenAI and Milvus.
- **.github/workflows**: GitHub Actions workflows for automation.

## Quick Setup

1. Clone and navigate into the repository:
    ```powershell
    git clone https://github.com/your-username/math-philosophy-research.git
    cd math-philosophy-research
    ```

2. Install Python dependencies:
    ```powershell
    pip install -r requirements.txt
    ```

3. Sync local data with AWS S3:
    ```powershell
    aws s3 sync ./input s3://your-bucket/input
    ```

4. Use provided scripts to automate analysis and LaTeX generation.

## Integrations

- GitHub ↔ Overleaf for seamless LaTeX collaboration.
- AWS S3 for data storage.
- Milvus for semantic context retrieval.
- OpenAI (GPT-4o) for content analysis and generation.

## LaTeX Toolchain Setup

The repository includes source `.tex` files under `input/documents`. A minimal
TeX tool-chain is required in order to build the PDF outputs.

Install XeLaTeX along with language and font packages:

```bash
sudo apt-get install -y --no-install-recommends \
  texlive-xetex texlive-latex-recommended texlive-latex-extra \
  texlive-fonts-recommended texlive-fonts-extra texlive-lang-cjk \
  latexmk fonts-sil-ezra fonts-noto-cjk
```

`latexmk` keeps the build invocation the same across platforms.

### Bundling Required Fonts

The document preamble references **Libertinus Serif**, **Ezra SIL**, and
**Noto Serif CJK SC**. These are available through the packages above, or they
can be vendored inside a local `texmf/fonts/` directory and made available to
TeX with:

```bash
echo "export TEXMFHOME=\"$PWD/texmf\"" >> "$BASH_ENV"
mktexlsr "$PWD/texmf"
```

### Building the PDF

With the provided `latexmkrc`, a single command compiles the document:

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode draft2.tex
```

Running just `latexmk` will pick up the options from `latexmkrc`.
