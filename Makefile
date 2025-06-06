# ============================
# FAANG-Level Universal Framework Makefile
# ============================

# Dynamically fetch current branch
CURRENT_BRANCH := $(shell git rev-parse --abbrev-ref HEAD)

# 🔧 Install all Python dependencies
install:
	pip install -r requirements.txt

# 🧪 Run all tests using Pytest
test:
	pytest tests/ --disable-warnings -v

# 🧼 Run strict linting (E9, F63, F7, F82)
lint:
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

# 🚀 Run single test with PythonPath resolution
run:
	PYTHONPATH=. python3 tests/ui/test_login.py

# 📦 Freeze dependencies into requirements.txt
freeze:
	pip freeze > requirements.txt

# 📝 Create Pull Request to dev with interactive title/body
pr:
	@read -p "🔤 Enter PR Title: " title; \
	read -p "📝 Enter PR Description: " body; \
	gh pr create --base dev --head $(CURRENT_BRANCH) --title "$$title" --body "$$body"

# 🔍 Live tail logs from report directory
logs:
	tail -f reports/logs/*.log

# 🧹 Clean pycache and temporary test data
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	rm -rf .pytest_cache .coverage reports/html/*

#make install        # Install dependencies
#make run            # Run single test
#make test           # Run all tests
#make pr             # Raise PR with prompt
#make logs           # View real-time logs
#make clean          # Clean pycache and report junk
