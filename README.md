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

### trigram (MLP, 12K params)

```
robernard.
lrosławoj.
wita.
eufenwktryacieolima.
jarosław.
dionifacy.
kyrsżgna.
toma.
zuza.
kunela.
wiols.
bogdaleria.
karołhlasta.
wena.
grzej.
irmgard.
zdy.
dionarda.
sylwebastan.
radela.
```

### gru (4-layer, 64-d, 29K params)

Novel names generated with `makemore` from `data/names/polish_first_names.txt`:

```
wigtoga
marcikt
banna
gusława
ferginim
bazbit
matatara
andyla
kargarz
joreno
mobrust
jugetna
jlina
angiestyna
olta
leonsa
ronimeo
fwiłsz
bosławur
berysz
kaweleta
judzekty
buga
becjanora
izicen
barda
klana
baris
winizardis
jawolt
ewomuek
celiusz
wtannatra
emkandydta
murta
bomindzneta
lityna
marzery
tomar
ertand
adonata
semanda
jugentyna
dina
fapolia
ludmałd
frybotyna
loniga
agteno
```

### transformer (6-layer, 8-head, 128-d, 1.2M params)

Novel names generated with `makemore` from `data/names/polish_first_names.txt`:

```
parceli
bronika
artus
krysbin
izabelgna
riana
h
zazia
stewonia
walentyn
puliuspiusz
kuron
izaspim
krysp
ambroh
nerafin
nat
epolinera
zenonia
rozalś
florenty
jarand
mo
```

## Pan Tadeusz experiment

The experiment trains a character-level language model on the Polish national epic poem "Pan Tadeusz" by Adam Mickiewicz.

The model is a small transformer trained on the text of the poem, including punctuation and line breaks.

At this scale, the model does not generate coherent literary text, but it already learns Polish-looking character patterns, punctuation, line breaks, and pseudo-archaic rhythm.

## params

```bash
uv run python makemore/makemore.py \
  -i data/poem/pan_tadeusz_clean.txt \
  -o out/pan-tadeusz-small \
  --type transformer \
  --n-layer 2 \
  --n-head 4 \
  --n-embd 64 \
  --batch-size 64 \
  --learning-rate 5e-4 \
  --max-steps 10000
```

## sample

```
Kto zorawania, rozwany zrokoszą chcestą
*Śwam głowu, sadługa rzecz dymusze zaloska,
Fonko piseluje i schę laszk werzął dlamę,
Przerwała? Porwu; nitry uletki co grubka miru zada,
Lub teraz jednym gniko, ci ubisłaniej zanach,
Wypók Wojedarz cień nierzczyny swę ust oto,
Jako nim; po sowej na klejszcze Sercze;
Prawny zabrzyzna: żeśmy przekł na ołów.
Z zającym zwionie były i czekają dna —
Gsię ręzywała mował moa cofi i zaje
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
- https://www.youtube.com/watch?v=TCH_1BHY58I&list=WL&index=1&t=1s

--

- https://youtu.be/P6sfmUTpUmc?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ
