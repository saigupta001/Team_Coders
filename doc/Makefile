ps_sources := presentation.tex
rp_sources := report.tex
ps_deps := $(wildcard ps_*.tex)
rp_deps := $(wildcard rp_*.tex)

report: $(rp_sources)

presentation: $(ps_sources) $(ps_deps)
	lualatex $(ps_sources)

report: $(rp_sources) $(rp_deps)
	lualatex -shell-escape $(rp_sources)

all: presentation report

clean:
	rm -f *.pdf *.aux *.log *.out *.nav *.toc *.snm
