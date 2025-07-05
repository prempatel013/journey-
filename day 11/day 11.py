"""
🏆 PYTHON DAY 11: PROFESSIONAL DEVELOPMENT WORKFLOW 🏆
Covers:
1. Project Packaging
2. Documentation
3. Testing & CI/CD
4. Collaboration Tools
5. Performance Optimization
"""

# ================ 1. PROJECT PACKAGING ================
print("\n" + "="*60 + "\n📦 1. PACKAGING YOUR CODE\n" + "="*60)

"""
📁 Sample Package Structure:
my_package/
├── __init__.py
├── core.py
├── utils/
│   ├── __init__.py
│   └── helpers.py
├── tests/
│   └── test_core.py
├── setup.py
├── pyproject.toml
├── README.md
└── requirements.txt
"""

# 🛠️ Example 1: setup.py Configuration
print("\nBasic setup.py example:")
setup_example = """
from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'requests>=2.25',
        'numpy'
    ],
    extras_require={
        'dev': ['pytest', 'black'],
        'docs': ['sphinx']
    },
    python_requires=">=3.8",
)
"""
print(setup_example)

# 🛠️ Example 2: Building and Installing
print("\nCommand Line Operations:")
print("""
# Build package
python setup.py sdist bdist_wheel

# Install locally
pip install -e .

# Upload to PyPI (requires account)
twine upload dist/*
""")

# ================ 2. DOCUMENTATION ================
print("\n" + "="*60 + "\n📝 2. PROFESSIONAL DOCUMENTATION\n" + "="*60)

# 🛠️ Example 3: Docstrings and Type Hints
def calculate_interest(principal: float, rate: float, years: int) -> float:
    """
    Calculate compound interest.

    Args:
        principal: Initial investment amount
        rate: Annual interest rate (e.g., 0.05 for 5%)
        years: Investment period in years

    Returns:
        Final amount after compound interest

    Examples:
        >>> calculate_interest(1000, 0.05, 10)
        1628.894626777442
    """
    return principal * (1 + rate) ** years

# 🛠️ Example 4: Generating Documentation
print("\nSphinx Documentation Steps:")
print("""
1. pip install sphinx
2. sphinx-quickstart docs
3. Edit docs/conf.py and docs/index.rst
4. sphinx-apidoc -o docs/source my_package
5. make html
""")

# ================ 3. TESTING & CI/CD ================
print("\n" + "="*60 + "\n✅ 3. TESTING & CONTINUOUS INTEGRATION\n" + "="*60)

# 🛠️ Example 5: Advanced Testing
import unittest
from unittest.mock import Mock, patch

class TestInvestment(unittest.TestCase):
    @patch('requests.get')
    def test_api_integration(self, mock_get):
        mock_get.return_value.json.return_value = {'rate': 0.05}
        from my_package.core import get_interest_rate
        rate = get_interest_rate()
        self.assertEqual(rate, 0.05)

# 🛠️ Example 6: GitHub Actions CI
print("\nBasic GitHub Actions Workflow (.github/workflows/test.yml):")
ci_example = """
name: Python CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -e .[dev]
    - name: Run tests
      run: |
        python -m pytest
"""
print(ci_example)

# ================ 4. COLLABORATION TOOLS ================
print("\n" + "="*60 + "\n👥 4. COLLABORATION WORKFLOW\n" + "="*60)

# 🛠️ Example 7: Git Pre-commit Hook
print("\n.pre-commit-config.yaml example:")
precommit_example = """
repos:
- repo: https://github.com/pre-commit/pre-commit-hooks
  rev: v4.0.1
  hooks:
    - id: trailing-whitespace
    - id: end-of-file-fixer
    - id: check-yaml
- repo: https://github.com/psf/black
  rev: 22.3.0
  hooks:
    - id: black
"""
print(precommit_example)

# 🛠️ Example 8: Code Review Automation
print("\nPull Request Template (.github/PULL_REQUEST_TEMPLATE.md):")
pr_template = """
## Description
What does this PR change?

## Related Issues
Fixes # (issue)

## Checklist
- [ ] Tests added
- [ ] Documentation updated
- [ ] CHANGELOG updated
"""
print(pr_template)

# ================ 5. PERFORMANCE OPTIMIZATION ================
print("\n" + "="*60 + "\n⚡ 5. PROFILING & OPTIMIZATION\n" + "="*60)

# 🛠️ Example 9: Profiling with cProfile
def profile_example():
    import cProfile
    import io
    import pstats
    from pstats import SortKey

    pr = cProfile.Profile()
    pr.enable()
    
    # Code to profile
    result = [x**2 for x in range(10**6)]
    
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats(SortKey.CUMULATIVE)
    ps.print_stats(10)
    print(s.getvalue())

print("\nProfiling example output:")
# profile_example()  # Uncomment to run

# 🛠️ Example 10: Memory Profiling
print("\nMemory profiling with memory_profiler:")
print("""
1. pip install memory_profiler
2. Add @profile decorator to function
3. Run: python -m memory_profiler script.py
""")

# ================ 🏆 6. CAPSTONE PROJECT ================
print("\n" + "="*60 + "\n🏆 6. PROFESSIONAL PROJECT SETUP\n" + "="*60)

class ProfessionalProject:
    def __init__(self, name):
        self.name = name
        self.structure = {
            'docs': ['conf.py', 'index.rst'],
            'tests': ['__init__.py', 'test_core.py'],
            'src': {
                self.name: ['__init__.py', 'core.py']
            },
            'config': ['setup.py', 'pyproject.toml']
        }
    
    def create(self):
        import os
        from pathlib import Path
        
        print(f"\nCreating project '{self.name}'...")
        for dirpath, files in self.structure.items():
            if isinstance(files, dict):
                for subdir, subfiles in files.items():
                    (Path(dirpath) / subdir).mkdir(parents=True, exist_ok=True)
                    for f in subfiles:
                        (Path(dirpath) / subdir / f).touch()
            else:
                Path(dirpath).mkdir(exist_ok=True)
                for f in files:
                    (Path(dirpath) / f).touch()
        
        # Create basic files
        with open('README.md', 'w') as f:
            f.write(f"# {self.name}\n\nProfessional Python project")
        
        with open('requirements.txt', 'w') as f:
            f.write("pytest\nblack\nmypy\n")
        
        print("Project structure created!")

# Usage
project = ProfessionalProject("my_awesome_package")
# project.create()  # Uncomment to generate project structure

# ================ 🚀 7. CONTINUING JOURNEY ================
print("\n" + "="*60 + "\n🚀 7. NEXT STEPS IN YOUR PYTHON JOURNEY\n" + "="*60)
print("""
1. Open Source Contribution:
   - Find projects on GitHub
   - Start with documentation fixes
   - Follow project contribution guidelines

2. Specialization Paths:
   ↗️ Web Development: FastAPI/Django, HTML/CSS
   ↗️ Data Science: Pandas, Scikit-learn, SQL
   ↗️ DevOps: Docker, Kubernetes, AWS

3. Professional Growth:
   - Get Python certified (PCAP, PCPP)
   - Build a portfolio
   - Contribute to PyPI packages

4. Advanced Topics:
   - Metaprogramming
   - C extensions (Cython)
   - Async architecture
""")

print("\n" + "="*60 + "\n🎉 CONGRATS ON COMPLETING PYTHON PROFESSIONAL WORKFLOW! 🎉\n" + "="*60)