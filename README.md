# PRACTICAL - 1
## Implementing the First CI Pipeline Using GitHub Actions

MLOps - CI/CD Practical | Step-by-Step Implementation

---

**Aim:** Run Python unit tests automatically on every commit to `main` and observe a failing and a passing CI run.

**Repo name on GitHub:** `first-ci-demo` (separate repo)

### 1. Run locally
```powershell
python result_logic.py
python -m unittest discover -v
```
**Expected:** `Predicted Result: PASS`, `Ran 3 tests ... OK`.

### 2. Push to GitHub
```powershell
git init -b main
git add .
git commit -m "Add first CI workflow"
git remote add origin https://github.com/<your-username>/first-ci-demo.git
git push -u origin main
```

### 3. Controlled failure demo
```powershell
python scripts/failure_demo.py break      # commit "Modify result logic" -> red run
python scripts/failure_demo.py restore    # commit "Fix result prediction bug" -> green run
```

### Screenshots to preserve
- Repository with result_logic.py, test_result_logic.py, .github/workflows/ci.yml
- ci.yml
- First green run + expanded test log (3 tests OK)
- Red run + failure log (`AssertionError: 'FAIL' != 'PASS'`)
- Final green run

### Next: Practical 2
