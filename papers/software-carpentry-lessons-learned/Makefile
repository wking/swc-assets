LATEX=pdflatex
BIBTEX=bibtex
SCLL=software-carpentry-lessons-learned

all : ${SCLL}.pdf

${SCLL}.pdf : ${SCLL}.tex ${SCLL}.bib
	${LATEX} ${SCLL}
	${BIBTEX} ${SCLL}
	${LATEX} ${SCLL}
	${LATEX} ${SCLL}

clean :
	@rm -f *~ *.aux *.bbl *.blg *.log *.pdf *.svn *.toc
