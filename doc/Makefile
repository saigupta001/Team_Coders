ps_sources := presentation.tex
ps_deps := $(wildcard ps_*.tex)

presentation: $(ps_sources) $(ps_deps)
	lualatex $(ps_sources)

clean:
	rm -f *.pdf *.aux *.log *.out *.nav *.toc *.snm
