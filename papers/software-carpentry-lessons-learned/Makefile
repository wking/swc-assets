BIBTEX=bibtex
CONVERT=pandoc
LATEX=pdflatex
SCLL=software-carpentry-lessons-learned

all : ${SCLL}.pdf ${SCLL}.html

${SCLL}.pdf : ${SCLL}.tex ${SCLL}.bib
	${LATEX} ${SCLL}
	${BIBTEX} ${SCLL}
	${LATEX} ${SCLL}
	${LATEX} ${SCLL}

${SCLL}.html : ${SCLL}.md
	${CONVERT} < $< > $@

clean :
	@rm -f *~ *.aux *.bbl *.blg *.log *.pdf *.svn *.toc
