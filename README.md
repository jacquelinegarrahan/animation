# animation
Animation repo


## Set up the repo
```bash
conda env create -f environment.yml
conda activate animation
```

## Run script
```bash
python wavefunction_sampling_pairs {filename(w/o .mp4)} {n pixels}
```


For example:
```bash
python wavefunction_sampling_pairs test 100
```

The file will be saved as text.mp4