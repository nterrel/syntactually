"""Test that all scripts have valid syntax."""

import subprocess
from pathlib import Path

import pytest


class TestBashScriptsSyntax:
    """Test bash scripts for syntax errors."""

    @pytest.mark.parametrize(
        "script_name",
        ["basics.sh", "grep.sh", "awk.sh"],
    )
    def test_bash_script_syntax(self, bash_dir: Path, script_name: str) -> None:
        """Test bash script syntax with bash -n."""
        script_path = bash_dir / script_name
        assert script_path.exists(), f"Script not found: {script_path}"

        result = subprocess.run(
            ["bash", "-n", str(script_path)],
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0, f"Syntax error in {script_name}:\n{result.stderr}"

    def test_run_scripts_sh_syntax(self, repo_root: Path) -> None:
        """Test run_scripts.sh syntax."""
        script_path = repo_root / "run_scripts.sh"
        assert script_path.exists(), "run_scripts.sh not found"

        result = subprocess.run(
            ["bash", "-n", str(script_path)],
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0, f"Syntax error in run_scripts.sh:\n{result.stderr}"


class TestPerlScriptsSyntax:
    """Test perl scripts for syntax errors."""

    def test_perl_basics_syntax(self, perl_dir: Path) -> None:
        """Test perl basics.pl syntax."""
        script_path = perl_dir / "basics.pl"
        assert script_path.exists(), f"Script not found: {script_path}"

        result = subprocess.run(
            ["perl", "-c", str(script_path)],
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0, f"Syntax error in basics.pl:\n{result.stderr}"


class TestZshScriptsSyntax:
    """Test zsh scripts for syntax errors."""

    @pytest.mark.parametrize(
        "script_name",
        ["basics.zsh"],
    )
    def test_zsh_script_syntax(self, zsh_dir: Path, script_name: str) -> None:
        """Test zsh script syntax with zsh -n."""
        script_path = zsh_dir / script_name
        assert script_path.exists(), f"Script not found: {script_path}"

        result = subprocess.run(
            ["zsh", "-n", str(script_path)],
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0, f"Syntax error in {script_name}:\n{result.stderr}"


class TestPythonScriptsSyntax:
    """Test python scripts for syntax errors."""

    @pytest.mark.parametrize(
        "script_name",
        ["basics.py", "numpy_basics.py", "matplotlib_basics.py"],
    )
    def test_python_script_syntax(self, python_dir: Path, script_name: str) -> None:
        """Test python script can be compiled."""
        script_path = python_dir / script_name
        assert script_path.exists(), f"Script not found: {script_path}"

        result = subprocess.run(
            ["python3", "-m", "py_compile", str(script_path)],
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0, f"Syntax error in {script_name}:\n{result.stderr}"


class TestCppProgramsSyntax:
    """Test C++ programs for syntax errors."""

    @pytest.mark.parametrize(
        "program_name",
        ["basics.cpp"],
    )
    def test_cpp_program_syntax(self, cpp_dir: Path, program_name: str) -> None:
        """Test C++ program syntax with compiler check."""
        program_path = cpp_dir / program_name
        assert program_path.exists(), f"Program not found: {program_path}"

        result = subprocess.run(
            ["g++", "-std=c++20", "-fsyntax-only", str(program_path)],
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0, f"Syntax error in {program_name}:\n{result.stderr}"
