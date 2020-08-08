
Step-by-step log of commands

1. Create virtual env

```
conda create --prefix ./.dvcenv python=3.7.8
```

2. Activate 

```
conda activate ./.dvcenv
```

3. Install requirements 

```
pip install -r requirements.txt
```

4. Init git repo 

```
git init
```

5. Init dvc 

```
dvc init
```

6. Configure artifact storage. NOTE: Here I stored it directly in repository, it is not how it supposed to be, never use current repo to store artifacs, read more https://dvc.org/doc/command-reference/remote/add

```
dvc remote add -d mylocal ./dvc-storage
```

7. DVC data 

```
dvc add data
git add .
git commit -m "Added data"
dvc push 
```

8. Add step 

```
dvc run -n step_1 -d scripts/action_a.py -d data/raw.txt -o output/step_1.txt "python -m scripts.action_a --input data/raw.txt --output output/step_1.txt"
dvc run -n step_2 -d scripts/action_b.py -d output/step_1.txt -o output/step_2.txt "python -m scripts.action_b --input output/step_1.txt --output output/step_2.txt"
dvc run -n step_3 -d scripts/action_c.py -d output/step_2.txt -o output/step_3.txt "python -m scripts.action_c --input output/step_2.txt --output output/step_3.txt"
```

9. Repro