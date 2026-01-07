OUTDIR ?= ../outputs

.PHONY: all check run
all: check run

check:
	@echo "==> Zsh: syntax checks"
	@test -f basics.zsh && zsh -n basics.zsh || echo "basics.zsh not found"
	@test -f functions.zsh && zsh -n functions.zsh || true
	@test -f advanced.zsh && zsh -n advanced.zsh || true

run:
	@echo "==> Zsh: running demos"
	@mkdir -p "$(OUTDIR)"
	@test -f basics.zsh && zsh basics.zsh > "$(OUTDIR)/zsh_basics.txt" || echo "basics.zsh not found" > "$(OUTDIR)/zsh_basics.txt"
	@test -f functions.zsh && zsh functions.zsh > "$(OUTDIR)/zsh_functions.txt" || echo "functions.zsh not found" > "$(OUTDIR)/zsh_functions.txt"
	@echo "Wrote zsh outputs"

.PHONY: clean
clean:
	@# zsh has no build artifacts