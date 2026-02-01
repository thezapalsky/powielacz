# powielacz

## sample output

### bigram

```
a.
muenates.
kta.
olin.
winionererbisłana.
brnanabeliledzargilisła.
eusemia.
bin.
onacjufrdoruna.
brarttawła.
iagina.
tustaponaw.
ia.
enirteronaw.
orinawialikalośchaniusługelema.
amincja.
jarntalelfa.
mirofininnksłodolwiksła.
miarizeuradawellelusłolierusłatymina.
maryliudwidrelinemanda.
```

## development

all commands use `uv run` (no manual venv activation).

run a script:

```bash
uv run python main.py
```

run a module (once you add a package under `src/`):

```bash
uv run python -m <package_name>
```

tests:

```bash
uv run pytest
```

lint + format:

```bash
uv run ruff format .
uv run ruff check .
uv run ty check src/
```

## sources

- https://www.youtube.com/watch?v=PaCmpygFfXo&list=WL&index=3
- https://www.kaggle.com/datasets/djablo/list-of-polish-first-and-last-names?resource=download
